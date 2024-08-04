from .android_handler import AndroidHandler
from .python_handler import PythonHandler
from .react_handler import ReactHandler
from .flutter_handler import FlutterHandler

def get_language_handler(language):
    handlers = {
        "Android": AndroidHandler,
        "Python": PythonHandler,
        "React": ReactHandler,
        "Flutter": FlutterHandler
    }
    handler_class = handlers.get(language)
    if handler_class:
        return handler_class()
    else:
        raise ValueError(f"Unsupported language: {language}")