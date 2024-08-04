import os
import sys
import logging

print(f"Current working directory: {os.getcwd()}")
print(f"Executable path: {sys.executable}")
print(f"sys.argv[0]: {sys.argv[0]}")
print(f"__file__: {__file__}")
print(f"Contents of current directory: {os.listdir()}")

from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.styles import set_dark_theme
from dotenv import load_dotenv


# Rest of your imports and code...
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
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()