def main():
    try:
        sayi = float(input("Lütfen bir sayı girin: "))
        if sayi > 100:
            print(f"{sayi}, 100'den büyüktür.")
        elif sayi < 100:
            print(f"{sayi}, 100'den küçüktür.")
        else:
            print(f"{sayi}, 100'e eşittir.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    main()