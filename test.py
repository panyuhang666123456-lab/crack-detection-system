from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("登录界面")
        self.resize(300, 200)

        # 用户名
        self.user_label = QLabel("用户名")
        self.user_input = QLineEdit()

        # 密码
        self.pwd_label = QLabel("密码")
        self.pwd_input = QLineEdit()
        self.pwd_input.setEchoMode(QLineEdit.Password)

        # 登录按钮
        self.login_btn = QPushButton("登录")
        self.login_btn.clicked.connect(self.check_login)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.pwd_label)
        layout.addWidget(self.pwd_input)
        layout.addWidget(self.login_btn)

        self.setLayout(layout)

    def check_login(self):
        username = self.user_input.text()
        password = self.pwd_input.text()

        # 简单验证
        if username == "admin" and password == "123456":
            QMessageBox.information(self, "成功", "登录成功！")
        else:
            QMessageBox.warning(self, "失败", "用户名或密码错误")


if __name__ == "__main__":
    app = QApplication([])

    window = LoginWindow()
    window.show()

    app.exec()