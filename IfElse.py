from Variable import price

age = 20

if age >= 18:
    print("Adult")
else:
    print("Child")


score = 80
if score >= 99:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")



x = 20
if x == 20:
    print("equal")
if x != 3:
    print("not equal")
if x > 5 and x < 30:
    print("in range")


name = None
if name is None:
    print("No name")


list = []
if not list:
    print("empty")


user = {"name": "Junior", "age": 28}
if user.get("age") > 24:
    print("Old enough")



users = [
    {"name": "A", "age": 20},
    {"name": "B", "age": 30}
]
for u in users:
    if u.get("age") >= 25:
        print(u["name"])