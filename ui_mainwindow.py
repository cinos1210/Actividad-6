# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(624, 309)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 20, 211, 201))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter_2 = QSplitter(self.groupBox)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.label = QLabel(self.splitter_2)
        self.label.setObjectName(u"label")
        self.splitter_2.addWidget(self.label)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName(u"label_2")
        self.splitter_2.addWidget(self.label_2)
        self.label_3 = QLabel(self.splitter_2)
        self.label_3.setObjectName(u"label_3")
        self.splitter_2.addWidget(self.label_3)
        self.label_4 = QLabel(self.splitter_2)
        self.label_4.setObjectName(u"label_4")
        self.splitter_2.addWidget(self.label_4)
        self.label_5 = QLabel(self.splitter_2)
        self.label_5.setObjectName(u"label_5")
        self.splitter_2.addWidget(self.label_5)
        self.label_6 = QLabel(self.splitter_2)
        self.label_6.setObjectName(u"label_6")
        self.splitter_2.addWidget(self.label_6)

        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 1)

        self.AgragrInicio_pushButton = QPushButton(self.groupBox)
        self.AgragrInicio_pushButton.setObjectName(u"AgragrInicio_pushButton")

        self.gridLayout.addWidget(self.AgragrInicio_pushButton, 2, 0, 1, 1)

        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(True)
        self.DesX_pinBox = QSpinBox(self.splitter)
        self.DesX_pinBox.setObjectName(u"DesX_pinBox")
        self.DesX_pinBox.setMaximum(500)
        self.splitter.addWidget(self.DesX_pinBox)
        self.DesY_spinBox_2 = QSpinBox(self.splitter)
        self.DesY_spinBox_2.setObjectName(u"DesY_spinBox_2")
        self.DesY_spinBox_2.setMaximum(500)
        self.splitter.addWidget(self.DesY_spinBox_2)
        self.Velocidad_spinBox_3 = QSpinBox(self.splitter)
        self.Velocidad_spinBox_3.setObjectName(u"Velocidad_spinBox_3")
        self.Velocidad_spinBox_3.setMaximum(1000)
        self.splitter.addWidget(self.Velocidad_spinBox_3)
        self.Red_spinBox_4 = QSpinBox(self.splitter)
        self.Red_spinBox_4.setObjectName(u"Red_spinBox_4")
        self.Red_spinBox_4.setMaximum(255)
        self.splitter.addWidget(self.Red_spinBox_4)
        self.Green_spinBox_5 = QSpinBox(self.splitter)
        self.Green_spinBox_5.setObjectName(u"Green_spinBox_5")
        self.Green_spinBox_5.setMaximum(255)
        self.splitter.addWidget(self.Green_spinBox_5)
        self.Blue_spinBox_6 = QSpinBox(self.splitter)
        self.Blue_spinBox_6.setObjectName(u"Blue_spinBox_6")
        self.Blue_spinBox_6.setMaximum(255)
        self.splitter.addWidget(self.Blue_spinBox_6)

        self.gridLayout.addWidget(self.splitter, 1, 1, 1, 1)

        self.agregarFinal_pushButton = QPushButton(self.groupBox)
        self.agregarFinal_pushButton.setObjectName(u"agregarFinal_pushButton")

        self.gridLayout.addWidget(self.agregarFinal_pushButton, 2, 1, 1, 1)

        self.Mostrar_pushButton = QPushButton(self.centralwidget)
        self.Mostrar_pushButton.setObjectName(u"Mostrar_pushButton")
        self.Mostrar_pushButton.setGeometry(QRect(40, 220, 201, 23))
        self.salida = QPlainTextEdit(self.centralwidget)
        self.salida.setObjectName(u"salida")
        self.salida.setGeometry(QRect(250, 20, 361, 231))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 624, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particula", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino X:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino Y:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.AgragrInicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al Inicio", None))
        self.agregarFinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.Mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
    # retranslateUi