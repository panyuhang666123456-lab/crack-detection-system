from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()

        # 🔥 登录成功回调（由 main.py 赋值）
        self.login_success_callback = None

        self.init_ui()

    def init_ui(self):

        # ================= 窗口设置 =================
        self.setWindowTitle("建筑表面裂纹智能巡检系统")
        self.resize(420, 320)

        # ================= 标题 =================
        title = QLabel("建筑表面裂纹智能巡检系统")
        title.setAlignment(Qt.AlignCenter)

        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        title.setFont(font)

        # ================= 用户名 =================
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("请输入用户名")

        # ================= 密码 =================
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("请输入密码")
        self.password_input.setEchoMode(QLineEdit.Password)

        # ================= 登录按钮 =================
        self.login_button = QPushButton("登录系统")
        self.login_button.clicked.connect(self.login)

        # ================= 布局 =================
        layout = QVBoxLayout()

        layout.addStretch()
        layout.addWidget(title)
        layout.addSpacing(25)

        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)

        layout.addSpacing(20)
        layout.addWidget(self.login_button)
        layout.addStretch()

        self.setLayout(layout)

        # ================= UI样式 =================
        self.setStyleSheet("""
            QWidget {
                background-color: #f2f2f2;
            }

            QLineEdit {
                height: 36px;
                padding-left: 10px;
                border: 1px solid #cccccc;
                border-radius: 5px;
                background: white;
                font-size: 14px;
            }

            QPushButton {
                height: 38px;
                background-color: #0078d7;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #005fa3;
            }
        """)

    # ================= 登录逻辑 =================
    def login(self):

        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        # 测试账号
        if username == "admin" and password == "123456":

            QMessageBox.information(self, "登录成功", "欢迎进入系统！")

            # 🚀 关键：通知主窗口
            if self.login_success_callback:
                self.login_success_callback()

        else:
            QMessageBox.warning(self, "登录失败", "用户名或密码错误")