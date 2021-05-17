def name(a):
    return a[0]
def age(a):
    return a[1]
def sex(a):
    return a[2]
def type(a):
    if a[1] < 15:
        return 0
    elif a[1] > 60:
        return 1
    else: return 2
def four(a):
    return (type(a), age(a), -len(sex(a)), name(a))
arr = [
        # Tên, tuổi, giới tính
        ("A", 18, "nam"),
        ("B", 23, "nữ"),
        ("C", 65, "nam"),
        ("D", 62, "nữ"),
        ("E", 6, "nam"),
        ("F", 12, "nữ")
    ]
arr.sort(key=name)
print(arr)
arr.sort(key=age)
print(arr)
arr.sort(key=sex,reverse=True)
print(arr)
arr.sort(key=four)
print(arr)