import math
print("Left = ",end="")
left = int(input())
print("Right = ",end="")
right = int(input())
arr = []
def check_palindrome(num):
    return str(num) == str(num)[::-1]
for i in range(int(math.sqrt(left)),int(math.sqrt(right))):
    if (check_palindrome(i) and check_palindrome(i*i)):
        arr.append(i*i)
print(arr)