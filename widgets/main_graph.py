from PyQt6 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import pandas as pd
import numpy as np


class PriceGraph(PlotWidget):

    def __init__(self, dataset):
        super(PlotWidget, self).__init__()

        self.price_graph = pg.PlotWidget()
        self.price_graph.setBackground('#000000')
        self.prices_close = dataset.iloc[6].iloc[::-1]
        self.dates = dict(enumerate((list(dataset)[::-1])))
        y_val = list(self.dates.keys())[0:-2]
        pen = pg.mkPen(color="#39FF14", width=3.0)
        self.price_graph.plot(y_val, np.array(self.prices_close[0:-2], dtype=float),
                              pen=pen)
        self.price_graph.getPlotItem().hideAxis('left')
        self.price_graph.getPlotItem().getAxis('bottom')\
            .setTicks([list(self.dates.items())[::5], list(self.dates.items())])
        self.price_graph.setXRange(len(self.prices_close) - 30, len(self.prices_close))
        self.price_graph.setYRange(min(self.prices_close[-32:-2]), max(self.prices_close[-32:-2]))
