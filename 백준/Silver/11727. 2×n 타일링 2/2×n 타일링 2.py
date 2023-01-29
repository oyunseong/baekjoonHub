n = int(input())
box = [0, 1, 3]

for i in range(n):
    box.append(box[-1] + box[-2] * 2)

print(box[n] % 10007)