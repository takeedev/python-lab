transactions : list = [
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

def process_transaction(user):
    balances : int = 0
    for r in transactions:
        if r.get("user") == user:
            if r.get("amount") is None or r.get("amount") < 0:
                continue 
            elif r.get("type") == "credit":
                balances += r.get("amount") 
            else:
                balances -= r.get("amount")
    return balances
    
user: list = []
for e in transactions: 
    user.append(e.get("user"))

distinct: list = list(dict.fromkeys(user))


output: list = []
for d in distinct:
    amount = process_transaction(d)
    output.append((d, amount))

print("User Balances:", output)

for user, balance in output:
    print(f"User: {user}, Balance: {balance}")