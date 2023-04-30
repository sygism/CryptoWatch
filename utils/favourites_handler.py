import pandas as pd
from utils.Currency import Currency


class FavouritesHandler:

    def __init__(self, db):
        try:
            self.frame = pd.read_json('user_favourites.json')
            self.db = db
        except FileNotFoundError:
            print("Internal error: Missing Favourites database .json file!")

    def get_currencies(self):
        return list(map(lambda x: Currency(x[0], x[1], self.db.get_description_by_symbol(x[1])),
                        self.frame.values.tolist()))
