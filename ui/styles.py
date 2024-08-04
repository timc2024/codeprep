from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QApplication

def set_dark_theme(app):
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.ColorRole.Window, QColor(40, 44, 52))
    dark_palette.setColor(QPalette.ColorRole.WindowText, QColor(171, 178, 191))
    dark_palette.setColor(QPalette.ColorRole.Base, QColor(58, 63, 75))
    dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ColorRole.ToolTipText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ColorRole.Text, QColor(171, 178, 191))
    dark_palette.setColor(QPalette.ColorRole.Button, QColor(58, 63, 75))
    dark_palette.setColor(QPalette.ColorRole.ButtonText, QColor(171, 178, 191))
    dark_palette.setColor(QPalette.ColorRole.BrightText, QColor(255, 0, 0))
    dark_palette.setColor(QPalette.ColorRole.Link, QColor(97, 175, 239))
    dark_palette.setColor(QPalette.ColorRole.Highlight, QColor(97, 175, 239))
    dark_palette.setColor(QPalette.ColorRole.HighlightedText, QColor(40, 44, 52))
    app.setPalette(dark_palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
