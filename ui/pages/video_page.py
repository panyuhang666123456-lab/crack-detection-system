import os
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QFileDialog
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QImage


class VideoPage(QWidget):

    def __init__(self):
        super().__init__()

        self.current_frame = None  # 当前帧（预留）
        self.init_ui()

        # 模拟视频刷新（后面换成摄像头）
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000)  # 1秒刷新一次（模拟）

    def init_ui(self):

        # ================= 视频显示区 =================
        self.video_label = QLabel("视频画面区域（预留摄像头）")
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setFixedHeight(400)
        self.video_label.setStyleSheet("""
            background-color: black;
            color: white;
            font-size: 16px;
        """)

        # ================= 按钮 =================
        self.btn_snapshot = QPushButton("📸 截图")
        self.btn_save = QPushButton("💾 保存图片")
        self.btn_ai = QPushButton("🧠 AI检测（预留）")

        self.btn_snapshot.clicked.connect(self.snapshot)
        self.btn_save.clicked.connect(self.save_image)
        self.btn_ai.clicked.connect(self.ai_detect)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_snapshot)
        btn_layout.addWidget(self.btn_save)
        btn_layout.addWidget(self.btn_ai)

        # ================= 主布局 =================
        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        self.setStyleSheet("""
            QPushButton {
                height: 40px;
                background-color: #0078d7;
                color: white;
                border: none;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #005fa3;
            }
        """)

    # ================= 模拟视频帧 =================
    def update_frame(self):
        """
        这里以后换成摄像头 / RTSP / 小车视频流
        """
        self.video_label.setText("📡 正在接收视频流（模拟）")

    # ================= 截图功能 =================
    def snapshot(self):
        pixmap = self.video_label.grab()
        self.current_frame = pixmap
        self.video_label.setText("📸 已截图成功")

    # ================= 保存图片 =================
    def save_image(self):

        if self.current_frame is None:
            self.video_label.setText("⚠️ 没有截图")
            return

        path, _ = QFileDialog.getSaveFileName(
            self,
            "保存图片",
            "",
            "PNG Files (*.png)"
        )

        if path:
            self.current_frame.save(path)
            self.video_label.setText("💾 图片已保存")

    # ================= AI接口预留 =================
    def ai_detect(self):
        """
        后面这里接：
        - YOLO
        - Crack Detection Model
        - GPU推理
        """
        self.video_label.setText("🧠 AI检测接口（未接入模型）")

    # ================= 设备通信预留 =================
    def send_to_robot(self, data):
        """
        预留接口：
        - WiFi
        - TCP
        - MQTT
        """
        pass