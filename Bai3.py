input = "[2,1 ,4, 3, 7 ,4,1]"
input = list(set(int(i) for i in input.strip("[] ").split(",")))
input.sort(reverse=True)
print(input)