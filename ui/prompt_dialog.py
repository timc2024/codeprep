from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, QTextEdit,
                             QDialogButtonBox, QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class PromptDialog(QDialog):
    def __init__(self, tag="", content=""):
        super().__init__()
        self.setWindowTitle("Add/Edit Prompt")
        self.tag = tag
        self.content = content
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Tag input
        tag_label = QLabel("Tag:")
        tag_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.tag_input = QLineEdit(self.tag)
        self.tag_input.setPlaceholderText("Enter tag")
        self.tag_input.setFont(QFont("Arial", 14))
        layout.addWidget(tag_label)
        layout.addWidget(self.tag_input)

        # Content input
        content_label = QLabel("Content:")
        content_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.content_input = QTextEdit(self.content)
        self.content_input.setPlaceholderText("Enter content")
        self.content_input.setFont(QFont("Arial", 14))
        layout.addWidget(content_label)
        layout.addWidget(self.content_input)

        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setStyleSheet("""
            QDialog {
                background-color: #282c34;
                color: #abb2bf;
            }
            QLabel {
                color: #e5c07b;
            }
            QLineEdit, QTextEdit {
                background-color: #3a3f4b;
                color: #abb2bf;
                border: 1px solid #5c6370;
                border-radius: 4px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton {background-color: #61afef;
                color: #282c34;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #56b6c2;
            }
        """)

    def get_prompt(self):
        return self.tag_input.text(), self.content_input.toPlainText()