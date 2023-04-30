from PyQt6.QtWidgets import QVBoxLayout, QLabel


class FavouritesListView:

    def __init__(self, currencies):
        self.layout = QVBoxLayout()

        title = QLabel()
        title.setText("Favourites")
        title.setStyleSheet(
            "color: #f5f5f5;"
            "font-size: 18px;"
            "font-weight: bold;"
            "margin-top: 100px;"
        )
        self.layout.addWidget(title)

        for item in currencies:
            coin = QLabel()
            coin.setText(item.get_name() + " (" + item.get_symbol() + ")")
            coin.setStyleSheet(
                "color: #f5f5f5;"
                "font-size: 12px;"
                "border-bottom: 1px solid black;"
                "margin-top: 5px;"
            )
            self.layout.addWidget(coin)

        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch()

    def get_layout(self):
        return self.layout
