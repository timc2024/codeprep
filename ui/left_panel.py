import os

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QLabel, QComboBox, QListWidget, QTextEdit, QFrame)
from PyQt6.QtCore import pyqtSignal, Qt, QPropertyAnimation, QEasingCurve, QSize
from PyQt6.QtGui import QFont, QColor, QIcon
from core.file_processor import FileProcessor
from core.masking_rules import MaskingRules
from config import SUPPORTED_LANGUAGES, OUTPUT_FOLDER
from ui.file_list_widget import FileListWidget
from ui.rule_preview_widget import RulePreviewWidget


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
            self.setIconSize(QSize(24,24))
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

class LeftPanel(QWidget):
    language_changed = pyqtSignal(str)
    generate_clicked = pyqtSignal(list, list, str, MaskingRules)

    def __init__(self):
        super().__init__()
        self.file_processor = FileProcessor()
        self.masking_rules = MaskingRules()
        self.init_ui()

    def on_language_changed(self, language):
        self.file_processor.set_language_handler(language)
        self.language_changed.emit(language)
        self.file_list.clear()

    def on_generate_clicked(self):
        files = [self.file_list.item(i).text() for i in range(self.file_list.count())]
        if not files:
            return
        common_path = os.path.commonpath(files)
        relative_files = [os.path.relpath(f, common_path) for f in files]
        self.generate_clicked.emit(files, relative_files, OUTPUT_FOLDER, self.masking_rules)
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Language selection
        lang_layout = QHBoxLayout()
        lang_label = QLabel("Language:")
        lang_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(SUPPORTED_LANGUAGES)
        self.lang_combo.setFixedHeight(40)
        self.lang_combo.setFont(QFont("Arial", 14))
        self.lang_combo.currentTextChanged.connect(self.on_language_changed)
        lang_layout.addWidget(lang_label)
        lang_layout.addWidget(self.lang_combo)
        layout.addLayout(lang_layout)

        # File list
        file_list_label = QLabel("Files:")
        file_list_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        layout.addWidget(file_list_label)

        self.file_list = FileListWidget()
        self.file_list.setFixedHeight(200)
        self.file_list.setFont(QFont("Arial", 14))
        layout.addWidget(self.file_list)

        # Masking rules
        rules_label = QLabel("Masking Rules:")
        rules_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        layout.addWidget(rules_label)

        self.rule_preview = RulePreviewWidget(self.masking_rules)  # Use RulePreviewWidget instead of QTextEdit
        layout.addWidget(self.rule_preview)

        layout.addStretch()

        # Generate button
        self.generate_button = AnimatedButton("Prepare Code for Claude", "icons/generate.png")
        self.generate_button.setFixedHeight(50)
        self.generate_button.clicked.connect(self.on_generate_clicked)
        layout.addWidget(self.generate_button)


        self.setStyleSheet("""
            QWidget {
                background-color: #282c34;
            }
            QLabel {
                color: #abb2bf;
            }
            QComboBox, QListWidget, QTextEdit {
                background-color: #2c313c;
                color: #abb2bf;
                border-radius: 10px;
                border: 1px solid #3a3f4b;
                padding: 10px;
            }
            QComboBox::drop-down {
                border: none;
                padding: 10px;
            }
            QComboBox::down-arrow {
                image: url(icons/dropdown.png);
                width: 14px;
                height: 14px;
            }
            QComboBox QAbstractItemView {
                background-color: #2c313c;
                color: #abb2bf;
                border: 1px solid #3a3f4b;
                border-radius: 10px;
                padding: 10px;
                selection-background-color: #61afef;
                selection-color: #282c34;
            }
            QComboBox QAbstractItemView::item {
                min-height: 40px;
            }
        """)


