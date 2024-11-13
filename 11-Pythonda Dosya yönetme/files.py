# Dosya açmak veya oluşturmak için open() fonksiyonu
# kullanılır.
# Kullanımı: open(dosya_adi, dosyerişme_modu)
# dosya_erişme_modu => dosyayaı hangi amaçla açtığımız belirtir

# "w": (Write) yazma modu. 
#   ** Dosyayı konumda oluşturur.
#   ** Dosya içeriğinin siler ve yeniden ekleme yapar

# file = open("newfile.txt","w")
# file= open("C:/Users/faika/desktop/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding='utf-8')
# file.write("Faik Aktaş")
# file.close

# "a": (Append) ekleme. Dosya konumda yoksa oluşturur

# file = open("newfile.txt","a",encoding='utf-8')
# file.write("\nFaik aktaş")
# file.close()

# "x": (Create) oluşturma. Doysa zaten varsa hata verir

file = open("newfile2.txt","x",encoding='utf-8')

# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir