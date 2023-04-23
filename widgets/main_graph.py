
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
        pen = pg.mkPen(color="#39FF14", width=3.0)
        price_plot = pg.PlotDataItem(np.arange(1, 16), np.array(self.prices_close[0:15], dtype=float), pen=pen)
        self.price_graph.addItem(price_plot)
        self.price_graph.getPlotItem().hideAxis('left')

