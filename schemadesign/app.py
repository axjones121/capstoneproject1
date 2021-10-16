import requests
import random


randonum = random.randint(1, 25)

resp = requests.get("https://newsapi.org/v2/everything", params={"q":"usa", "from": "2021-10-12", "apiKey": "d2fc5fadf24b456db9bdd392a2249d65"})


# print(resp.json())

data = resp.json()

print(data)