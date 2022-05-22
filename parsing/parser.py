from bs4 import BeautifulSoup
from numpy import true_divide
import requests
import pandas as pd
url = "https://coinmarketcap.com/"

headers = {
     "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.3.852 Yowser/2.5 Safari/537.36"
}

def search(coin: str):
    search_results = dataframe[dataframe.eq(coin).any(1)]
    if(not search_results.empty):
        return search_results
    else:
        return 'Not found'

resp = requests.get(url, headers=headers).text
soup = BeautifulSoup(resp, "html.parser")
tbody = soup.tbody
coins = tbody.find_all("tr")[0:10]
coins_list = list()

for coin in coins:
    p_tags =  coin.find_all("p")
    span_tags =  coin.find_all("span")
    data = {'cripto_name': p_tags[1].text, 'price': span_tags[2].text, 'market_cap': span_tags[8].text}
    coins_list.append(data)
dataframe = pd.DataFrame(coins_list)

print(dataframe)

dataframe.to_csv('criptocoin.csv', index=False)
while True:
    print("\n" 'Для нахождения криптовалюты введите ее название: ',end=" ")
    print(search(str(input())))
