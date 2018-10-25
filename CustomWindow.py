from PySide2 import QtWidgets
from BaseUI import MUIWindow

class CustomWindow(MUIWindow.MUIWindow):

    def __init__(self):
        ui_url = '/home/chi/maya/scripts/MUI/resource/mui.ui'
        super(CustomWindow,self).__init__(ui_url)

    # ----------------------------------------------- init UI stuff -----------------------------------------------
    def init_UI(self):
        self.btn = self.getUIElement(QtWidgets.QPushButton,"pushButton")
        self.lineEdit = self.getUIElement(QtWidgets.QLineEdit,"lineEdit")
        self.label = self.getUIElement(QtWidgets.QLabel,"label")

    def SignalSlotLinker(self):
        self.btn.clicked.connect( self.updateLineEdit)

    # ----------------------------------------------- slot function -----------------------------------------------
    def updateLineEdit(self):
        self.label.setText(self.lineEdit.text())


