from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class DetailPage(QWidget):

    def __init__(self, order):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"标题: {order[1]}"))
        layout.addWidget(QLabel(f"内容: {order[2]}"))
        layout.addWidget(QLabel(f"提交人: {order[3]}"))
        layout.addWidget(QLabel(f"状态: {order[4]}"))
        layout.addWidget(QLabel(f"创建时间: {order[6]}"))

        update_time = order[7] if len(order) > 7 else "未更新"
        finish_time = order[8] if len(order) > 8 else "未完成"

        layout.addWidget(QLabel(f"更新时间: {update_time}"))
        layout.addWidget(QLabel(f"完成时间: {finish_time}"))

        self.setLayout(layout)