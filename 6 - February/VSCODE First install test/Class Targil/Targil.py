import requests
for i in range (0, 10):
    response = requests.get("https://randomuser.me/api")
    print(response.json())