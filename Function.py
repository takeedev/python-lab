## Default function
def greet(name):
    return f"Hello {name}"
print(greet("Junior"))

## multiple return
def calculate(a,b):
    return a + b , a * b
sum_val , mul_val = calculate(10,10)
print(sum_val)
print(mul_val)


def calculates(a,b):
    return a + b , a * b, a - b, a / b
sum_vals , mul_vals , d_vals, b_vals = calculates(10,10)
print("บวก", sum_vals)
print("คูณ",mul_vals)
print("ลบ",d_vals)
print("หาร",b_vals)
