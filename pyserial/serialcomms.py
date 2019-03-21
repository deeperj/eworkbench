
# coding: utf-8

# In[ ]:

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox, QPlainTextEdit, 
                             QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QSlider)

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        grid = QGridLayout()
        grid.addWidget(self.createSlider(), 0, 0)
        grid.addWidget(self.createLogArea(), 1, 0)
        #grid.addWidget(self.createExampleGroup(), 0, 1)
        #grid.addWidget(self.createExampleGroup(), 1, 1)
        self.setLayout(grid)

        self.setWindowTitle("STM Terminal")
        self.resize(400, 300)

    def createSlider(self):
        self.groupBox = QGroupBox("DDS Frequency = 1")

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.setSingleStep(1)
        self.slider.setMaximum(100)
        self.slider.setMinimum(1)
        self.slider.valueChanged.connect(self.sliderChanged)

        vbox = QVBoxLayout()
        vbox.addWidget(self.slider)
        #vbox.addStretch(1)
        self.groupBox.setLayout(vbox)
        return self.groupBox

    def sliderChanged(self):
        self.groupBox.setTitle("DDS Frequency = "+str(self.slider.value()))


    def createLogArea(self):
        groupBox = QGroupBox("Log")


        self.ta = QPlainTextEdit(groupBox)
        vbox = QVBoxLayout()
        vbox.addWidget(self.ta)
        groupBox.setLayout(vbox)

        return groupBox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())


# In[ ]:



