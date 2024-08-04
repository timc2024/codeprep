from PyQt6.QtWidgets import QComboBox
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QPoint, Qt, pyqtProperty
from PyQt6.QtGui import QPainter, QColor, QPen, QPolygon

class AnimatedComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._arrow_rotation = 0
        self._animation = QPropertyAnimation(self, b"arrowRotation")
        self._animation.setDuration(200)
        self._animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        
        # Add some padding and set a modern style
        self.setStyleSheet("""
            QComboBox {
                padding: 5px 30px 5px 10px;
                border: 1px solid #abb2bf;
                border-radius: 4px;
                background-color: #282c34;
                color: #abb2bf;
            }
            QComboBox::drop-down {
                border: none;
            }
        """)

    def showPopup(self):
        self._animation.setEndValue(180)
        self._animation.start()
        super().showPopup()

    def hidePopup(self):
        self._animation.setEndValue(0)
        self._animation.start()
        super().hidePopup()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw the arrow
        arrow_size = 8
        arrow_x = self.width() - arrow_size - 15  # Increased padding
        arrow_y = (self.height() - arrow_size) // 2

        painter.save()
        painter.translate(arrow_x + arrow_size / 2, arrow_y + arrow_size / 2)
        painter.rotate(self._arrow_rotation)
        painter.translate(-arrow_size / 2, -arrow_size / 2)

        arrow = QPolygon([
            QPoint(0, 0),
            QPoint(arrow_size, 0),
            QPoint(arrow_size // 2, arrow_size // 2)
        ])

        painter.setPen(QPen(QColor("#abb2bf"), 1.5))  # Slightly thinner line
        painter.setBrush(QColor("#abb2bf"))
        painter.drawPolygon(arrow)
        painter.restore()

    def get_arrow_rotation(self):
        return self._arrow_rotation

    def set_arrow_rotation(self, value):
        self._arrow_rotation = value
        self.update()

    arrowRotation = pyqtProperty(float, get_arrow_rotation, set_arrow_rotation)