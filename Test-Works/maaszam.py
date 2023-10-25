#Maaş ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
maas = float(input("Lütfen maas giriniz:"))
zamOrani= float(input("Lütfen zam oranının yüzdesini girin:"))
yenimaas = maas*((100+zamOrani)/100)
print("Yeni maasiniz:" + str(yenimaas))
