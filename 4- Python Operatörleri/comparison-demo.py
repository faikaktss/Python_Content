
# 1- Girilen 2 sayıdan hangisi büyüktür ?

# a = int(input('a: '))
# b = int(input('b: '))

# result = (a > b)
# print(f"a: {a} b: {b} den büyüktür: {result}")

# 2- Kulalnıcıdan 2 vize (%60) ve final (%40) notunu
#    alıp ortalama hesaplayınız, Eğer ortalama 50 ve
#    üstündeyse geçti değilse kaldı yazdırın

# vize1 = float(input('1. vize: '))
# vize2 = float(input('2. vize: '))
# final = float(input('final: '))

# ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)

# print(f"not ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama>=50}")

# 3-Girilen bir sayınıntek mi çift mi olduğunu yazdırın.

# sayi = int(input('sayı: '))

# tekcift = (sayi % 2 == 0)

# print(f"girilen sayı çift olma durumu {tekcift}")

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın

# sayi = int(input('sayı: '))

# negatifpozitif = (sayi % 2 == 0)

# print(f"girilen sayı poazitif olma durumu {negatifpozitif}")

# 5-Parola ve email bilgsinin isteyip doğruluğunun 
#   kontorl ediniz (email: email@faik.com parola: abc123)

email ='email@faikaktas.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('parola: ')

isEmail = (email == girilenEmail.lower())
isPassword = (password == girilenPassword.lower())

print(f"Email bilgisi doğrumu: {isEmail} ve parola doğrumu: {isPassword}")