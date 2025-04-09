from os import system
from colorama import Fore

system("cls")

def hesap():
    toplama="+"
    cikarma="-"
    carpma="x"
    bolme="%"

    secim=input(Fore.CYAN + "Yapacağınız İşlemi Seçiniz (+, -, x, %): ")
    sayi1=float(input("1.Sayı: "))
    sayi2=float(input("2.Sayı: "))
    
    if secim==toplama:
        print(Fore.GREEN + str(sayi1 + sayi2))
    elif secim==cikarma:
        print(Fore.GREEN + str(sayi1 - sayi2))
    elif secim==carpma:
        print(Fore.GREEN + str(sayi1 * sayi2))
    elif secim==bolme:
        print(Fore.GREEN + str(sayi1 / sayi2))
    else:
        print(Fore.RED + "Yanlış tuşa bastın mal.")


hesap()