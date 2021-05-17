f = open("text.txt","r",encoding='utf8')
line = f.read()
x = line.strip(",./ ").split()
diction = {}
for i in x:
    if i not in diction.keys():
        diction[i] = 1
    else:
        diction[i] = diction[i] + 1
max = 0
maxc = ""
for i in diction:
    if diction[i] > max:
        max = diction[i]
        maxc = i
print(maxc, max)
print(set(x))
print(diction)
