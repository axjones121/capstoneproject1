import requests
import random


randonum = random.randint(1, 25)

resp = requests.get("https://newsapi.org/v2/everything", params={"qInTitle":"coronavirus", "from": "2021-11-01", "apiKey": "d2fc5fadf24b456db9bdd392a2249d65"})


# print(resp.json())

data = resp.json()



print(data['articles'][0])


#make sure your in right folder
#ipython
#%run app.py