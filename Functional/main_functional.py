import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt

from design.python_files.MainWindow_class import MainWindow_class

from python.api_request_staticMap import get_image
from python.api_request_geocode import get_coord


class MainWindow(QMainWindow, MainWindow_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.scale = 14
        self.delta = 0.01911
        self.radio_buttons_theme = [self.dark_theme_rbt, self.light_theme_rbt]
        self.radio_buttons_maptype = [self.base_rbt, self.car_rbt, self.public_car_rbt, self.admin_rbt]
        self.marks = []

        self.current_maptype = 'map'
        self.current_theme = 'light'
        self.last_mark = None
        self.apply_light_theme()

        self.flag_get_coord_led = True

        self.last_coord = [37.620070, 55.753630]

        self.display_btn.clicked.connect(self.get_text)
        self.apply_them_btn.clicked.connect(self.apply_changes)
        self.find_object_btn.clicked.connect(self.find_object)
        self.drop_search_btn.clicked.connect(self.drop_search)

    def get_map_image(self, coord):
        try:
            resp = get_image(coord, self.scale, theme=self.current_theme, maptype=self.current_maptype,
                             marks=self.marks)
            with open("map.png", "wb") as f:
                f.write(resp.content)
            f.close()

        except Exception as exc:
            print("Ошибка", exc)

    def display_map(self):
        pixmap = QPixmap("map.png")
        self.map_field_lbl.setPixmap(pixmap)

    def get_text(self):
        coord = self.get_coord_led.text()
        coord = list(map(float, coord.split()))

        if coord:
            self.last_coord = coord
        if coord in [None, []]:
            coord = self.last_coord

        self.get_map_image(coord)
        self.display_map()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_PageUp:
            self.scale += 1
        elif event.key() == Qt.Key.Key_PageDown:
            self.scale -= 1
        elif event.key() == Qt.Key.Key_W:
            self.get_map_image([self.last_coord[0], self.last_coord[1] + self.delta])
            self.display_map()

            self.last_coord = [self.last_coord[0], self.last_coord[1] + self.delta]
        elif event.key() == Qt.Key.Key_S:
            self.get_map_image([self.last_coord[0], self.last_coord[1] - self.delta])
            self.display_map()

            self.last_coord = [self.last_coord[0], self.last_coord[1] - self.delta]
        elif event.key() == Qt.Key.Key_A:
            self.get_map_image([self.last_coord[0] - self.delta, self.last_coord[1]])
            self.display_map()

            self.last_coord = [self.last_coord[0] - self.delta, self.last_coord[1]]
        elif event.key() == Qt.Key.Key_D:
            self.get_map_image([self.last_coord[0] + self.delta, self.last_coord[1]])
            self.display_map()

            self.last_coord = [self.last_coord[0] + self.delta, self.last_coord[1]]
        elif event.key() == Qt.Key.Key_Up:
            self.get_map_image([self.last_coord[0], self.last_coord[1] + 0.0002])
            self.display_map()

            self.last_coord = [self.last_coord[0], self.last_coord[1] + 0.0002]
        elif event.key() == Qt.Key.Key_Down:
            self.get_map_image([self.last_coord[0], self.last_coord[1] - 0.0002])
            self.display_map()

            self.last_coord = [self.last_coord[0], self.last_coord[1] - 0.0002]
        elif event.key() == Qt.Key.Key_Left:
            self.get_map_image([self.last_coord[0] - 0.0002, self.last_coord[1]])
            self.display_map()

            self.last_coord = [self.last_coord[0] - 0.0002, self.last_coord[1]]
        elif event.key() == Qt.Key.Key_Right:
            self.get_map_image([self.last_coord[0] + 0.0002, self.last_coord[1]])
            self.display_map()

            self.last_coord = [self.last_coord[0] + 0.0002, self.last_coord[1]]
        elif event.key() == Qt.Key.Key_L:
            self.flag_get_coord_led = not self.flag_get_coord_led
            self.get_coord_led.setEnabled(self.flag_get_coord_led)
            self.display_btn.setEnabled(self.flag_get_coord_led)
            self.get_coord_led_chb.setEnabled(self.flag_get_coord_led)

        self.current_scale_lbl.setText(f'Текущий маштаб карты: {self.scale}')

        super().keyPressEvent(event)

    def check_radio_buttons(self, radio_buttons):
        data = {}
        checked_rbt = None

        for rbt in radio_buttons:
            data[rbt.objectName()] = rbt.isChecked()
            if rbt.isChecked():
                checked_rbt = rbt.objectName()
        return [data, checked_rbt]

    def apply_light_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                color: #000000;
            }
            QPushButton {
                background-color: #e0e0e0;
                color: #000000;
            }
        """)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QPushButton {
                background-color: #444444;
                color: #ffffff;
            }
        """)

    def apply_changes(self):
        data_rbt = self.check_radio_buttons(self.radio_buttons_theme)
        if data_rbt[1] == 'light_theme_rbt':
            self.apply_light_theme()
            self.current_theme = 'light'
        elif data_rbt[1] == 'dark_theme_rbt':
            self.apply_dark_theme()
            self.current_theme = 'dark'

        data_rbt = self.check_radio_buttons(self.radio_buttons_maptype)
        if data_rbt[1] == 'base_rbt':
            self.current_maptype = 'map'
        elif data_rbt[1] == 'car_rbt':
            self.current_maptype = 'driving'
        elif data_rbt[1] == 'public_car_rbt':
            self.current_maptype = 'transit'
        elif data_rbt[1] == 'admin_rbt':
            self.current_maptype = 'admin'

        self.get_map_image(self.last_coord)
        self.display_map()

    def add_mark(self, coord):
        self.marks.append(f'{coord[0]},{coord[1]},vkbkm')

    def print_information(self, full_address):
        text = f"""Full address: {full_address}\n
        """
        self.information_tbr.setPlainText(text)

    def find_object(self):
        address = self.search_bar_led.text()
        response = get_coord(address)

        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_coodrinates = list(map(float, toponym_coodrinates.split()))

        self.print_information(toponym_address)

        self.add_mark(toponym_coodrinates)
        self.get_map_image(toponym_coodrinates)

        self.last_coord = toponym_coodrinates
        self.last_mark = f'{toponym_coodrinates[0]},{toponym_coodrinates[1]},vkbkm'

        self.display_map()

    def drop_search(self):
        if self.last_mark in self.marks:
            self.marks.remove(self.last_mark)
        else:
            self.search_bar_led.setText("Уже удалена")
        self.information_tbr.clear()

        self.get_map_image(self.last_coord)
        self.display_map()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
