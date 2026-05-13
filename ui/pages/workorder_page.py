from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QLineEdit,
    QTextEdit, QLabel, QComboBox, QMessageBox
)
from PySide6.QtCore import QDateTime
from db.database import (
    insert_order,
    fetch_orders,
    update_status,
    update_image
)
from ui.pages.detail_page import DetailPage
from db.database import delete_order

class WorkOrderPage(QWidget):

    def __init__(self):
        super().__init__()

        # ================= 数据结构 =================
        self.workorders = []

        self.init_ui()

    def init_ui(self):

        self.title = QLabel("工单管理系统")

        # ================= 输入区域 =================
        self.input_title = QLineEdit()
        self.input_title.setPlaceholderText("工单标题")

        self.input_content = QTextEdit()
        self.input_content.setPlaceholderText("工作内容 / 描述")

        self.input_user = QLineEdit()
        self.input_user.setPlaceholderText("提交人")

        self.btn_create = QPushButton("创建工单")
        self.btn_create.clicked.connect(self.create_order)

        # ================= 状态操作 =================
        self.status_box = QComboBox()
        self.status_box.addItems(["待处理", "处理中", "已完成"])

        self.btn_update = QPushButton("更新状态")
        self.btn_update.clicked.connect(self.update_status)

        # ================= 列表 =================
        self.todo_list = QListWidget()
        self.doing_list = QListWidget()
        self.done_list = QListWidget()

        # ================= 布局 =================
        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.input_title)
        layout.addWidget(self.input_content)
        layout.addWidget(self.input_user)
        layout.addWidget(self.btn_create)

        layout.addWidget(QLabel("状态修改"))
        layout.addWidget(self.status_box)
        layout.addWidget(self.btn_update)

        

        # ====== 三个列容器 ======

        todo_label = QLabel("待处理")
        todo_label.setStyleSheet("color:black;font-size:16px;font-weight:bold;")

        todo_layout = QVBoxLayout()
        todo_layout.addWidget(todo_label)
        todo_layout.addWidget(self.todo_list)
        todo_layout.addStretch()

        doing_label = QLabel("处理中")
        doing_label.setStyleSheet("color:black;font-size:16px;font-weight:bold;")

        doing_layout = QVBoxLayout()
        doing_layout.addWidget(doing_label)
        doing_layout.addWidget(self.doing_list)
        doing_layout.addStretch()

        done_label = QLabel("已完成")
        done_label.setStyleSheet("color:black;font-size:16px;font-weight:bold;")

        done_layout = QVBoxLayout()
        done_layout.addWidget(done_label)
        done_layout.addWidget(self.done_list)
        done_layout.addStretch()

        # ====== 横向看板 ======

        board_layout = QHBoxLayout()
        board_layout.setSpacing(40)
        board_layout.setContentsMargins(10, 10, 10, 10)
        board_layout.addLayout(todo_layout)
        board_layout.addLayout(doing_layout)
        board_layout.addLayout(done_layout)

        layout.addLayout(board_layout)

        self.setLayout(layout)

        # ================= 样式 =================
        self.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: bold;
            }

            QLineEdit, QTextEdit, QComboBox {
                padding: 6px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }

            QPushButton {
                height: 35px;
                background-color: #0078d7;
                color: white;
                border: none;
                border-radius: 4px;
            }

            QPushButton:hover {
                background-color: #005fa3;
            }
        """)
        self.todo_list.itemDoubleClicked.connect(self.open_detail)
        self.doing_list.itemDoubleClicked.connect(self.open_detail)
        self.done_list.itemDoubleClicked.connect(self.open_detail)
        self.btn_delete = QPushButton("删除工单")
        self.btn_delete.clicked.connect(self.delete_order)
        layout.addWidget(self.btn_delete)

    # ================= 创建工单 =================
    def create_order(self):

        title = self.input_title.text().strip()
        content = self.input_content.toPlainText().strip()
        user = self.input_user.text().strip()

        if not title:
            return

        insert_order(title, content, user)

        self.refresh_board()

        self.input_title.clear()
        self.input_content.clear()
        self.input_user.clear()
        
    # ================= 更新状态 =================
    def update_status(self):

        item = (
            self.todo_list.currentItem()
            or self.doing_list.currentItem()
            or self.done_list.currentItem()
        )

        if not item:
            return

        order_id = int(item.text().split("]")[0][1:])

        new_status = self.status_box.currentText()

        update_status(order_id, new_status)

        self.refresh_board()

    # ================= 刷新列表 =================
    def refresh_board(self):

        self.todo_list.clear()
        self.doing_list.clear()
        self.done_list.clear()

        orders = fetch_orders()

        self.workorders = orders

        for w in orders:

            text = f"[{w[0]}] {w[1]}"

            if w[4] == "待处理":
                self.todo_list.addItem(text)

            elif w[4] == "处理中":
                self.doing_list.addItem(text)

            elif w[4] == "已完成":
                self.done_list.addItem(text)

            
    def open_detail(self, item):

        text = item.text()
        order_id = int(text.split("]")[0][1:])

        order = None
        for w in self.workorders:
            if w[0] == order_id:
                order = w
                break

        if order:
            self.detail = DetailPage(order)
            self.detail.show()
    

    def delete_order(self):

        item = self.todo_list.currentItem() or \
               self.doing_list.currentItem() or \
               self.done_list.currentItem()

        if not item:
            return

        order_id = int(item.text().split("]")[0][1:])

        delete_order(order_id)
        self.workorders = fetch_orders()
        self.refresh_board()