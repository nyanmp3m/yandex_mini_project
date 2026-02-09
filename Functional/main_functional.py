from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMainWindow
import sys
from ui_file import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Get_Ma_bt.clicked.connect(self.get_text)

    def get_text(self):
        self.coords = self.Get_Coord.text()

    def mouseMoveEvent(self, event):
        self.Get_Coord.setText(f"Координаты: {event.pos().x()}, {event.pos().y()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())