from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from design.python_files.MainWindow_class import MainWindow_class

from python.api_request import get_image

class MainWindow(QMainWindow, MainWindow_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Get_Ma_bt.clicked.connect(self.get_text)

    def get_text(self):
        self.coords = self.Get_Coord.text()

        resp = get_image(list(map(float, self.coords.split())))

        with open("map.png", "wb") as f:
            f.write(resp.content)

        pixmap = QPixmap("map.png")
        self.Map.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())