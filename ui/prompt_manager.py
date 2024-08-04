from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QScrollArea,
                             QLabel, QFrame, QHBoxLayout, QSizePolicy)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize
from PyQt6.QtGui import QFont, QColor
from .prompt_card import PromptCard
from .prompt_dialog import PromptDialog
from data.database import db
from ui.animated_button import AnimatedButton

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
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Header
        header_label = QLabel("Prompts")
        header_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        main_layout.addWidget(header_label)

        # Content widget (scroll area + button)
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(20)

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
        content_layout.addWidget(scroll_area, 1)  # Set stretch factor to 1

        # Add new card button
        self.add_button = AnimatedButton("Add new prompt", "fa5s.plus")
        self.add_button.setFixedHeight(50)
        self.add_button.clicked.connect(self.add_prompt)
        content_layout.addWidget(self.add_button)

        main_layout.addWidget(content_widget, 1)  # Add content widget with stretch

        self.setStyleSheet("""
            QWidget {
                background-color: #282c34;
            }
            QLabel {
                color: #abb2bf;
            }
        """)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.load_prompts()
        