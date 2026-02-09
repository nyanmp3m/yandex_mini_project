from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout
import sys
import io
from PyQt6 import uic


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>925</width>
    <height>744</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLineEdit" name="Get_Coord">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>110</y>
      <width>241</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="Get_Ma_bt">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>160</y>
      <width>241</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Отобразить карту</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(io.StringIO(template), self)

        self.Get_Coord = QLineEdit(self)
        self.Get_Coord.setText("")
        self.Get_Coord.move(30, 30)

        self.Get_Map_bt = QPushButton(self, "Получить карту")

        self.Map = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.Get_Coord)
        layout.addWidget(self.Get_Map_bt)
        layout.addWidget(self.Map)

        self.Get_Map_bt.clicked.connect(self.get_text)

        self.setLayout(layout)

    def get_text(self):
        self.coords = self.Get_Coord.text()


    def mouseMoveEvent(self, event):
        self.Get_Coord.setText(f"Координаты: {event.pos().x()}, {event.pos().y()}")

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())