while True:
    try:
        print("Nhap ho va ten: ",end="")
        ten = input()
        print(ten)
        print("Nhap tuoi: ",end="")
        tuoi = int(input())
        break
    except:
        pass
print(ten,": " ,tuoi,"tuoi")
