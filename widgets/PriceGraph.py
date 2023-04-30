from pyqtgraph import PlotWidget
import pyqtgraph as pg
import numpy as np


class PriceGraph(PlotWidget):

    def __init__(self, dataset):
        super(PlotWidget, self).__init__()

        self.is_trendline_shown = False
        self.is_resistance_lines_shown = False
        self.is_moving_average_shown = False

        self.trendline_plot = None
        self.sma_plot = None
        self.resistance_high_plot = None
        self.resistance_low_plot = None

        self.price_graph = pg.PlotWidget()
        self.price_graph.setBackground('#000000')
        self.prices_close = dataset.iloc[6].iloc[::-1]
        self.dates = dict(enumerate((list(dataset)[::-1])))
        y_val = list(self.dates.keys())[0:-2]
        pen = pg.mkPen(color="#39FF14", width=3.0)
        self.price_graph.plot(y_val, np.array(self.prices_close[0:-2], dtype=float),
                              pen=pen)
        self.price_graph.getPlotItem().getAxis('bottom') \
            .setTicks([list(self.dates.items())[::5], list(self.dates.items())])
        self.price_graph.setXRange(len(self.prices_close) - 30, len(self.prices_close))
        self.price_graph.setYRange(min(self.prices_close[-32:-2]), max(self.prices_close[-32:-2]))

    def get_main_graph(self):
        return self.price_graph

    def get_prices_in_period(self, period):
        return self.prices_close[len(self.prices_close) - period:-2]

    def get_dataset_size(self):
        return len(self.prices_close[0:-2])

    def show_trendline_plot(self, period):
        if self.is_trendline_shown:
            self.price_graph.removeItem(self.trendline_plot)
        else:
            _prices = self.get_prices_in_period(period)
            _prices = np.array(_prices[0:], dtype=float)
            trend_line = np.polyfit(np.arange(self.get_dataset_size() - len(_prices),
                                              self.get_dataset_size()), _prices, 1)
            x = np.arange(self.get_dataset_size() - period, self.get_dataset_size())
            y = np.polyval(trend_line, x)
            pen = pg.mkPen(color="#FF3131", width=2.0)
            self.trendline_plot = self.price_graph.plot(x, y, pen=pen)
        self.is_trendline_shown = not self.is_trendline_shown

    def show_sma_plot(self, period, window_size=10):
        if self.is_moving_average_shown:
            self.price_graph.removeItem(self.sma_plot)
        else:
            _prices = self.get_prices_in_period(period)
            sma = []
            i = 0
            while i < len(_prices) - window_size + 1:
                window = _prices[i: i + window_size]
                window_avg = round(sum(window) / window_size, 2)
                sma.append(window_avg)
                i += 1
            pen = pg.mkPen(color="#9D00FF", width=2.0)
            self.sma_plot = self.price_graph.plot(np.arange(self.get_dataset_size() - len(sma),
                                                            self.get_dataset_size()),
                                                  sma, pen=pen)
        self.is_moving_average_shown = not self.is_moving_average_shown

    def show_resistance_plot(self, period):
        if self.is_resistance_lines_shown:
            self.price_graph.removeItem(self.resistance_high_plot)
            self.price_graph.removeItem(self.resistance_low_plot)
        else:
            _prices = self.get_prices_in_period(period)
            price_high = np.full(shape=30, fill_value=_prices.max())
            price_low = np.full(shape=30, fill_value=_prices.min())
            pen = pg.mkPen(color="#F5F5F5", width=2.0)
            self.resistance_high_plot = self.price_graph.plot(np.arange(self.get_dataset_size() - period,
                                                                        self.get_dataset_size()),
                                                              price_high, pen=pen)
            self.resistance_low_plot = self.price_graph.plot(np.arange(self.get_dataset_size() - period,
                                                                       self.get_dataset_size()),
                                                             price_low, pen=pen)
        self.is_resistance_lines_shown = not self.is_resistance_lines_shown
