from PyQt6.QtCore import Qt, pyqtSignal, QSize
from PyQt6.QtGui import QColor, QIcon
from PyQt6.QtWidgets import QGraphicsDropShadowEffect, QFrame, QLabel, QVBoxLayout, QPushButton, QHBoxLayout

class PromptCard(QFrame):
    edit_requested = pyqtSignal(str)
    deleted = pyqtSignal(str)

    def __init__(self, prompt_id, tag, content):
        super().__init__()
        self.prompt_id = prompt_id
        self.tag = tag
        self.content = content
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        tag_label = QLabel(self.tag)
        tag_label.setStyleSheet("""
            background-color: #61afef;
            color: #282c34;
            padding: 5px 10px;
            border-radius: 10px;
            font-weight: bold;
            font-size: 14px;
        """)
        tag_label.setFixedHeight(30)
        tag_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(tag_label, alignment=Qt.AlignmentFlag.AlignLeft)

        content_preview = self.content[:100] + "..." if len(self.content) > 100 else self.content
        content_label = QLabel(content_preview)
        content_label.setStyleSheet("""
            color: #abb2bf;
            font-size: 16px;
            padding: 10px;
            background-color: #3a3f4b;
            border-radius: 8px;
        """)
        content_label.setWordWrap(True)
        layout.addWidget(content_label)

        button_layout = QHBoxLayout()
        edit_button = QPushButton(QIcon("icons/edit.png"), "Edit")
        delete_button = QPushButton(QIcon("icons/delete.png"), "Delete")
        for button in (edit_button, delete_button):
            button.setStyleSheet("""
                QPushButton {
                    background-color: #3a3f4b;
                    color: #abb2bf;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #4a4f5b;
                }
            """)
            button.setIconSize(QSize(20, 20))
        edit_button.clicked.connect(lambda: self.edit_requested.emit(self.prompt_id))
        delete_button.clicked.connect(lambda: self.deleted.emit(self.prompt_id))
        button_layout.addWidget(edit_button)
        button_layout.addWidget(delete_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)

        self.setStyleSheet("""
            PromptCard {
                background-color: #2c313c;
                border-radius: 10px;
                border: 1px solid #3a3f4b;
            }
        """)
        # Add shadow effect
        self.setGraphicsEffect(self.create_shadow())

    def create_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(5)
        shadow.setColor(QColor(0, 0, 0, 80))
        return shadow
