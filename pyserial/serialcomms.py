
# coding: utf-8

# In[ ]:

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox, QPlainTextEdit, 
                             QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QSlider)
import serial_rx_tx
import serial.tools.list_ports


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        for m in serial.tools.list_ports.comports():
            if 'VID:PID=1F00:2012' in m.usb_info():
                port=m.device

        self.serialPort = serial_rx_tx.SerialPort()
        # Register the callback above with the serial port object
        self.serialPort.RegisterReceiveCallback(self.OnReceiveSerialData)
        self.serialPort.Open(port,115200)

        grid = QGridLayout()
        grid.addWidget(self.createSlider(), 0, 0)
        grid.addWidget(self.createLogArea(), 1, 0)
        #grid.addWidget(self.createExampleGroup(), 0, 1)
        #grid.addWidget(self.createExampleGroup(), 1, 1)
        self.setLayout(grid)

        self.setWindowTitle("STM Terminal")
        self.resize(400, 300)

        self.destroyed.connect(self.OnWindowClosing)

    # serial data callback function
    def OnReceiveSerialData(self,message):
        str_message = message.decode("utf-8")
        self.ta.insertPlainText(str_message)

    # Release resources
    def OnWindowClosing(self,message):
        self.serialPort.Close()

    def createSlider(self):
        self.groupBox = QGroupBox("DDS Frequency set at 1 Hz")

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
        self.groupBox.setTitle("DDS Frequency set at %s Hz "% str(self.slider.value()))


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



