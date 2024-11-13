# DERS 3.3

maasFaik = 5000
maasHasan = 4000
vergi = 0.27


print(maasFaik - (maasFaik * vergi))
print(maasHasan - (maasHasan * vergi))

# Değişken Tanımlama Kuralları

# 1- rakam ile başlayamaz (1number şeklinde başlayamaz)

number1 = 10
print(number1)

number1 = 20
print(number1)

number1+= 30 
print(number1)

# Büyük küçük harf duyarlılığı (age ile AGE i farklı algılar)

age = 20
AGE = 30

print(age)
print(AGE)

# Türkçe karakter kullanmayalım (Yani yaş yerine age kullanmalıyız)

yaş = 30
_age = 30

x = 1               # int               
y = 2.3             # float
name = "Çinar"      # string (toplama dahi olsa toplamaz ne gördüyse aynen yazar)
isStudent = True    # bool

#x, y, name, isStudent (1, 2.3, "Çınar", True)

a = "10"
b = "20"
print(a+b)  # normalde 30 olcak ama string bir ifade olduğu için toplamaz aynı şekilde yazar 1020

firstName = "Faik " # (kelimeler arası boşluk olmaz first Name yanlış kullanım)
lastName = "Aktas"

print(firstName + lastName) # Faık Aktas