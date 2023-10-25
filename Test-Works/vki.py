#Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
boy  = float(input("\nLütfen boyunuzu 'metre' cinsinden yazınız: "))
kilo = float(input("\nLütfen ağırlığınızı 'kilogram' cinsinden yazınız: "))
if boy >= 1.60 and kilo > 50:
    bki = round(kilo/(boy**2))
    if bki<=18.5:
        print(f"\nBeden kitle indeksiniz: {bki}, zayıfsınız")
    elif bki >18.5 and bki < 25:
        print(f"\nBeden kitle indeksiniz: {bki}, normalsiniz")
    elif bki >=25 and bki < 30:
        print(f"\nBeden kitle indeksiniz: {bki}, kilolusunuz")
    elif bki >= 30 and bki < 35:
        print(f"\nBeden kitle indeksiniz: {bki}, obezsiniz")
    else:
        print(f"\nBeden kitle indeksiniz: {bki}, morbid obezsiniz")
else:
    print("\nLütfen vücut değerlerinizi doğru giriniz")