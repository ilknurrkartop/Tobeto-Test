print("Merhaba Tobeto Test Ekibi")

#değişkenler 
#metinsel => STRING
text = "Merhaba"
print(text)

#numerik =>INT,INTEGER - Tam Sayı
studentCount=45
print(studentCount)

studentCount2="50"
#print(studentCount+studentCount2)

#double,decimal,float => ondalık sayı
averagePoint=25.5
print(averagePoint)

#boolean => true-false (0,1)
isVerified = True
print(isVerified)

print(type(studentCount))
print(type(studentCount2))
print(type(averagePoint))
print(type(isVerified))

#operatörler 
#matematiksel + - * / % 
number = 10

print(number + number)
print(number - number)
print(number * number)
print(number / 2)
#sol taraftaki değerin sağdaki değere bölümünden kalan sonuç olur
print(number % 3)

#mantıksal operatörler

print(number == 10) #true
print(number == 11) #false

print(number != 10) #false
print(number != 11) #true

print(number > 10) #false
print(number >= 10) #true

print(number < 10) #false
print(number <= 10) #true

#string interpolation => metin birleştirme

hello = "merhaba"
userName = "irem"

totalText = hello +" "+ "irem"
print(totalText)

totalText = "{message} Sayın {name}".format(message="Selam", name=userName)
print(totalText)

#f-string
totalText = f"Hoşgeldiniz {userName}"
print(totalText)

