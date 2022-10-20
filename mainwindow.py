from base64 import decodebytes
from contextlib import redirect_stderr
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particle_adminstrator import administrador
from particulas import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.administrador = administrador()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregarFinal_pushButton.clicked.connect(self.click_agregar)
        self.ui.AgragrInicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.Mostrar_pushButton.clicked.connect(self.click_mostrar)

    @Slot()
    def click_mostrar(self):
        # self.administrador.mostrar()
        self.ui.salida.insertPlainText(str(self.administrador))


    @Slot()
    def click_agregar_inicio(self):
        desX = self.ui.DesX_pinBox.value()
        desY = self.ui.DesY_spinBox_2.value()
        velocidad = self.ui.Velocidad_spinBox_3.value()
        red = self.ui.Red_spinBox_4.value()
        green = self.ui.Green_spinBox_5.value()
        blue = self.ui.Blue_spinBox_6.value()

        Particle = Particula(0, destino_x=desX, destino_y=desY, velocidad=velocidad, red=red, green=green, blue=blue)
        self.administrador.agregar_incio(Particle)
    
    @Slot()
    def click_agregar(self):
        desX = self.ui.DesX_pinBox.value()
        desY = self.ui.DesY_spinBox_2.value()
        velocidad = self.ui.Velocidad_spinBox_3.value()
        red = self.ui.Red_spinBox_4.value()
        green = self.ui.Green_spinBox_5.value()
        blue = self.ui.Blue_spinBox_6.value()

        Particle = Particula(0, destino_x=desX, destino_y=desY, velocidad=velocidad, red=red, green=green, blue=blue)
        self.administrador.agregar_final(Particle)

        
