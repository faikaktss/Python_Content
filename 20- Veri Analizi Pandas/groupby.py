import pandas as pd

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Yılmaz','Çınar Turan','Faik Aktaş'],
    'Departman':['İnsan kaynakları','Bilgi işlem','Muhasebe','İnsan kaynakları'],
    'Yaş' : [30,23,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,2750,6500,4500]
}

df = pd.DataFrame(personeller)

result = df

print(result)