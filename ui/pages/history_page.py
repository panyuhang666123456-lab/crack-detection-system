from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel
import datetime


class HistoryPage(QWidget):

    def __init__(self):
        super().__init__()

        self.records = []

        self.init_ui()

    def init_ui(self):

        layout = QVBoxLayout()

        self.title = QLabel("📊 检测历史记录")

        self.list_widget = QListWidget()

        layout.addWidget(self.title)
        layout.addWidget(self.list_widget)

        self.setLayout(layout)

    def add_record(self, result):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.records.append((time, result))

        self.list_widget.addItem(f"{time} - {result}")