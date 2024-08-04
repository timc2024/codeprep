from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDropEvent

class RulePreviewWidget(QTextEdit):
    def __init__(self, masking_rules):
        super().__init__()
        self.masking_rules = masking_rules
        self.setAcceptDrops(True)
        self.setReadOnly(True)

    def dragEnterEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.DropAction.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.DropAction.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                if file_path.endswith('.txt'):
                    self.load_masking_rules(file_path)
                    break
        else:
            event.ignore()

    def load_masking_rules(self, file_path):
        self.masking_rules.load_from_file(file_path)
        self.update_preview()

    def update_preview(self):
        self.setText("\n".join([f"{original} -> {masked}" for original, masked in self.masking_rules.rules]))