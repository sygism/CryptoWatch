import json
import pandas as pd


class DatabaseParser(str):
    def __init__(self, location):
        try:
            self.frame = pd.read_json(location)
        except FileNotFoundError:
            print("Internal error: Missing Crypto database .json file!")


if __name__ == "__main__":
    instance = DatabaseParser('../crypto_db.json')
    print(str(instance.frame))


