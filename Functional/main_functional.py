import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt

from design.python_files.MainWindow_class import MainWindow_class

from python.api_request import get_image

class MainWindow(QMainWindow, MainWindow_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.scale = 14

        self.display_btn.clicked.connect(self.get_text)

    def get_text(self):
        self.coords = self.get_coord_led.text()

        try:
            resp = get_image(list(map(float, self.coords.split())), self.scale)
            with open("map.png", "wb") as f:
                f.write(resp.content)

        except Exception:
            ...

        pixmap = QPixmap("map.png")
        self.map_field_lbl.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_PageUp:
            self.scale += 1
        elif event.key() == Qt.Key.Key_PageDown:
            self.scale -= 1
        self.current_scale_lbl.setText(f'Текущий маштаб карты: {self.scale}')

        super().keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())