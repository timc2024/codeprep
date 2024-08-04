from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QComboBox, QFileDialog,
                             QMessageBox, QTextEdit, QStyle)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from src.gui.file_list_widget import FileListWidget
from src.gui.rule_preview_widget import RulePreviewWidget
from src.gui.styling import apply_stylesheet
from src.core.file_processor import FileProcessor
from src.core.masking_rules import MaskingRules
from src.utils.path_utils import get_common_path, get_relative_path

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_processor = FileProcessor()
        self.masking_rules = MaskingRules()
        self.init_ui()
        self.on_language_change("Python")  # Set default language to Python

    def init_ui(self):
        self.setWindowTitle("CodePrep")
        self.setGeometry(100, 100, 1000, 800)  # Increased window size to accommodate larger fonts

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Header
        header_label = QLabel("CodePrep")
        header_label.setStyleSheet("font-size: 32px; font-weight: bold; margin-bottom: 15px;")
        layout.addWidget(header_label, alignment=Qt.AlignCenter)

        # Language selection
        lang_layout = QHBoxLayout()
        lang_label = QLabel("Select Language:")
        lang_label.setStyleSheet("font-size: 18px;")
        lang_layout.addWidget(lang_label)
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["Python", "Android", "React", "Flutter"])
        self.lang_combo.currentTextChanged.connect(self.on_language_change)
        lang_layout.addWidget(self.lang_combo)
        layout.addLayout(lang_layout)

        # File list
        file_list_layout = QHBoxLayout()
        file_list_icon = QLabel()
        file_list_icon.setPixmap(
            self.style().standardIcon(QStyle.SP_FileDialogNewFolder).pixmap(32, 32))  # Increased icon size
        file_list_layout.addWidget(file_list_icon)
        file_list_label = QLabel("Drag and drop files or folders:")
        file_list_label.setStyleSheet("font-size: 18px;")
        file_list_layout.addWidget(file_list_label)
        layout.addLayout(file_list_layout)

        self.file_list = FileListWidget()
        layout.addWidget(self.file_list)

        # Rule preview
        rule_preview_layout = QHBoxLayout()
        rule_preview_icon = QLabel()
        rule_preview_icon.setPixmap(
            self.style().standardIcon(QStyle.SP_FileDialogDetailedView).pixmap(32, 32))  # Increased icon size
        rule_preview_layout.addWidget(rule_preview_icon)
        rule_preview_label = QLabel("Drag and drop masking rules file here:")
        rule_preview_label.setStyleSheet("font-size: 18px;")
        rule_preview_layout.addWidget(rule_preview_label)
        layout.addLayout(rule_preview_layout)

        self.rule_preview = RulePreviewWidget(self.masking_rules)
        layout.addWidget(self.rule_preview)

        # Generate button
        generate_button = QPushButton("Prepare Code for Claude")
        generate_button.setIcon(self.style().standardIcon(QStyle.SP_ArrowRight))
        generate_button.clicked.connect(self.generate_code)
        generate_button.setStyleSheet("font-size: 18px; padding: 12px;")
        layout.addWidget(generate_button)

        # Status Bar
        self.statusBar().showMessage("Ready")
        self.statusBar().setStyleSheet("font-size: 14px; padding: 5px;")

        # Apply stylesheet
        apply_stylesheet(self)

    def on_language_change(self, language):
        logging.info(f"Language changed to: {language}")
        self.file_processor.set_language_handler(language)
        self.file_list.set_language(language)

    def generate_code(self):
        if self.file_list.count() == 0:
            QMessageBox.warning(self, "Error", "No files selected.")
            return

        output_folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if not output_folder:
            return

        try:
            files = [self.file_list.item(i).text() for i in range(self.file_list.count())]
            common_path = get_common_path(files)
            relative_files = [get_relative_path(file, common_path) for file in files]

            output_files = self.file_processor.process_files(files, relative_files, output_folder, self.masking_rules)

            if output_files:
                success_message = "Files generated successfully:\n" + "\n".join(output_files)
                QMessageBox.information(self, "Success", success_message)
                logging.info(f"Generated files: {output_files}")
            else:
                QMessageBox.warning(self, "Warning",
                                    "No files were generated. This may be due to an unexpected error or mismatched file types.")
                logging.warning("No files were generated")
        except Exception as e:
            error_message = f"Failed to generate files: {str(e)}"
            QMessageBox.critical(self, "Error", error_message)
            logging.error(error_message)