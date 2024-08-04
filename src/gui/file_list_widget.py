import os
from PyQt5.QtWidgets import QListWidget, QAbstractItemView, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDropEvent, QKeyEvent

class FileListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)  # Enable multi-selection
        self.current_language = "Python"  # Default language
        self.language_extensions = {
            "Android": ('.java', '.kt', '.xml'),
            "Python": ('.py', '.txt'),
            "React": ('.js', '.jsx', '.ts', '.tsx'),
            "Flutter": ('.dart',)
        }

    def set_language(self, language):
        self.current_language = language
        self.filter_items()

    def dragEnterEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            dropped_files = []
            for url in event.mimeData().urls():
                path = url.toLocalFile()
                dropped_files.extend(self.process_dropped_path(path))

            if not dropped_files:
                QMessageBox.warning(self, "No Matching Files",
                                    f"No files matching the current language ({self.current_language}) were found in the dropped items.\n\n"
                                    f"Accepted extensions: {', '.join(self.language_extensions[self.current_language])}")
        else:
            event.ignore()

    def process_dropped_path(self, path):
        dropped_files = []
        if os.path.isfile(path):
            if self.add_file(path):
                dropped_files.append(path)
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if self.add_file(file_path):
                        dropped_files.append(file_path)
        return dropped_files

    def add_file(self, path):
        if path.endswith(self.language_extensions[self.current_language]):
            if path not in [self.item(i).text() for i in range(self.count())]:
                self.addItem(path)
                return True
        return False

    def filter_items(self):
        for i in range(self.count() - 1, -1, -1):
            item = self.item(i)
            if not item.text().endswith(self.language_extensions[self.current_language]):
                self.takeItem(i)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Delete:
            self.delete_selected_items()
        else:
            super().keyPressEvent(event)

    def delete_selected_items(self):
        for item in self.selectedItems():
            self.takeItem(self.row(item))