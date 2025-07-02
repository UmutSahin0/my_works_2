import requests

url = "http://51.21.220.24:8000/count"
data = {"number": 10}  # Göndermek istediğin sayı

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Sonuç:", response.json()["result"])
else:
    print("Hata:", response.status_code, response.text)
