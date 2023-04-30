from PyQt6.QtWidgets import QVBoxLayout, QLabel, QCheckBox


class ToolCheckbox:

    def __init__(self, title):
        self.layout = QCheckBox(text=title)
        self.layout.setStyleSheet(
            "background: #222222;"
            "color: #f5f5f5;"
            "font-size: 16px;"
        )

    def get_checkbox_instance(self):
        return self.layout
