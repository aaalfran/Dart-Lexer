from PyQt5 import QtCore, QtGui, QtWidgets
import lexico as lex
import sintaxis as sin
import sys

class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(225, 52, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 52, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(225, 52, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        MainWindow.setPalette(palette)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(420, 80, 361, 351))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 80, 361, 351))
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(580, 60, 47, 13))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 480, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 480, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 480, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.connectActions()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Funcion para conectar las funcionalidades de el GUI a sus respectivas funciones
    def connectActions(self):
        self.pushButton.clicked.connect(self.syntax)
        self.pushButton_2.clicked.connect(self.lexer)
        self.pushButton_3.clicked.connect(self.clear)
    
    # Funcion para realizar el analisis sintactico
    def syntax(self):
        self.textBrowser_2.setText("")
        texto = self.textEdit.toPlainText()
        #sin.validaRegla(texto)

        lines = 0
        for item in texto.splitlines():
         lines += 1
        if item:
            gram = sin.validaRegla(texto)
            #print(gram)
            if gram is None:
                self.textBrowser_2.insertPlainText("Info: No hay errores! \n")
            else:
                self.textBrowser_2.insertPlainText(f"Linea: {str(lines)} | Info: {str(gram)} \n")

    # Funcion para realizar el analisis lexico
    def lexer(self):
        self.textBrowser_2.setText("")
        texto = self.textEdit.toPlainText()
        listaTokens = lex.analizadorLexico(texto)
        for elem in listaTokens:
            self.textBrowser_2.insertPlainText(str(elem)+"\n")
        listaTokens.clear()
    #Funcion para limpiar caja de texto
    def clear(self):
        self.textEdit.setText("")
        self.textBrowser_2.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Dart Syntax and lexer"))
        self.label_2.setText(_translate("MainWindow", "Input"))
        self.label_3.setText(_translate("MainWindow", "Output"))
        self.pushButton.setText(_translate("MainWindow", "Syntax"))
        self.pushButton_2.setText(_translate("MainWindow", "Lexer"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())