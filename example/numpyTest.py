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

## array operation
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b) 

## array filtering
arr1 = np.array([10, 20, 30, 40])
result = arr[(arr > 10) & (arr < 40)]
print(result)