from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel
from PyQt6.QtGui import QPalette, QColor, QFont, QIcon, QPixmap
import sys
from utils.db_parser import DatabaseParser
from widgets.search_bar import SearchBar
from utils.price_scraper import PriceScraper
from widgets.main_graph import PriceGraph


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        container = QWidget()

        container_lout = QGridLayout()
        container_lout.setHorizontalSpacing(0)
        container.setLayout(container_lout)

        self.setCentralWidget(container)
        logo = QLabel()
        img = QPixmap('res/logo.png').scaled(25, 25)
        logo.setPixmap(img)
        container_lout.addWidget(logo, 0, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        app_title = QLabel()
        app_title.setText("CryptoWatch")
        app_title.setStyleSheet(
            "color: #f5f5f5;"
            "font-size: 18px;"
        )
        container_lout.addWidget(app_title, 0, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        db_parser = DatabaseParser('crypto_db.json')
        searchbar = SearchBar(db_parser.frame)
        container_lout.addWidget(searchbar.searchbar, 0, 2, QtCore.Qt.AlignmentFlag.AlignRight)

        scraper = PriceScraper(('ADA', 'EUR'))
        graph_widget = PriceGraph(scraper.df)

        container_lout.addWidget(graph_widget.price_graph, 1, 1, 2, 2, QtCore.Qt.AlignmentFlag.AlignRight)

        self.setFont(QFont('Roboto-medium', 14))
        self.setStyleSheet("background-color: #222222;")
        self.setFixedSize(1280, 720)
        self.setWindowTitle("CryptoWatch")
        self.setWindowIcon(QIcon('res/logo.png'))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
