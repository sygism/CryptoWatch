import pandas as pd
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from dotenv import load_dotenv
import os
from datetime import date
from utils.Currency import Currency


class PriceScraper:

    def __init__(self, p_coin, market):
        # Load environment variables
        load_dotenv()
        self.live_price = 0
        self.currency = market
        self.designator = p_coin.get_symbol()
        self.api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
        self.instance = CryptoCurrencies(key=self.api_key)
        self.df = None
        self.fetch_pricing_data()

    def fetch_pricing_data(self):
        root_dir = '/'.join(str(__file__).split('/')[:-2])
        if os.path.exists('{0}/cache/{1}_price_data.csv'.format(root_dir, self.designator)):
            df = pd.read_csv('{0}/cache/{1}_price_data.csv'.format(root_dir, self.designator))
            if str(date.today()) in df.keys():
                self.df = df
                print("Fetched cached value for currency: {0}".format(self.designator))
            else:
                data, metadata = self.instance.get_digital_currency_daily(symbol=self.designator,
                                                                          market=self.currency)
                self.df = pd.DataFrame.from_dict(data)
                self.df.to_csv('{0}/cache/{1}_price_data.csv'.format(root_dir, self.designator))
        else:
            data, metadata = self.instance.get_digital_currency_daily(symbol=self.designator,
                                                                      market=self.currency)
            self.df = pd.DataFrame.from_dict(data)
            self.df.to_csv('{0}/cache/{1}_price_data.csv'.format(root_dir, self.designator))

    def fetch_live_price(self):
        price, metadata = self.instance.get_digital_currency_exchange_rate(from_currency=self.designator,
                                                                           to_currency=self.currency)
        return round(float(price["5. Exchange Rate"]), 3)


if __name__ == "__main__":
    coin = Currency('Bitcoin', 'BTC', "None")
    c_instance = PriceScraper(coin, 'EUR')
    # print(str(c_instance.df))
    # print(str(date.today()))
    print(str('/'.join(str(__file__).split('/')[:-2])))
