# Form implementation generated from reading ui file 'C:\Users\tapia\Desktop\IndustrialEngeenering\Second_2023-1\Programacion Avanzada\Clase 05_05_2013\2 AdmonFacultad\2 AdmonFacultad\Diseno\DFuentes.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1053, 801)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 100, 971, 674))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.LEModificarContacto = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.LEModificarContacto.setObjectName("LEModificarContacto")
        self.gridLayout.addWidget(self.LEModificarContacto, 11, 2, 1, 1)
        self.PBBuscar = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBBuscar.setFont(font)
        self.PBBuscar.setObjectName("PBBuscar")
        self.gridLayout.addWidget(self.PBBuscar, 3, 1, 1, 1)
        self.LContactoAgregar = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LContactoAgregar.setFont(font)
        self.LContactoAgregar.setObjectName("LContactoAgregar")
        self.gridLayout.addWidget(self.LContactoAgregar, 6, 2, 1, 1)
        self.LCodigoNombreNuevo = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LCodigoNombreNuevo.setFont(font)
        self.LCodigoNombreNuevo.setObjectName("LCodigoNombreNuevo")
        self.gridLayout.addWidget(self.LCodigoNombreNuevo, 6, 1, 1, 1)
        self.SBCodigoBuscar = QtWidgets.QSpinBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SBCodigoBuscar.setFont(font)
        self.SBCodigoBuscar.setMaximum(1000)
        self.SBCodigoBuscar.setObjectName("SBCodigoBuscar")
        self.gridLayout.addWidget(self.SBCodigoBuscar, 4, 0, 1, 1)
        self.LCodigoEliminar = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LCodigoEliminar.setFont(font)
        self.LCodigoEliminar.setObjectName("LCodigoEliminar")
        self.gridLayout.addWidget(self.LCodigoEliminar, 1, 0, 1, 2)
        self.LCodigoModificar = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LCodigoModificar.setFont(font)
        self.LCodigoModificar.setObjectName("LCodigoModificar")
        self.gridLayout.addWidget(self.LCodigoModificar, 3, 0, 1, 1)
        self.LCodigoNuevo = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LCodigoNuevo.setFont(font)
        self.LCodigoNuevo.setObjectName("LCodigoNuevo")
        self.gridLayout.addWidget(self.LCodigoNuevo, 6, 0, 1, 1)
        self.LEAgregarNombre = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.LEAgregarNombre.setObjectName("LEAgregarNombre")
        self.gridLayout.addWidget(self.LEAgregarNombre, 7, 1, 1, 1)
        self.LENombreModificar = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.LENombreModificar.setObjectName("LENombreModificar")
        self.gridLayout.addWidget(self.LENombreModificar, 11, 1, 1, 1)
        self.PBModificar = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBModificar.setFont(font)
        self.PBModificar.setObjectName("PBModificar")
        self.gridLayout.addWidget(self.PBModificar, 8, 1, 1, 1)
        self.LNombreModificar = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LNombreModificar.setFont(font)
        self.LNombreModificar.setObjectName("LNombreModificar")
        self.gridLayout.addWidget(self.LNombreModificar, 10, 1, 1, 1)
        self.LContactoModificar = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LContactoModificar.setFont(font)
        self.LContactoModificar.setObjectName("LContactoModificar")
        self.gridLayout.addWidget(self.LContactoModificar, 10, 2, 1, 1)
        self.SBCodigoNuevo = QtWidgets.QSpinBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SBCodigoNuevo.setFont(font)
        self.SBCodigoNuevo.setMaximum(1000)
        self.SBCodigoNuevo.setObjectName("SBCodigoNuevo")
        self.gridLayout.addWidget(self.SBCodigoNuevo, 7, 0, 1, 1)
        self.LCodigoModifica = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LCodigoModifica.setFont(font)
        self.LCodigoModifica.setObjectName("LCodigoModifica")
        self.gridLayout.addWidget(self.LCodigoModifica, 10, 0, 1, 1)
        self.SBCodigoExistente = QtWidgets.QSpinBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SBCodigoExistente.setFont(font)
        self.SBCodigoExistente.setMaximum(1000)
        self.SBCodigoExistente.setObjectName("SBCodigoExistente")
        self.gridLayout.addWidget(self.SBCodigoExistente, 9, 0, 1, 1)
        self.SBCodigoModificar = QtWidgets.QSpinBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SBCodigoModificar.setFont(font)
        self.SBCodigoModificar.setMaximum(1000)
        self.SBCodigoModificar.setObjectName("SBCodigoModificar")
        self.gridLayout.addWidget(self.SBCodigoModificar, 11, 0, 1, 1)
        self.LEAgregarContacto = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.LEAgregarContacto.setObjectName("LEAgregarContacto")
        self.gridLayout.addWidget(self.LEAgregarContacto, 7, 2, 1, 1)
        self.TWTabla = QtWidgets.QTableWidget(parent=self.layoutWidget)
        self.TWTabla.setMinimumSize(QtCore.QSize(711, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TWTabla.setFont(font)
        self.TWTabla.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.TWTabla.setObjectName("TWTabla")
        self.TWTabla.setColumnCount(3)
        self.TWTabla.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TWTabla.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWTabla.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWTabla.setHorizontalHeaderItem(2, item)
        self.TWTabla.horizontalHeader().setDefaultSectionSize(144)
        self.TWTabla.verticalHeader().setMinimumSectionSize(60)
        self.gridLayout.addWidget(self.TWTabla, 12, 0, 1, 3)
        self.PBSalir = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBSalir.setFont(font)
        self.PBSalir.setObjectName("PBSalir")
        self.gridLayout.addWidget(self.PBSalir, 13, 2, 1, 1)
        self.LCodigoExistente = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LCodigoExistente.setFont(font)
        self.LCodigoExistente.setObjectName("LCodigoExistente")
        self.gridLayout.addWidget(self.LCodigoExistente, 8, 0, 1, 1)
        self.SBCodigoEliminar = QtWidgets.QSpinBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SBCodigoEliminar.setFont(font)
        self.SBCodigoEliminar.setObjectName("SBCodigoEliminar")
        self.gridLayout.addWidget(self.SBCodigoEliminar, 2, 0, 1, 1)
        self.PBTodas = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBTodas.setFont(font)
        self.PBTodas.setObjectName("PBTodas")
        self.gridLayout.addWidget(self.PBTodas, 2, 2, 1, 1)
        self.PBEliminar = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBEliminar.setFont(font)
        self.PBEliminar.setObjectName("PBEliminar")
        self.gridLayout.addWidget(self.PBEliminar, 2, 1, 1, 1)
        self.LTitulo = QtWidgets.QLabel(parent=self.layoutWidget)
        self.LTitulo.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LTitulo.setFont(font)
        self.LTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LTitulo.setObjectName("LTitulo")
        self.gridLayout.addWidget(self.LTitulo, 0, 0, 1, 3)
        self.PBAgregar = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PBAgregar.setFont(font)
        self.PBAgregar.setObjectName("PBAgregar")
        self.gridLayout.addWidget(self.PBAgregar, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.SBCodigoEliminar, self.PBEliminar)
        MainWindow.setTabOrder(self.PBEliminar, self.TWTabla)
        MainWindow.setTabOrder(self.TWTabla, self.PBSalir)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PBBuscar.setText(_translate("MainWindow", "Buscar"))
        self.LContactoAgregar.setText(_translate("MainWindow", "Contacto Nuevo"))
        self.LCodigoNombreNuevo.setText(_translate("MainWindow", "Nombre Nuevo"))
        self.LCodigoEliminar.setText(_translate("MainWindow", "Código a Eliminar"))
        self.LCodigoModificar.setText(_translate("MainWindow", "Código a Buscar"))
        self.LCodigoNuevo.setText(_translate("MainWindow", "Código Nuevo"))
        self.PBModificar.setText(_translate("MainWindow", "Modificar"))
        self.LNombreModificar.setText(_translate("MainWindow", "Nombre Nuevo"))
        self.LContactoModificar.setText(_translate("MainWindow", "Contacto Nuevo"))
        self.LCodigoModifica.setText(_translate("MainWindow", "Código Nuevo"))
        item = self.TWTabla.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Codigo"))
        item = self.TWTabla.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.TWTabla.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Contacto"))
        self.PBSalir.setText(_translate("MainWindow", "Salir Fuentes"))
        self.LCodigoExistente.setText(_translate("MainWindow", "Código Existente"))
        self.PBTodas.setText(_translate("MainWindow", "Ver Todas"))
        self.PBEliminar.setText(_translate("MainWindow", "Eliminar"))
        self.LTitulo.setText(_translate("MainWindow", "Administración de Fuentes de Financiación"))
        self.PBAgregar.setText(_translate("MainWindow", "Agregar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
