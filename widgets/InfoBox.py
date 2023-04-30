from functools import partial
from PyQt6.QtWidgets import QVBoxLayout, QLabel
from widgets.ToolCheckbox import ToolCheckbox
from widgets.NumberSelector import NumberSelector


class InfoBox(QVBoxLayout):

    def __init__(self, coin, scraper, graph):
        super().__init__()
        self.layout = QVBoxLayout()

        self.layout.addStretch()
        currency_name = QLabel()
        currency_name.setText(coin.get_name() + " (" + coin.get_symbol() + ")")
        currency_name.setStyleSheet(
            "color: #f5f5f5;"
            "font-size: 24px;"
            "font-weight: bold;"
            "border-bottom: 1px solid #f5f5f5;"
        )
        self.layout.addWidget(currency_name)

        price = str(scraper.fetch_live_price())

        currency_price = QLabel()
        currency_price.setText("Live price: " + price + " €")
        currency_price.setStyleSheet(
            "color: #39FF14;"
            "font-size: 20px;"
        )
        self.layout.addWidget(currency_price)

        currency_desc_title = QLabel()
        currency_desc_title.setText("Description")
        currency_desc_title.setStyleSheet(
            "color: #f5f5f5;"
            "font-size: 20px;"
            "font-weight: bold;"
            "border-bottom: 1px solid #f5f5f5;"
        )
        self.layout.addWidget(currency_desc_title)

        currency_desc = QLabel()
        currency_desc.setText(coin.get_description())
        currency_desc.setStyleSheet(
            "color: #f5f5f5;"
            "font-size: 12px;"
        )
        currency_desc.setFixedWidth(250)
        currency_desc.setWordWrap(True)
        self.layout.addWidget(currency_desc)

        # Toolbox layout
        content_title = QLabel()
        content_title.setText("Toolbox")
        content_title.setStyleSheet(
            "color: #f5f5f5;"
            "font-size: 24px;"
            "font-weight: bold;"
            "border-bottom: 1px solid #f5f5f5;"
            "margin-top: 25px;"
        )

        self.layout.addWidget(content_title)

        func_title = QLabel()
        func_title.setText("Function period (days)")
        func_title.setStyleSheet(
            "color: #f5f5f5;"
            "font-size: 18px;"
            "font-weight: bold;"
            "border-bottom: 1px solid #f5f5f5;"
            "margin-top: 15px;"
        )

        self.layout.addWidget(func_title)

        period_selector = NumberSelector(default=30).get_instance()
        self.layout.addWidget(period_selector)

        func2_title = QLabel()
        func2_title.setText("Function window size (days)")
        func2_title.setStyleSheet(
            "color: #f5f5f5;"
            "font-size: 18px;"
            "font-weight: bold;"
            "border-bottom: 1px solid #f5f5f5;"
            "margin-top: 15px;"
        )

        self.layout.addWidget(func2_title)

        window_selector = NumberSelector(minimum=3, maximum=45).get_instance()
        self.layout.addWidget(window_selector)

        sma_box = ToolCheckbox("Simple Moving Average").get_checkbox_instance()
        sma_box.stateChanged.connect(lambda: graph.show_sma_plot(period_selector.value()))
        self.layout.addWidget(sma_box)

        resistance_box = ToolCheckbox("Resistance lines").get_checkbox_instance()
        resistance_box.stateChanged.connect(lambda: graph.show_resistance_plot(period_selector.value()))
        self.layout.addWidget(resistance_box)

        trend_box = ToolCheckbox("Trendline").get_checkbox_instance()
        trend_box.stateChanged.connect(lambda: graph.show_trendline_plot(period_selector.value()))
        self.layout.addWidget(trend_box)

        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addStretch()

    def get_layout_object(self):
        return self.layout


