number = [1,2,3,4,5,6,7]
## continue
for n in number:
    if n == 3:
         continue
    print(n)

print("-----------------")
## break
for n in number:
    if n == 3:
        break
    print(n)





users = [
    {"name": "A", "age": 20},
    {"name": "B", "age": None},
    {"name": "C", "age": 30}
]
for u in users:
    if u.get("age") is None:
        continue
    if u.get("age") >= 25:
        print(u.get("name"))




userBreak = [
    {"name": "A", "age": 20},
    {"name": "B", "age": 30},
    {"name": "C", "age": 40}
]
for u in userBreak:
    if u["age"] > 25:
        print(u["name"])
        break

userNext = [
    {"name": "A", "age": 20},
    {"name": "B", "age": 30}
]
found = next((u for u in userNext if u["name"] == "B"), None)
print(found)

## loop range 100
for _ in range(100):
    print("TEST LOOP")


## loop range 0 to 99
for _ in range(0,100):
    print(_)
