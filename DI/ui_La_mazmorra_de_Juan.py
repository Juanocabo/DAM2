# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'La_mazmorra_de_Juan.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 444)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(750, 444))
        MainWindow.setMaximumSize(QSize(750, 444))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.actionAyuda = QAction(MainWindow)
        self.actionAyuda.setObjectName(u"actionAyuda")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:1.443, fx:0.5, fy:0.5, stop:0 rgba(166, 166, 166, 255), stop:1 rgba(0, 0, 0, 255));")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-1, -1, 751, 401))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.horizontalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color:transparent;\n"
"border:solid 0px;")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(2)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, -4, 371, 401))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(12)
        self.gridLayout_2.setVerticalSpacing(24)
        self.gridLayout_2.setContentsMargins(14, 14, 14, 14)
        self.norte = QPushButton(self.layoutWidget)
        self.norte.setObjectName(u"norte")
        self.norte.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.norte.sizePolicy().hasHeightForWidth())
        self.norte.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setKerning(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.norte.setFont(font1)
        self.norte.setCursor(QCursor(Qt.PointingHandCursor))
        self.norte.setMouseTracking(False)
        self.norte.setAutoFillBackground(False)
        self.norte.setStyleSheet(u"background-color:rgb(209, 250, 255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:blue;")

        self.gridLayout_2.addWidget(self.norte, 0, 1, 1, 1)

        self.central = QPushButton(self.layoutWidget)
        self.central.setObjectName(u"central")
        self.central.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.central.sizePolicy().hasHeightForWidth())
        self.central.setSizePolicy(sizePolicy1)
        self.central.setFont(font1)
        self.central.setCursor(QCursor(Qt.PointingHandCursor))
        self.central.setMouseTracking(False)
        self.central.setAutoFillBackground(False)
        self.central.setStyleSheet(u"background-color:rgb(209, 250, 255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:blue;")

        self.gridLayout_2.addWidget(self.central, 1, 1, 1, 1)

        self.este = QPushButton(self.layoutWidget)
        self.este.setObjectName(u"este")
        self.este.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.este.sizePolicy().hasHeightForWidth())
        self.este.setSizePolicy(sizePolicy1)
        self.este.setFont(font1)
        self.este.setCursor(QCursor(Qt.PointingHandCursor))
        self.este.setMouseTracking(False)
        self.este.setAutoFillBackground(False)
        self.este.setStyleSheet(u"background-color:rgb(209, 250, 255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:blue;")

        self.gridLayout_2.addWidget(self.este, 1, 2, 1, 1)

        self.sur = QPushButton(self.layoutWidget)
        self.sur.setObjectName(u"sur")
        self.sur.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.sur.sizePolicy().hasHeightForWidth())
        self.sur.setSizePolicy(sizePolicy1)
        self.sur.setFont(font1)
        self.sur.setCursor(QCursor(Qt.PointingHandCursor))
        self.sur.setMouseTracking(False)
        self.sur.setAutoFillBackground(False)
        self.sur.setStyleSheet(u"background-color:rgb(209, 250, 255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:blue;")

        self.gridLayout_2.addWidget(self.sur, 2, 1, 1, 1)

        self.oeste = QPushButton(self.layoutWidget)
        self.oeste.setObjectName(u"oeste")
        self.oeste.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.oeste.sizePolicy().hasHeightForWidth())
        self.oeste.setSizePolicy(sizePolicy1)
        self.oeste.setBaseSize(QSize(50, 50))
        self.oeste.setFont(font1)
        self.oeste.setCursor(QCursor(Qt.PointingHandCursor))
        self.oeste.setMouseTracking(False)
        self.oeste.setAutoFillBackground(False)
        self.oeste.setStyleSheet(u"background-color:rgb(209, 250, 255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:blue;")

        self.gridLayout_2.addWidget(self.oeste, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.horizontalLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"background-color:transparent;\n"
"border:solid 0px;")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.jugar = QPushButton(self.frame_2)
        self.jugar.setObjectName(u"jugar")
        self.jugar.setGeometry(QRect(50, 330, 111, 51))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.jugar.setFont(font2)
        self.jugar.setCursor(QCursor(Qt.PointingHandCursor))
        self.jugar.setMouseTracking(False)
        self.jugar.setAutoFillBackground(False)
        self.jugar.setStyleSheet(u"background-color:rgb(209, 250, 255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:blue;")
        self.salir = QPushButton(self.frame_2)
        self.salir.setObjectName(u"salir")
        self.salir.setGeometry(QRect(210, 330, 111, 51))
        self.salir.setFont(font2)
        self.salir.setCursor(QCursor(Qt.PointingHandCursor))
        self.salir.setMouseTracking(False)
        self.salir.setAutoFillBackground(False)
        self.salir.setStyleSheet(u"background-color:rgb(209, 250, 255);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:blue;")
        self.verticalFrame = QFrame(self.frame_2)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setGeometry(QRect(50, 120, 271, 91))
        self.verticalFrame.setAutoFillBackground(False)
        self.verticalFrame.setStyleSheet(u"background-color:transparent")
        self.verticalFrame.setFrameShape(QFrame.Panel)
        self.verticalFrame.setFrameShadow(QFrame.Sunken)
        self.verticalFrame.setLineWidth(2)
        self.verticalFrame.setMidLineWidth(3)
        self.respuestas = QVBoxLayout(self.verticalFrame)
        self.respuestas.setObjectName(u"respuestas")
        self.r1 = QRadioButton(self.verticalFrame)
        self.r1.setObjectName(u"r1")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.r1.setFont(font3)
        self.r1.setStyleSheet(u"background-color:rgb(209, 250, 255)")

        self.respuestas.addWidget(self.r1)

        self.r2 = QRadioButton(self.verticalFrame)
        self.r2.setObjectName(u"r2")
        self.r2.setFont(font3)
        self.r2.setStyleSheet(u"background-color:rgb(209, 250, 255)")

        self.respuestas.addWidget(self.r2)

        self.r3 = QRadioButton(self.verticalFrame)
        self.r3.setObjectName(u"r3")
        self.r3.setFont(font3)
        self.r3.setStyleSheet(u"background-color:rgb(209, 250, 255)")

        self.respuestas.addWidget(self.r3)

        self.txtsala = QTextEdit(self.frame_2)
        self.txtsala.setObjectName(u"txtsala")
        self.txtsala.setEnabled(True)
        self.txtsala.setGeometry(QRect(50, 10, 271, 101))
        font4 = QFont()
        font4.setFamilies([u"Noto Sans Lao"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.txtsala.setFont(font4)
        self.txtsala.setAutoFillBackground(False)
        self.txtsala.setStyleSheet(u"background-color:rgb(209, 250, 255)")
        self.txtsala.setReadOnly(True)
        self.txtresultado = QTextEdit(self.frame_2)
        self.txtresultado.setObjectName(u"txtresultado")
        self.txtresultado.setEnabled(True)
        self.txtresultado.setGeometry(QRect(50, 220, 271, 101))
        self.txtresultado.setFont(font4)
        self.txtresultado.setAutoFillBackground(False)
        self.txtresultado.setStyleSheet(u"background-color:rgb(209, 250, 255)")
        self.txtresultado.setReadOnly(True)

        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 750, 22))
        self.menubar.setStyleSheet(u"background-color:rgb()")
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuMenu.setStyleSheet(u"background-color:rgb()")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionAyuda)
        self.menuMenu.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAyuda.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.norte.setText(QCoreApplication.translate("MainWindow", u"NORTE", None))
        self.central.setText(QCoreApplication.translate("MainWindow", u"CENTRAL", None))
        self.este.setText(QCoreApplication.translate("MainWindow", u"ESTE", None))
        self.sur.setText(QCoreApplication.translate("MainWindow", u"SUR", None))
        self.oeste.setText(QCoreApplication.translate("MainWindow", u"OESTE", None))
        self.jugar.setText(QCoreApplication.translate("MainWindow", u"JUGAR", None))
        self.salir.setText(QCoreApplication.translate("MainWindow", u"SALIR", None))
        self.r1.setText("")
        self.r2.setText("")
        self.r3.setText("")
        self.txtsala.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans Lao'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:700;\"><br /></p></body></html>", None))
        self.txtresultado.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans Lao'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:700;\"><br /></p></body></html>", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

