import sys
from PySide6.QtWidgets import QApplication

from db.database import init_db
from ui.login.login_window import LoginWindow
from ui.main_window.main_window import MainWindow


def main():

    # ✅ 初始化数据库（关键）
    init_db()

    app = QApplication(sys.argv)

    login = LoginWindow()
    window = MainWindow()

    def on_login_success():
        login.close()
        window.show()

    login.login_success_callback = on_login_success

    login.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()