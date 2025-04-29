def linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1  

arr = [10, 15, 20, 25, 30, 80, 50]
target = 30

result = linear(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")