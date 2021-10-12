import requests


resp = requests.get("https://newsapi.org/v2/everything", params={"q":"Trump", "apiKey": "d2fc5fadf24b456db9bdd392a2249d65"})


# print(resp.json())

data = resp.json()

print(data['articles'][2])