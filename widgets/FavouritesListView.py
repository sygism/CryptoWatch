from PyQt6.QtWidgets import QVBoxLayout, QLabel, QPushButton
from utils.Currency import Currency


class FavouritesListView:

    def __init__(self, currencies, main_window, layout, container):
        self.layout = QVBoxLayout()

        self.layout.addStretch()
        title = QLabel()
        title.setText("Favourites")
        title.setStyleSheet(
            "color: #f5f5f5;"
            "font-size: 18px;"
            "font-weight: bold;"
        )
        self.layout.addWidget(title)

        for item in currencies:
            coin = QPushButton()
            coin.setText(item.get_name() + " (" + item.get_symbol() + ")")
            coin.setStyleSheet(
                "color: #f5f5f5;"
                "font-size: 12px;"
                "border-bottom: 1px solid black;"
                "margin-top: 5px;"
            )
            # TODO: FIXME, on any button clicked, item value is set the last iterated currency in the list
            coin.clicked.connect(lambda ch: main_window.update_window_with_user_currency(
                Currency(item.get_name(), item.get_symbol(), item.get_description()),
                layout, container, currencies))
            self.layout.addWidget(coin)

        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch()

    def get_layout(self):
        return self.layout
