#***YAPILACAK****
#***ÖNCEDEN YAPILMIŞTI***

'''
1-Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.


sayi = float(input('sayı: '))
result = (sayi > 0) and (sayi<=100)

if result:
    print('sayı 0-100 arasında.')
else:
    print('sayı 0-100 arasında değildir')

'''




'''
2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.



'''

sayi = int(input)
'''
3- Email ve parola bilgileri ile giriş kontroolü yapınız.

email = 'email@faikaktas.com'
passwrod = 'abc123'

girilenEmail = input('email: ')
girilenPassword = input('passwrod: '

result = (girilenEmail == email) and (girilenPassword == password)
print(f'uygulama giriş başarılı mı: {result}')

'''


'''
4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

result = (a > b) and (b > c)
print(f'a en büyük sayıdır: {result})

result = (b > a) and (b > c)
print(f'b en büyük sayıdır : {result})

result =  (c > a) and (c > b)
print(f'c enbüyük sayıdır : {result})

'''

'''
5- Kullanıcdıan 2 vize (%60) ve final(%40) notunu alıp ortalam hesaplayınız
    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
    b-) Finalden 70 alınıdğında ortalamaının önemi olmasın
vize1 = float(input('vize1: '))
vize2 = float(input('vize2: ))
final = float(input('final: ))

ortalmaa = ((vize1+vize2)/2)*0..6 + (final * 0.4)
result = (ortalama>=50) and (final>=50)
result = (ortalama>=50) or (final>=70)

print(f'öğrencinin ortalamsı: {ortalama } ve geçme durumu: {result})

'''