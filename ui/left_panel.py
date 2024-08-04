import os

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QTextEdit, QFrame)
from PyQt6.QtCore import pyqtSignal, Qt, QPropertyAnimation, QEasingCurve, QSize
from PyQt6.QtGui import QFont, QColor
from core.file_processor import FileProcessor
from core.masking_rules import MaskingRules
from config import SUPPORTED_LANGUAGES, OUTPUT_FOLDER
from ui.animated_button import AnimatedButton
from ui.animated_combo_box import AnimatedComboBox
from ui.file_list_widget import FileListWidget
from ui.rule_preview_widget import RulePreviewWidget
import qtawesome as qta

class LeftPanel(QWidget):
    language_changed = pyqtSignal(str)
    generate_clicked = pyqtSignal(list, list, MaskingRules)

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
        self.generate_clicked.emit(files, relative_files, self.masking_rules)

    def load_masking_rules(self, file_path):
        self.masking_rules = MaskingRules()
        self.masking_rules.load_from_file(file_path)
        # Update UI to show that rules have been loaded

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)  # Increased spacing between sections

        # Language selection
        lang_layout = self.create_section_layout("fa5s.code", "Language:")
        self.lang_combo = AnimatedComboBox()
        self.lang_combo.addItems(SUPPORTED_LANGUAGES)
        self.lang_combo.setFixedSize(200, 40)
        self.lang_combo.setFont(QFont("Arial", 12))
        self.lang_combo.currentTextChanged.connect(self.on_language_changed)
        lang_layout.addWidget(self.lang_combo)
        layout.addLayout(lang_layout)

        # File list
        file_layout = self.create_section_layout("fa5s.file-code", "Files:")
        layout.addLayout(file_layout)

        self.file_list = FileListWidget()
        self.file_list.setFixedHeight(200)
        self.file_list.setFont(QFont("Arial", 14))
        layout.addWidget(self.file_list)

        # Masking rules
        masking_layout = self.create_section_layout("fa5s.user-secret", "Masking Rules:")
        layout.addLayout(masking_layout)

        self.rule_preview = RulePreviewWidget(self.masking_rules)
        layout.addWidget(self.rule_preview)

        layout.addStretch()

        # Generate button
        self.generate_button = AnimatedButton("Prepare Code for Claude", "fa5s.cogs")
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
            QComboBox {
                background-color: #2c313c;
                color: #abb2bf;
                border-radius: 5px;
                border: 1px solid #3a3f4b;
                padding: 5px 10px;
            }
            QComboBox::drop-down {
                border: none;
                padding-right: 10px;
            }
            QComboBox QAbstractItemView {
                background-color: #2c313c;
                color: #abb2bf;
                border: 1px solid #3a3f4b;
                selection-background-color: #61afef;
                selection-color: #282c34;
            }
        """)

    def create_section_layout(self, icon_name, label_text):
        section_layout = QHBoxLayout()
        section_layout.setSpacing(10)  # This controls horizontal spacing within the section header
        section_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        icon = QLabel()
        icon.setPixmap(qta.icon(icon_name, color='#abb2bf').pixmap(24, 24))
        section_layout.addWidget(icon)
        label = QLabel(label_text)
        label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        section_layout.addWidget(label)
        section_layout.addStretch()
        return section_layout