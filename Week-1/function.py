#definition

def ortalamaHesapla():
    final = 69
    vize = 87
    ortalama = (vize* 0.4) + (final* 0.6)
    print(ortalama)

def ortalamaHesaplaveDöndür():
    final = 69
    vize = 87
    ortalama = (vize* 0.4) + (final* 0.6)
    return ortalama

ortalamaHesapla()
print(ortalamaHesaplaveDöndür())

def ortalamaHesapla(vize, final):
    return (vize * 0.4) + (final * 0.6)

print(ortalamaHesapla(50,78))

vize = int(input("vize notunuzu giriniz: "))
final = int(input("final notunuzu giriniz: "))

def ortalamaHesaplaveYazdır(vize=vize, final=final):
    return (vize * 0.4) + (final * 0.6)

print(ortalamaHesaplaveYazdır())