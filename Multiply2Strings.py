def convertStrtoInt(vl):
    num=0
    for i in vl:
        num=num*10 + (ord(i) - 48)
    return num
n1=(input("num 1 - "))
n2=(input("num 2 - "))
res = (convertStrtoInt(n1) * convertStrtoInt(n2))
print(res)
print(type(res))
