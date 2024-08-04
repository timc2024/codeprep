from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QScrollArea,
                             QLabel, QFrame, QHBoxLayout)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize
from PyQt6.QtGui import QFont, QColor, QIcon
from .prompt_card import PromptCard
from .prompt_dialog import PromptDialog
from data.database import db

class AnimatedButton(QPushButton):
    def __init__(self, text, icon=None):
        super().__init__(text)
        self.setStyleSheet("""
            QPushButton {
                background-color: #61afef;
                color: #282c34;
                border: none;
                padding: 12px;
                border-radius: 6px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #56b6c2;
            }
        """)
        if icon:
            self.setIcon(QIcon(icon))
            self.setIconSize(QSize(24, 24))
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setEasingCurve(QEasingCurve.Type.OutQuad)
        self.animation.setDuration(100)

    def enterEvent(self, event):
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(self.geometry().adjusted(-2, -2, 2, 2))
        self.animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(self.geometry().adjusted(2, 2, -2, -2))
        self.animation.start()
        super().leaveEvent(event)

class PromptManager(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def load_prompts(self):
        prompts = db.get_all_prompts()
        for prompt in prompts:
            self.add_prompt_card(str(prompt['_id']), prompt['tag'], prompt['content'])
    def add_prompt(self):
        dialog = PromptDialog()
        if dialog.exec():
            tag, content = dialog.get_prompt()
            prompt_id = db.add_prompt(tag, content)
            self.add_prompt_card(str(prompt_id), tag, content)

    def add_prompt_card(self, prompt_id, tag, content):
        card = PromptCard(prompt_id, tag, content)
        card.edit_requested.connect(self.edit_prompt)
        card.deleted.connect(self.delete_prompt)
        self.scroll_layout.addWidget(card)

    def edit_prompt(self, prompt_id):
        prompt = db.get_prompt(prompt_id)
        if prompt:
            dialog = PromptDialog(prompt['tag'], prompt['content'])
            if dialog.exec():
                new_tag, new_content = dialog.get_prompt()
                db.update_prompt(prompt_id, new_tag, new_content)
                self.refresh_prompts()

    def delete_prompt(self, prompt_id):
        db.delete_prompt(prompt_id)
        self.refresh_prompts()

    def refresh_prompts(self):
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.itemAt(i).widget().setParent(None)
        self.load_prompts()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Header
        header_label = QLabel("Prompts")
        header_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        layout.addWidget(header_label)

        # Scroll area for cards
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
        """)
        scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.setSpacing(15)
        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)

        layout.addStretch()

        # Add new card button
        self.add_button = AnimatedButton("+ Add new prompt", "icons/add.png")
        self.add_button.setFixedHeight(50)
        self.add_button.clicked.connect(self.add_prompt)
        layout.addWidget(self.add_button)

        self.setStyleSheet("""
            QWidget {
                background-color: #282c34;
            }
            QLabel {
                color: #abb2bf;
            }
        """)

        self.load_prompts()
