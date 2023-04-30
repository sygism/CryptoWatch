from PyQt6.QtWidgets import QVBoxLayout, QLabel


class ToolBox(QVBoxLayout):

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def get_layout_object(self):
        return self.layout


