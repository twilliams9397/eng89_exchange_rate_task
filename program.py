from app.currency_function import CurrencyExchange
import json

data = open("exchange_rates.json", "r")
currency_data = json.load(data)

CurrencyExchange.show_base(currency_data)
CurrencyExchange.show_list(currency_data)

