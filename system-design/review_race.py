"""A local database boundary for stale approval. No network or patient data."""
import json
from pathlib import Path
import sqlite3
import tempfile

class StaleReview(Exception):
    pass

def connect(path):
    return sqlite3.connect(path, isolation_level=None, timeout=5)

def initialize(path):
    with connect(path) as db:
        db.executescript('''
        CREATE TABLE packet(id TEXT PRIMARY KEY, version INTEGER NOT NULL,
                            body TEXT NOT NULL, approved_version INTEGER);
        CREATE TABLE intent(case_id TEXT PRIMARY KEY, version INTEGER NOT NULL,
                            body TEXT NOT NULL, request_key TEXT UNIQUE NOT NULL);
        INSERT INTO packet VALUES ('PA-1042',1,'synthetic packet v1',NULL);
        ''')

def approve(db):
    # A trusted mock staff action; production needs authenticated reviewer identity.
    db.execute("UPDATE packet SET approved_version=version WHERE id='PA-1042'")

def edit(db, body):
    db.execute('BEGIN IMMEDIATE')
    try:
        if db.execute('SELECT 1 FROM intent').fetchone():
            raise StaleReview('Intent exists; use an explicit amendment workflow')
        db.execute("UPDATE packet SET version=version+1,body=?,approved_version=NULL WHERE id='PA-1042'",(body,))
        db.commit()
    except Exception:
        db.rollback()
        raise

def record_intent(db):
    db.execute('BEGIN IMMEDIATE')
    try:
        old=db.execute('SELECT request_key FROM intent WHERE case_id=?',('PA-1042',)).fetchone()
        if old:
            db.commit()
            return old[0]
        version,body,approved=db.execute("SELECT version,body,approved_version FROM packet WHERE id='PA-1042'").fetchone()
        if approved != version:
            raise StaleReview('Current packet needs review')
        key=f'PA-1042:v{version}'
        db.execute('INSERT INTO intent VALUES (?,?,?,?)',('PA-1042',version,body,key))
        db.commit()
        return key
    except Exception:
        db.rollback()
        raise

def demo():
    with tempfile.TemporaryDirectory() as folder:
        path=Path(folder)/'case.db';initialize(path)
        reader,editor=connect(path),connect(path)
        try:
            approve(reader)
            snapshot=reader.execute('SELECT version,approved_version FROM packet').fetchone()
            edit(editor,'synthetic packet v2')
            print('Worker A cached:',json.dumps(snapshot))
            print('Worker B edited: version 2; approval cleared')
            try:record_intent(reader)
            except StaleReview as error:print('Submission blocked:',error)
            approve(reader)
            first=record_intent(reader);second=record_intent(editor)
            print('Fresh review:',first)
            print('Repeated intent returns same key:',first==second)
            print('Durable intents:',reader.execute('SELECT count(*) FROM intent').fetchone()[0])
            print('No remote submission occurred; external idempotency remains a separate contract.')
        finally:
            reader.close();editor.close()

if __name__=='__main__':demo()
