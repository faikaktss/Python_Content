### HATA ###

import requests
import json

api_url = "https://api.exchangeratesapi.io/v1/latest"

bozulan_doviz = input("bozulan döviz türü: ")
alinan_doviz = input("alınan döviz türü: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

result = requests.get(api_url+bozulan_doviz)
result = json.loads(result.text)

print(result)