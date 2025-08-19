import requests

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print("Úspěšně vytvořeno:", response.json())
else:
    print(f"Chyba při odesílání dat: {response.status_code}")
