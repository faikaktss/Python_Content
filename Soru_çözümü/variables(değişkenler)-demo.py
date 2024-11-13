# Ders 3.4
"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz

    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri tc kimlik 
    Müşteri doğum yılı
    Müşteri adres bilgisi
    Müşteri yaşı
"""

musteriAdi = "Faik"
musteriSoyad = "Aktaş"
musteriAdSoyad = musteriAdi + ' ' +musteriSoyad
musteriCinsiyet = True # Erkek
musteriTCKimlik = "12378979812"
musteriDogumYili = 2004  #  burdaki ifade string değil çünkü matematiksel bir işlem yapılcak
musteriAdresBilgisi = "Sedat özcan kyk yurdu"
musteriYas = 2023 - musteriDogumYili
print(musteriYas)

"""
    2- Aşağıdaki siparişerlin toplam bilgisini hesaplayınız

    Sipariş 1 => 110 tl
    Sipariş 2 => 1100.5 tl
    Sipariş 3 => 356.95 tl

"""

Siparis1 = 110 
Siparis2 = 1100.5 
Siparis3 = 356.95
total = Siparis1 + Siparis2 + Siparis3

print(total)