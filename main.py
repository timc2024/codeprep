import sys
import os
import logging
from PyQt6.QtWidgets import QApplication, QMessageBox
from ui.main_window import MainWindow
from ui.styles import set_dark_theme
from dotenv import load_dotenv
from config import MONGODB_URI, OUTPUT_FOLDER, SUPPORTED_LANGUAGES

def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.abspath(os.path.dirname(__file__))

def test_config():
    print("Testing configuration...")
    print(f"Base path: {get_base_path()}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"MONGODB_URI: {MONGODB_URI[:10]}..." if MONGODB_URI else "MONGODB_URI is not set")
    print(f"OUTPUT_FOLDER: {OUTPUT_FOLDER}")
    print(f"SUPPORTED_LANGUAGES: {SUPPORTED_LANGUAGES}")
    print(".env file contents:")
    env_path = os.path.join(get_base_path(), '.env')
    try:
        with open(env_path, 'r') as env_file:
            print(env_file.read())
    except FileNotFoundError:
        print(f".env file not found at {env_path}")
    except Exception as e:
        print(f"Error reading .env file: {e}")
    print("Directory contents:")
    print(os.listdir(get_base_path()))
    print("Configuration test complete.")

def main():
    base_path = get_base_path()
    os.chdir(base_path)

    # Load .env file
    load_dotenv(os.path.join(base_path, '.env'))

    if "--test-config" in sys.argv:
        test_config()
        return

    app = QApplication(sys.argv)
    set_dark_theme(app)

    if not MONGODB_URI or MONGODB_URI == "mongodb://localhost:27017":
        QMessageBox.critical(None, "Configuration Error", "MongoDB URI is not set correctly. Please check your .env file or environment variables.")
        return

    try:
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        logging.exception("An unexpected error occurred while initializing the main window")
        QMessageBox.critical(None, "Error", f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        main()
    except Exception as e:
        logging.exception("An unexpected error occurred in main")
        QMessageBox.critical(None, "Critical Error", f"A critical error occurred: {str(e)}\nThe application will now exit.")
        sys.exit(1)