# Beginner lab (Part 1 of the book)

Two small files, standard library only, Python 3.10 or newer.

| File | What it shows |
|---|---|
| `payment_lab.py` | A pretend bank, a careless helper that pays twice, and a careful helper that uses a reference key and checks status before it speaks. No AI model is involved, on purpose. |
| `ask_model.py` | Win 6 (optional). A model reads an invoice with a hidden order. The model only proposes; the harness decides. Runs offline with a pretend, fooled model. |

```sh
python payment_lab.py
python ask_model.py
```

To try a real model, set `ANTHROPIC_API_KEY` and run `ask_model.py` again. The
real-model path has not been exercised in CI; the offline path is tested.
Everything here is fictional. No real payments, accounts or data.
