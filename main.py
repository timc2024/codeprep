import sys
import os
from PyQt6.QtWidgets import QApplication, QMessageBox
from ui.main_window import MainWindow
from ui.styles import set_dark_theme
from dotenv import load_dotenv
from config import MONGODB_URI

def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.abspath(os.path.dirname(__file__))

def main():
    base_path = get_base_path()
    os.chdir(base_path)

    # Load .env file
    load_dotenv(os.path.join(base_path, '.env'))

    app = QApplication(sys.argv)
    set_dark_theme(app)

    if not MONGODB_URI:
        QMessageBox.critical(None, "Configuration Error", "MongoDB URI is not set. Please check your configuration.")
        return

    try:
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        QMessageBox.critical(None, "Error", f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()