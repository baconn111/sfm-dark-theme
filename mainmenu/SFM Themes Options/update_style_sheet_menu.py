import sfm, sfmApp, sfmConsole
from PySide import QtCore, QtGui, shiboken

class StyleSheetMenu(QtGui.QWidget):
    def __init__(self):
        
        super(StyleSheetMenu, self).__init__()
        self.Window()

    def Window(self):

        grid = QtGui.QGridLayout()
        
        self.buttonSmallSheet = QtGui.QPushButton()
        self.buttonSmallSheet.setText("Apply Small Sheet")
        self.buttonSmallSheet.clicked.connect(lambda: self.setSheet())
        grid.addWidget(self.buttonSmallSheet, 0, 0, 0)

        self.buttonReloadSheet = QtGui.QPushButton()
        self.buttonReloadSheet.setText("Reload to Default")
        self.buttonReloadSheet.clicked.connect(lambda: self.reloadSheet())
        grid.addWidget(self.buttonReloadSheet, 1, 0, 0)
        self.setLayout(grid)


    def setSheet(self):
        sfmApp.ExecuteGameCommand("sfm_smallstylesheet")
    def reloadSheet(self):
        sfmApp.ExecuteGameCommand("sfm_reloadstylesheet")

Janela = StyleSheetMenu()
sfmApp.RegisterTabWindow( "Style Sheet Menu", "Menu Style Sheet", shiboken.getCppPointer( Janela )[0] )
sfmApp.ShowTabWindow("Style Sheet Menu")
