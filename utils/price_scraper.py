import pandas as pd
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from dotenv import load_dotenv
import os
from datetime import date


class PriceScraper(str):

    def __init__(self, params):
        # Load environment variables
        load_dotenv()
        self.live_price = 0
        self.currency = params[1]
        self.designator = params[0]
        self.api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
        self.instance = CryptoCurrencies(key=self.api_key)
        self.df = None
        self.fetch_pricing_data()

    def fetch_pricing_data(self):
        root_dir = '/'.join(str(__file__).split('/')[:-2])
        if os.path.exists('{0}/cache/{1}_price_data.csv'.format(root_dir, self.designator)):
            df = pd.read_csv('{0}/cache/{1}_price_data.csv'.format(root_dir, self.designator))
            print(str(df))
            if str(date.today()) in df.keys():
                self.df = df
        else:
            data, metadata = self.instance.get_digital_currency_daily(symbol=self.designator,
                                                                      market=self.currency)
            self.df = pd.DataFrame.from_dict(data)
            self.df.to_csv('{0}/cache/{1}_price_data.csv'.format(root_dir, self.designator))

    def fetch_live_price(self):
        return self.instance.get_digital_currency_exchange_rate(from_currency=self.designator,
                                                                to_currency=self.currency)


if __name__ == "__main__":
    # c_instance = PriceScraper(('BTC', 'EUR'))
    # print(str(c_instance.df))
    # print(str(date.today()))
    print(str('/'.join(str(__file__).split('/')[:-2])))
