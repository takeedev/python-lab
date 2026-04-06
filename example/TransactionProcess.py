transactions = [
    {"id": "T1", "user": "A", "amount": 100, "type": "credit"},
    {"id": "T2", "user": "A", "amount": 50, "type": "debit"},
    {"id": "T3", "user": "B", "amount": 200, "type": "credit"},
    {"id": "T4", "user": "A", "amount": None, "type": "credit"},
    {"id": "T5", "user": "B", "amount": -10, "type": "debit"},
    {"id": "T6", "user": "C", "amount": 300, "type": "credit"},
]




for t in transactions:
    if t.get("amount") is None:
        continue
    elif t.get("amount") < 0:
        print("invalid transaction:", {t.get("id")})
    

