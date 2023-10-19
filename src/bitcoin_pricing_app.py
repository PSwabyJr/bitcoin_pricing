#bitcoin_pricing_app.py
import os
import requests

TWELVE_DATA_API_KEY = os.environ.get('TWELVE_DATA_API_KEY')
API_LINK = 'https://api.twelvedata.com'


def get_bitcoin_pricing_from_difference_currencies()->dict:
    ticker_list = ["BTC/USD", "BTC/EUR", "BTC/CAD", "BTC/GBP"]
    pricing = {}

    for ticker in ticker_list:
        try:
            link = f'{API_LINK}/time_series?apikey={TWELVE_DATA_API_KEY}&interval=1min&symbol={ticker}&format=JSON&type=none&outputsize=1'
            response = requests.get(link)
            closing_price = response.json()['values'][0]['close']
            currency_unit = response.json()['meta']['currency_quote']
            pricing[ticker] = (closing_price, currency_unit)
        except Exception as e:
            print(e)
            print("Error getting data for ticker: ", ticker)
            pricing[ticker] = ('Not', 'Found')
            continue
    
    return pricing

def summary_of_bitcoin_pricing_in_different_currencies(input:dict):
    print('Bitcoin Pricing Summary in Different Currencies')
    for key, value in input.items():
        try:
            print(f'Bitcoin price in {key} is {float(value[0])} {value[1]}s')
        except Exception:
            print(f'Unable to find Bitcoin price in {key}')
            continue


def main():
    pricing = get_bitcoin_pricing_from_difference_currencies()
    summary_of_bitcoin_pricing_in_different_currencies(pricing)

if __name__ == '__main__':
    main()



