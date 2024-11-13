sayilar= [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hnagi sayılar 3'ün katıdır
for sayi in sayilar:
     if (sayi%3==0):
         print(sayi)


# 2- Saialr listesinde sayıların toplamı kaçtır?
toplam = 0
for sayi in sayilar:
     toplam += sayi
print('toplam:',toplam)


# 3- Sayilar listesindeki tek sayılaırn karesini alınız.

for sayi in sayilar:
    if (sayi % 2 == 1):
         print(sayi ** 2) 

sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# 4- Şehirlereden hangileri en fazla 5 karakterlidir?

for i in sehirler:
     if len(sehirler) <=5:
         print(i)

urunler =[
     {'name':'samsung S6',  'price': '3000'},
     {'name':'samsung S7',  'price': '4000'},
     {'name':'samsung S8',  'price': '5000'},
     {'name':'samsung S9',  'price': '6000'},
     {'name':'samsung S10',  'price': '7000'}
 ]

# 5- Ürünlerin fiyatları toplamı nedir
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print('toplam ürün fiyatı:', toplam)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz


for urun in urunler:
    if int(urun['price']) <=5000:
        print(urun['name'])