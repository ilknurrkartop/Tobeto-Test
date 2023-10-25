Not = int(input("Lütfen notunuzu giriniz.")) #klavyeden aldığım değer
#print(type(Not))
#NotAsInteger = int(Not)
#print(type(NotAsInteger))

#if else koşullu ifadesi kullanımı
if Not >80 :
    print("Harika, geçtiniz")
    if Not >90:
        print("Bravo")
#else if
elif Not >50:
    print("Başarılı")
else:
    print("Kaldınız")