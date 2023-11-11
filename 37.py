canh = int(input("Nhap vao so canh: "))
if canh < 3 or canh > 10:
    print("Loi: So canh phai nam trong khoang tu 3 den 10.")
else:
    hinhdang = {
        3: "Tam giac",
        4: "Tu giac",
        5: "Ngu giac",
        6: "Luc giac",
        7: "That giac",
        8: "Bat giac",
        9: "Cuu giac",
        10:"Thap giac"
        }
    hinhdang = hinhdang[canh]
    print(f"Hinh co {canh} canh la hinh {hinhdang}.")