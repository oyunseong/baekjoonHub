n = int(input())
arr= [0,1]

for i in range(n):
    arr.append(arr[-1] + arr[-2])
   
print(arr[n])