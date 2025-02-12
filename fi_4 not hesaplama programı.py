print("  NOT HESAPLAMA PROGRAMI")
print("══════════════════════════\n")

ad = input("Adınızı giriniz\t:")
n1 = int(input("1.Yazılının notu nedir\t:"))
n2 = int(input("1.Yazılının notu nedir\t:"))

ortalama = (n1+n2)//2
if n1>100 or n2>100 or n1<0 or n2<0:
    print("Geçersiz not girişi")
    print("Lütfen tekrar deneyiniz..")

else:
    if ortalama>90 : print(f"süper. ortalaman:{ortalama}")
    elif ortalama>80 : print(f"Güzel not ortalaman {ortalama}")
    elif ortalama>50 : print(f"Ortalama ile geçtin{ortalama}")
    else: print(f"Malesef {ortalama} ortalama ile kaldın.")