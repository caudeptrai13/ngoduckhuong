while True:
    try:
        print("Nhap ho va ten: ",end="")
        ten = input()
        print("Nhap tuoi: ",end="")
        tuoi = int(input())
        break
    except:
        pass
print("""Ho va ten la : {0}
Tuoi la : {1}""".format(ten.strip().title(),tuoi))
