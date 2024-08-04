from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QFrame, QSplitter, QPushButton)
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QFont, QIcon
from .left_panel import LeftPanel
from .prompt_manager import PromptManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(None, Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("CodePrep 2024")
        self.setGeometry(100, 100, 1400, 900)
        self.init_ui()
        self.draggable = False
        self.offset = QPoint()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Custom title bar
        title_bar = QFrame()
        title_bar.setStyleSheet("background-color: #1e2127; color: white;")
        title_bar.setFixedHeight(40)
        title_layout = QHBoxLayout(title_bar)
        title_layout.setContentsMargins(10, 0, 10, 0)
        title_label = QLabel("CodePrep 2024")
        title_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        title_layout.addWidget(title_label)
        title_layout.addStretch()

        for icon_name, slot in [("minimize", self.showMinimized),
                                ("maximize", self.toggle_maximize),
                                ("close", self.close)]:
            button = QPushButton(QIcon(f"icons/{icon_name}.png"), "")
            button.setFixedSize(30, 30)
            button.clicked.connect(slot)
            button.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                }
                QPushButton:hover {
                    background-color: #4a4f5b;
                }
            """)
            title_layout.addWidget(button)

        main_layout.addWidget(title_bar)

        # Main content area
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        self.left_panel = LeftPanel()
        self.right_panel = PromptManager()

        # Create wrapper widgets for left and right panels
        left_wrapper = QWidget()
        left_layout = QVBoxLayout(left_wrapper)
        left_layout.setContentsMargins(0, 0, 10, 0)  # Add right margin
        left_layout.addWidget(self.left_panel)

        right_wrapper = QWidget()
        right_layout = QVBoxLayout(right_wrapper)
        right_layout.setContentsMargins(10, 0, 0, 0)  # Add left margin
        right_layout.addWidget(self.right_panel)

        splitter.addWidget(left_wrapper)
        splitter.addWidget(right_wrapper)
        splitter.setSizes([int(self.width() * 0.6), int(self.width() * 0.4)])
        splitter.setHandleWidth(1)
        splitter.setStyleSheet("""
            QSplitter::handle {
                background-color: #3a3f4b;
            }
        """)

        content_layout.addWidget(splitter)
        main_layout.addWidget(content_widget)

        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #282c34;
                color: #abb2bf;
                font-size: 16px;
            }
            QFrame {
                border: none;
            }
        """)

    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and event.y() < 40:
            self.draggable = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.draggable and event.buttons() & Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.draggable = False