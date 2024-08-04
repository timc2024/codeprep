import logging

from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QFrame, QSplitter, QPushButton, QMessageBox, QSizePolicy, QFileDialog)
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QFont, QIcon
from .left_panel import LeftPanel
from .prompt_manager import PromptManager
import qtawesome as qta

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CodePrep")
        self.setGeometry(100, 100, 1400, 900)
        self.init_ui()

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
        title_label = QLabel("CodePrep")
        title_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        title_layout.addWidget(title_label)
        title_layout.addStretch()

        main_layout.addWidget(title_bar)

        # Main content area
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        self.left_panel = LeftPanel()
        self.left_panel.generate_clicked.connect(self.generate_code)  # Connect the signal
        self.left_panel.language_changed.connect(self.left_panel.file_list.set_language)
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
        right_wrapper.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
     
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

    def generate_code(self, files, relative_files, masking_rules):
        output_folder = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if not output_folder:
            return

        try:
            output_files = self.left_panel.file_processor.process_files(files, relative_files, output_folder,
                                                                        masking_rules)

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