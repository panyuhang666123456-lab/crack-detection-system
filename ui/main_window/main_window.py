from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget
)

from PySide6.QtCore import Qt
from ui.pages.video_page import VideoPage
from ui.pages.workorder_page import WorkOrderPage
from ui.pages.history_page import HistoryPage
from ui.pages.report_page import ReportPage

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("裂纹智能巡检系统 - 控制台")
        self.resize(1000, 600)

        # ================= 主容器 =================
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # ================= 左侧菜单 =================
        self.menu_widget = QWidget()
        self.menu_layout = QVBoxLayout()
        self.menu_widget.setLayout(self.menu_layout)

        self.menu_widget.setFixedWidth(180)

        # 菜单按钮
        self.btn_video = QPushButton("实时视频巡检")
        self.btn_image = QPushButton("图像检测")
        self.btn_robot = QPushButton("小车控制")
        self.btn_workorder = QPushButton("工单管理")
        self.btn_history = QPushButton("历史查询")
        self.btn_report = QPushButton("报告生成")

        self.menu_layout.addWidget(self.btn_video)
        self.menu_layout.addWidget(self.btn_image)
        self.menu_layout.addWidget(self.btn_robot)
        self.menu_layout.addWidget(self.btn_workorder)
        self.menu_layout.addWidget(self.btn_history)
        self.menu_layout.addWidget(self.btn_report)

        self.menu_layout.addStretch()

        self.stack = QStackedWidget()

        # ================= 页面 =================
        self.video_page = VideoPage()
        self.image_page = QLabel("🖼 图像检测页面")
        self.image_page.setAlignment(Qt.AlignCenter)

        self.robot_page = QLabel("🚗 小车控制页面")
        self.robot_page.setAlignment(Qt.AlignCenter)

        self.workorder_page = WorkOrderPage()
        self.history_page = HistoryPage()
        self.report_page = ReportPage()

        # ================= 加入堆栈（顺序很重要） =================
        self.stack.addWidget(self.video_page)      # 0
        self.stack.addWidget(self.image_page)      # 1
        self.stack.addWidget(self.robot_page)     # 2
        self.stack.addWidget(self.workorder_page) # 3
        self.stack.addWidget(self.history_page)   # 4
        self.stack.addWidget(self.report_page)    # 5

        # ================= 布局组合 =================
        main_layout.addWidget(self.menu_widget)
        main_layout.addWidget(self.stack)

        # ================= 绑定事件 =================
        self.btn_video.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.btn_image.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.btn_robot.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        self.btn_workorder.clicked.connect(lambda: self.stack.setCurrentIndex(3))
        self.btn_history.clicked.connect(lambda: self.stack.setCurrentIndex(4))
        self.btn_report.clicked.connect(lambda: self.stack.setCurrentIndex(5))
        
        # ================= 样式 =================
        self.setStyleSheet("""

QWidget {
    background-color: #f5f5f5;
}

/* ================= 左侧菜单 ================= */
QPushButton {
    height: 42px;
    text-align: left;
    padding-left: 12px;

    border: none;
    background-color: transparent;

    color: #222;   /* 默认黑色字体 */
    font-size: 14px;
}

/* 鼠标悬停 */
QPushButton:hover {
    background-color: #e6f2ff;
}

/* 选中状态（我们后面会控制） */
QPushButton:checked {
    background-color: #0078d7;
    color: white;
    font-weight: bold;
}

/* 内容区域 */
QStackedWidget {
    background-color: white;
    border-left: 1px solid #ddd;
}

""")