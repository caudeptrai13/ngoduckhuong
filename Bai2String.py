n = int(input())
dki = []
arr = {}
for i in range(n):
    dki.append(input())
dki.sort()
prev = ""
for i in range(n):
    now = dki[i]
    if now != prev:
        index = now.rfind(" ")
        ten, lop = now[:index], now[index+1:]
        if ten not in arr.keys():
            arr[ten] = 1
        else:
            arr[ten] += 1
    prev = now

print(arr)