
# coding: utf-8

# In[ ]:

import sys
from PyQt5.QtCore import Qt,QThread
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox, QPlainTextEdit, 
                             QMenu, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QWidget, QSlider)
import serial_rx_tx
import serial.tools.list_ports,time

sys_paused=True
prev_time=None

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
        grid.addWidget(self.cmdButtons(), 2, 0)
        #grid.addWidget(self.createExampleGroup(), 1, 1)
        self.setLayout(grid)

        self.setWindowTitle("STM Terminal")
        self.resize(400, 300)

        self.destroyed.connect(self.OnWindowClosing)

        #self.sliderWatch = QThread()

    # serial data callback function
    def OnReceiveSerialData(self,message):
        str_message = message.decode("utf-8")
        try:
            self.ta.insertPlainText(str_message)
        except(Exception ):
            self.serialPort.Close()

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
        self.slider.setMaximum(400)
        self.slider.setMinimum(1)
        self.slider.valueChanged.connect(self.sliderChanged)

        vbox = QVBoxLayout()
        vbox.addWidget(self.slider)
        #vbox.addStretch(1)
        self.groupBox.setLayout(vbox)
        return self.groupBox

    def sliderChanged(self):
        #if(prev_time==None):prev_time=time.time()
        #new_time = time.time()
        #elapsed_time = new_time - prev_time
        self.groupBox.setTitle("DDS Frequency set at %s Hz "% str(self.slider.value()))
        if not sys_paused:
            self.sendCmd('P')
        #print(elapsed_time)
        #prev_time=time.time()

    def sendCmd(self, c):
        print('starting..'+c)
        if(c=='P'):
            sys_paused=True
            self.btnPause.setEnabled(not sys_paused)
            self.btnResume.setEnabled(sys_paused)
        elif(c=='R'):
            #self.sendCmd(str(self.slider.value()))
            sys_paused=False
            self.btnPause.setEnabled(not sys_paused)
            self.btnResume.setEnabled(sys_paused)
            #time.sleep(1.2)
        self.serialPort.Send(c)

    def createLogArea(self):
        groupBox = QGroupBox("Log")

        self.ta = QPlainTextEdit(groupBox)
        vbox = QVBoxLayout()
        vbox.addWidget(self.ta)
        groupBox.setLayout(vbox)

        return groupBox

    def cmdButtons(self):
        groupBox = QGroupBox("Commands")

        self.btnPause = QPushButton("Pause",self)
        self.btnPause.clicked.connect(lambda: self.sendCmd('P'))
        self.btnPause.setEnabled(not sys_paused)
        self.btnResume = QPushButton("Capture",self)
        self.btnResume.clicked.connect(lambda: self.sendCmd('R'))
        hbox = QHBoxLayout()
        hbox.addWidget(self.btnPause)
        hbox.addWidget(self.btnResume)
        groupBox.setLayout(hbox)

        return groupBox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())


# In[ ]:



