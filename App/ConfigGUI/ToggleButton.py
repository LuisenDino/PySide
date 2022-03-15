from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class ToggleButton(QWidget):
    def __init__(self, boolVar):
        super().__init__()
        self.boolVar = boolVar

        #Set Layout
        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)

        self.on = QPushButton("On", self)
        self.on.clicked.connect(self.toggle)
        self.mainLayout.addWidget(self.on, 0,0)
        self.off = QPushButton("Off", self)
        self.off.clicked.connect(self.toggle)
        self.mainLayout.addWidget(self.off, 0,1)

        if self.boolVar:
            self.off.setEnabled(False)
            self.on.setEnabled(True)
        else:
            self.on.setEnabled(False)
            self.off.setEnabled(True)
    
    def get(self): 
        return self.boolVar

    def toggle(self):
        self.boolVar = not self.boolVar
        if self.on.isEnabled():
            self.on.setEnabled(False)
            self.off.setEnabled(True)
        else:
            self.off.setEnabled(False)
            self.on.setEnabled(True)