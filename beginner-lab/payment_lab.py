# payment_lab.py (Python 3.10+, nothing to install)

class Bank:
    """A pretend bank. The same reference is never paid twice."""
    def __init__(self, mode):
        self.mode = mode          # "reply_lost" or "request_lost"
        self.paid = {}            # reference -> amount
        self.first_call = True
        self.counter = 0

    def pay(self, amount, reference=None):
        first, self.first_call = self.first_call, False
        if first and self.mode == "request_lost":
            raise TimeoutError("request never arrived")
        if reference is None:     # no reference: a brand new payment
            self.counter += 1
            reference = f"auto-{self.counter}"
        self.paid.setdefault(reference, amount)
        if first and self.mode == "reply_lost":
            raise TimeoutError("reply lost on the way back")
        return "SUCCESS"

    def status(self, reference):
        return "SUCCESS" if reference in self.paid else "NOT_FOUND"

    def total_paid(self):
        return sum(self.paid.values())


def careless_pay(bank, amount):
    """First draft: if anything goes wrong, just try again."""
    try:
        bank.pay(amount)
    except TimeoutError:
        bank.pay(amount)
    return "Payment sent"


MESSAGES = {
    "SUCCESS": "Payment sent. The bank confirmed it.",
}

def careful_pay(bank, amount, reference, trail):
    """Second draft: keep a state, check before retrying, reuse the reference."""
    trail.append("REQUESTED")
    try:
        state = bank.pay(amount, reference)
    except TimeoutError:
        state = "UNKNOWN"                        # honest: we do not know yet
    trail.append(state)
    if state == "UNKNOWN":
        state = bank.status(reference)           # ask the bank. Never guess.
        trail.append("CHECKED:" + state)
        if state == "NOT_FOUND":
            state = bank.pay(amount, reference)  # same reference: safe to retry
            trail.append(state)
    return MESSAGES.get(state, "Payment pending. We are checking with your bank.")


def run(label, pay_fn, mode, *extra):
    bank = Bank(mode)
    message = pay_fn(bank, 48500, *extra)
    print(f"{label:8} {mode:12} says: {message}")
    print(f"{'':8} {'':12} bank really paid: Rs {bank.total_paid():,}")
    if extra:
        print(f"{'':8} {'':12} states: " + " > ".join(extra[-1]))


for mode in ("reply_lost", "request_lost"):
    run("careless", careless_pay, mode)
    run("careful", careful_pay, mode, "INV-2041", [])
