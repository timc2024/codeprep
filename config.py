import os
import sys
from dotenv import load_dotenv

def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.abspath(os.path.dirname(__file__))

base_path = get_base_path()
env_path = os.path.join(base_path, '.env')

print(f"Base path: {base_path}")
print(f"Looking for .env file at: {env_path}")
print(f"Current working directory: {os.getcwd()}")
print(f"Directory contents: {os.listdir(base_path)}")

load_dotenv(env_path)

MONGODB_URI = os.getenv('MONGODB')

if not MONGODB_URI:
    print("MONGODB_URI not found in environment variables. Attempting to read from .env file...")
    try:
        with open(env_path, 'r') as env_file:
            for line in env_file:
                if line.startswith('MONGODB='):
                    MONGODB_URI = line.split('=', 1)[1].strip()
                    break
    except FileNotFoundError:
        print(f".env file not found at {env_path}")
    except Exception as e:
        print(f"Error reading .env file: {e}")

if not MONGODB_URI:
    print("MONGODB_URI is still not set. Please check your .env file or environment variables.")
    MONGODB_URI = "mongodb://localhost:27017"  # Fallback value

print(f"MONGODB_URI: {MONGODB_URI[:10]}...")  # Print first 10 characters for debugging

OUTPUT_FOLDER = "output"
SUPPORTED_LANGUAGES = ["Python", "Android", "React", "Flutter"]