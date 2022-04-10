import requests


def get_amount_of_currencies(amount = 10):
    crypto_currencies = []
    r = requests.get("https://api.coinlore.net/api/tickers/")
    for i in range(amount + 1):
        if r.json()["data"][i]["symbol"] != "USDT":
            crypto_currencies.append(r.json()["data"][i])
    return crypto_currencies


def get_markets(amount = 10):
    crypto_prices = []
    avoid = ['BCex', None]
    for i in range(amount):
        crypto_markets = []
        symbol = get_amount_of_currencies()[i]
        r = requests.get(f"https://api.coinlore.net/api/coin/markets/?id={symbol['id']}")
        result = r.json()
        for coin in result:
            if coin["base"] == symbol["symbol"] and coin["name"] not in avoid:
                crypto_markets.append({'Market': coin['name'], 'Price': coin['price_usd']})
        sorted_prices = sorted(crypto_markets, key=lambda price: price['Price'])
        prices = [sorted_prices[0], sorted_prices[-1]]
        crypto_prices.append(prices)
    return crypto_prices




def to_be_printed(amount = 10):
    for i in range(amount):
        first = get_amount_of_currencies()
        second = get_markets()
        profit = ((second[i][1]["Price"] - second[i][0]["Price"])/second[i][0]["Price"]) * 100
        print(first[i]["name"],
              second[i][0]["Market"],
              round(second[i][0]["Price"], 3),
              second[i][1]["Market"],
              round(second[i][1]["Price"], 3),
              round(profit, 3)
              )


test = to_be_printed()
