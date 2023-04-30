
class Currency:
    def __init__(self, name, symbol, desc=None):
        self.name = name
        self.symbol = symbol
        self.desc = desc

    def get_name(self):
        return str(self.name)

    def get_symbol(self):
        return str(self.symbol)

    def get_description(self):
        return str(self.desc)
