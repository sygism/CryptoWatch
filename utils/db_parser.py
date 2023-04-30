import json
import pandas as pd


class DatabaseParser(str):
    def __init__(self, location):
        try:
            self.frame = pd.read_json(location)
        except FileNotFoundError:
            print("Internal error: Missing Crypto database .json file!")

    def get_raw_frame(self):
        return self.frame

    def get_description_by_symbol(self, symbol):
        return self.frame["Description"].where(self.frame["Designator"] == symbol)[0]


if __name__ == "__main__":
    instance = DatabaseParser('../crypto_db.json')
    print(str(instance.get_description_by_symbol('BTC')))


