from PyQt6.QtWidgets import QSpinBox


class NumberSelector:

    def __init__(self, minimum=10, maximum=999, default=5):
        self.layout = QSpinBox()
        self.layout.setMinimum(minimum)
        self.layout.setMaximum(maximum)
        self.layout.setValue(default)
        self.layout.setStyleSheet(
            "background: #222222;"
            "color: #f5f5f5;"
            "font-size: 16px;"
        )

    def get_instance(self):
        return self.layout
