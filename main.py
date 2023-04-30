import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QFont, QIcon, QPixmap, QFontDatabase
from utils.db_parser import DatabaseParser
from widgets.SearchBar import SearchBar
from utils.price_scraper import PriceScraper
from widgets.PriceGraph import PriceGraph
from utils.favourites_handler import FavouritesHandler
from utils.Currency import Currency
from widgets.InfoBox import InfoBox
from widgets.FavouritesListView import FavouritesListView


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        container = QWidget()

        container_lout = QVBoxLayout()
        container.setLayout(container_lout)
        self.current_currency = None

        self.setCentralWidget(container)

        row1_container = QHBoxLayout()
        logo = QLabel()
        img = QPixmap('res/logo.png').scaled(25, 25)
        logo.setPixmap(img)
        row1_container.addWidget(logo)
        app_title = QLabel()
        app_title.setText("CryptoWatch")
        app_title.setStyleSheet(
            "color: #f5f5f5;"
            "font-size: 18px;"
        )
        row1_container.addWidget(app_title)
        row1_container.addStretch()
        db_parser = DatabaseParser('crypto_db.json')
        searchbar = SearchBar(db_parser.get_raw_frame())
        row1_container.addWidget(searchbar.searchbar)

        user_favourites = FavouritesHandler(db_parser)
        user_currencies = user_favourites.get_currencies()

        if len(user_currencies) == 0:
            self.current_currency = Currency('Bitcoin', 'BTC', db_parser.get_description_by_symbol("BTC"))
        else:
            self.current_currency = Currency(user_currencies[2].get_name(), user_currencies[2].get_symbol(),
                                             db_parser.get_description_by_symbol(user_currencies[2].get_symbol()))
        scraper = PriceScraper(self.current_currency, 'EUR')

        row2_container = QHBoxLayout()

        lv = FavouritesListView(user_currencies)
        row2_container.addLayout(lv.get_layout())

        graph_widget = PriceGraph(scraper.df)
        infobox = InfoBox(self.current_currency, scraper, graph_widget)
        row2_container.addLayout(infobox.get_layout_object())
        row2_container.addWidget(graph_widget.get_main_graph())

        container_lout.addLayout(row1_container)
        container_lout.addLayout(row2_container)

        # Import default font ('Roboto') for the application
        e_id = QFontDatabase.addApplicationFont('res/Roboto-Medium.ttf')
        if e_id < 0:
            print("Error loading font!")

        self.setFont(QFont(QFontDatabase.applicationFontFamilies(e_id)[0], 14))
        self.setStyleSheet("background-color: #222222;")
        self.setFixedSize(1280, 720)
        self.setWindowTitle("CryptoWatch")
        self.setWindowIcon(QIcon('res/logo.png'))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
