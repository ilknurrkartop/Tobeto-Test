print("İlk Sayfa")
krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu Emekliler"]

#alias
for kredi in krediler:
  print("<option>"+ kredi + "<option>")

print("İkinci Sayfa")

krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu Emekliler"]

#alias
for kredi in krediler:
    print("<option>" + kredi + "<option>")

print("Üçüncü Sayfa")
krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu Emekliler"]

#alias
for kredi in krediler:
    print("<option>" + kredi + "<option>")

#ayrı ayrı yazmak yerine fonksiyon oluştur

def kredileriListele():
  krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel", "Mutlu Emekliler"]
  for kredi in krediler:
    print("<option>" + kredi + "<option>")
kredileriListele()