from PyQt6.QtWidgets import (QWidget, QLineEdit, QCompleter, QAbstractItemView)
import pandas as pd


class SearchBar(QWidget, pd.DataFrame):

    def __init__(self, db):
        super(SearchBar, self).__init__()
        self.searchbar = QLineEdit()
        self.searchbar.setFixedWidth(400)
        self.searchbar.setStyleSheet(
            "background-color: #222222;"
            "selection-background-color: #8D918D;"
            "color: #f5f5f5;"
            "border: 2px solid #27445C;"
            "border-radius: 5px;")
        # self.searchbar.addAction(":/../res/search.png", QLineEdit.ActionPosition.LeadingPosition)
        # self.searchbar.textChanged.connect(self.on_search)

        search_list = (db["Name"] + ' (' + db["Designator"] + ')').values.tolist()
        self.autocomplete = QCompleter(search_list)
        self.autocomplete.popup().setStyleSheet(
           "background-color: #222222;"
           "color: #f5f5f5;"
           "border: 2px solid #28445C;"
           "border-radius: 5px"
        )
        self.searchbar.setCompleter(self.autocomplete)


