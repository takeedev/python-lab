transactions : list = [
    {"id": "T1", "user": "A", "amount": 100, "type": "credit"},
    {"id": "T2", "user": "A", "amount": 50, "type": "debit"},
    {"id": "T3", "user": "B", "amount": 200, "type": "credit"},
    {"id": "T4", "user": "A", "amount": None, "type": "credit"},
    {"id": "T5", "user": "B", "amount": -10, "type": "debit"},
    {"id": "T6", "user": "C", "amount": 300, "type": "credit"},
]

def process_transaction(transactions):
    balances : dict = {} 
    for t in transactions:

        user = t.get("user")
        tx_type = t.get("type")
        amount = t.get("amount")

        if t.get("amount") is None:
            continue
        elif t.get("amount") < 0:
            print("invalid transaction:", {t.get("id")})
            continue

        if tx_type == "credit":
            balances[user] = balances.get(user, 0) + amount
        else:
            balances[user] = balances.get(user, 0) - amount
    return balances

output = process_transaction(transactions)

for user, balance in output.items():
    print(f"User: {user}, Balance: {balance}")