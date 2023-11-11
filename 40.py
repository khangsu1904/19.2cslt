c1=int(input("Do dai canh 1: "))
c2=int(input("Do dai canh 2: "))
c3=int(input("Do dai canh 3: "))
if c1==c2==c3:
    tg="Tam giac deu"
elif c1==c2 or c2==c3 or c1==c3:
    tg="Tam giac can"
else:
    tg="Tam giac thuong"
print("La",tg)
    
