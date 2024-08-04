import os
import sys

from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.styles import set_dark_theme
from dotenv import load_dotenv

def main():
    # Load .env file from the project root
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    app = QApplication(sys.argv)
    set_dark_theme(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()