sayilar = [100,200,300,400,"Merhaba"]
#programcılar saymaya sıfırdan başlar.
print(sayilar[0])
print(sayilar)

#listenin sonuna eleman ekler.
sayilar.append(500)
print(sayilar)

#indexe göre siler(default son index)
sayilar.pop(2)
print(sayilar)

#değere göre siler
sayilar.remove(100)
print(sayilar)

#appendin aksine çoklu veri ekleme
sayilar.extend([10,20,30])
print(sayilar)

sayilar.clear()
print(sayilar)