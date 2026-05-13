from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel


class ReportPage(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        layout = QVBoxLayout()

        self.title = QLabel("📄 报告生成系统")

        self.btn_export = QPushButton("导出报告（预留PDF）")

        layout.addWidget(self.title)
        layout.addWidget(self.btn_export)

        self.setLayout(layout)