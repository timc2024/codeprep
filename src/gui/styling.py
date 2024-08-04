from PyQt5.QtWidgets import QStyleFactory
import qdarkstyle

def apply_stylesheet(widget):
    widget.setStyle(QStyleFactory.create('Fusion'))
    widget.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5() + """
    QWidget {
        font-family: 'Roboto', 'Segoe UI', 'Arial', sans-serif;
        font-size: 14px;
    }
    QLabel {
        font-size: 16px;
    }
    QPushButton {
        background-color: #3a3a3a;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #4a4a4a;
    }
    QPushButton:pressed {
        background-color: #555555;
    }
    QListWidget, QTextEdit {
        border: 1px solid #3a3a3a;
        border-radius: 5px;
        padding: 5px;
        font-size: 15px;
    }
    QComboBox {
        border: 1px solid #555555;
        border-radius: 5px;
        padding: 5px;
        min-width: 120px;
        font-size: 15px;
    }
    QHeaderView::section {
        background-color: #2b2b2b;
        padding: 6px;
        border: 1px solid #3a3a3a;
        font-size: 15px;
        font-weight: bold;
    }
    QStatusBar {
        font-size: 14px;
    }
    """)