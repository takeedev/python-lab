user = {
    "name": "Junior",
    "age": 28
}
print("user ",user)

## Access
print("name access " ,user["name"])
print("age access " ,user["age"])

## Loop Dist and Add Dict
user["email"] = "test@gmail.com"
for key, value in user.items():
    print(key,value)


users = [
    {"name": "Junior","age": 28},
    {"name": "Takee","age": 23},
]
for u in users:
    print(u)