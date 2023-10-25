#Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
metin = input("Metni Giriniz: ")
ters=metin[::-1]
print ("Girilen metnin tersi:" , ters)

if ters == metin:
    print("Girilen metin palindromdur.")
else:
    print("Girilen metin palindrom değildir.")    