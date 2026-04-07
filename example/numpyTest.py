import numpy as np

## 1D array
nums = np.array([1, 2, 3, 4])
result = nums * 2
print(result)


## 2D array Metrix
arr = np.array([
    [1, 2],
    [3, 4]
])
print(arr[0][1])  # 2

## array operation
amounts = np.array([100, 50, 200])
print(amounts.sum())

## rundom number
data = np.random.randint(1, 100, size=10)
print(data)


## statistics
arr = np.array([10, 20, 30, 40])
print(arr.min())
print(arr.max())
print(arr.std())