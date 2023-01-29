n = int(input())

arr = [0] * 91
arr[0] = 0
arr[1] = 1

for i in range(89):
    arr[i + 2] = arr[i + 1] + arr[i]
        
print(arr[n])