import sys

from lamazmorradeJuan import Ui_MainWindow
from PyQt6 import QtGui
from PyQt6.QtWidgets import (QApplication, QWidget, QMessageBox, QMainWindow, QDialog)
import random as rd

class MainWindow(QMainWindow):

    preguntas=[("¿Cuál es el río más largo de España?","Ebro"),
("¿Cuál es el río más largo de la península ibérica? ","Tajo"),
("¿Cuál es el río más largo del mundo?","Amazonas"),
("¿Cuál es la montaña más alta de España?","Teide"),("¿Cuál es la montaña más alta del mundo?","Everest"),
("¿Cuál es el océano más grande?","Pacífico"),("¿Cuál es el país con más extensión?","Rusia"),
("¿Cuál es el país más poblado?","India")]
    acertijos=[("Hay algo que, aunque te pertenezca, la gente siempre lo utiliza más que tú. ¿Qué es?","tu nombre"),
("Crezco a pesar de no estar vivo. No tengo pulmones, pero para vivir necesito el aire. El agua, aunque no tenga boca, me mata. ¿Qué soy?","el fuego"),
("Estando roto es más útil que sin romperse. ¿Qué es?","el huevo"),("Aparato que vibra y gira, te metes en la boca unas 3 veces al día y mide unos 15 cm. ¿Qué es?","un cepillo electrico"),
("Las personas siempre duermen menos en un mes del año. ¿Cuál es este mes?","febrero"),("Estoy en todo pese a estar en nada. ¿Qué soy?","letra d"),
("Te paras cuando está verde y continúas cuando está rojo. ¿Qué es?","sandia"),("¿Qué monte era el más alto del mundo antes de descubrir el Everest?","everest"),
("La señora y el señor Sánchez tienen 6 hijos. Cada hijo tiene una hermana. ¿Cuántas personas hay en la familia Sánchez?","9"),
("Soy alto siendo joven y corto cuando soy viejo. Resplandezco con la vida y el viento es mi mayor enemigo. ¿Qué soy?","vela")]
    sala ="central"
    isNorte = False
    isSur = False

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initializeUI()
        self.show()

    def initializeUI(self):
        self.ui.txtsala.setText("Te encuentras en la sala central de la MAZMORRA DE JUAN")
        self.ui.r1.setText("")
        self.ui.r2.setText("")
        self.ui.r3.setText("")
        self.ui.salir.clicked.connect(self.salir)
        self.ui.salir.setEnabled(False)
        self.ui.actionSalir.triggered.connect(self.exit)
        self.ui.actionAyuda.triggered.connect(self.ayudaPopUp)
        self.ui.jugar.clicked.connect(self.habilitar)
        self.ui.norte.clicked.connect(lambda x : self.navegar("n"))
        self.ui.sur.clicked.connect(lambda x : self.navegar("s"))
        self.ui.este.clicked.connect(lambda x : self.navegar("e"))
        self.ui.oeste.clicked.connect(lambda x : self.navegar("o"))
        self.ui.central.clicked.connect(lambda x : self.navegar("c"))
        self.deshabilitar()    

    def salir(self):
        if(self.sala != "central"):
            self.navegar("c")


    def habilitar(self):
            if(self.sala == "central"):
                self.ui.frame.setEnabled(True)
                self.ui.jugar.setEnabled(False)
                self.ui.central.setStyleSheet('QPushButton {background-color: #bd91fa;border: 1px solid  #6902f7;}')
            elif(self.sala =="este"):
                self.inEste()
            elif(self.isNorte):
                self.contra()
            elif(self.sala == "norte"):
                self.inNorte()
            elif(self.isSur):
                self.responder(self.sala)
            elif(self.sala == "sur"):
                self.inSur()
            elif(self.sala == "oeste"):
                self.inOeste()
            

    def deshabilitar(self):
            self.ui.verticalFrame.setEnabled(False)
            self.ui.frame.setEnabled(False) 

    def exit(self):
            sys.exit(app.exec())

    def volverCentral(self):
            self.sala = "central"

    def navegar(self, rumbo):
            self.quitarStilos()
            if rumbo == "n":
                self.ui.salir.setEnabled(True)
                self.ui.jugar.setEnabled(True)
                self.deshabilitar()
                self.sala = "norte"
                self.ui.txtsala.setText("Oh no! Parece que has encontrado a un enemigo bastante enfadado que quiere atacarte!!!")
                self.ui.norte.setStyleSheet('QPushButton {background-color: #bd91fa;border: 1px solid  #6902f7;}')
            
            elif rumbo == "s":
                self.ui.salir.setEnabled(True)
                self.ui.jugar.setEnabled(True)
                self.deshabilitar()
                self.sala = "sur"
                self.ui.txtsala.setText("Tendras que resolver el acertijo que te contare ahora...")
                self.ui.sur.setStyleSheet('QPushButton {background-color: #bd91fa;border: 1px solid  #6902f7;}')
            
            elif rumbo == "e":
                self.ui.salir.setEnabled(True)
                self.ui.jugar.setEnabled(True)
                self.deshabilitar()
                self.sala = "este"
                self.ui.txtsala.setText("Parece ser que ante ti se haya un tesoro sin igual, el que solo con fortuna abrirlo lograrás")
                self.ui.este.setStyleSheet('QPushButton {background-color: #bd91fa;border: 1px solid  #6902f7;}') 
                
                
            elif rumbo == "o":
                self.ui.salir.setEnabled(True)
                self.ui.jugar.setEnabled(True)
                self.deshabilitar()
                self.sala = "oeste"
                self.ui.txtsala.setText("Tendras que resolver la pregunta que te contare ahora...")
                self.ui.oeste.setStyleSheet('QPushButton {background-color: #bd91fa;border: 1px solid  #6902f7;}')
                
            else:
                self.ui.salir.setEnabled(False)
                self.ui.verticalFrame.setEnabled(False)
                self.ui.r1.setText("")
                self.ui.r2.setText("")
                self.ui.r3.setText("")
                self.sala = "central"
                self.habilitar()
                self.ui.central.setStyleSheet('QPushButton {background-color: #bd91fa;border: 1px solid  #6902f7;}')
                self.inCentral()

            

    def quitarStilos(self):
            ##self.ui.txtresultado.setText("")
            self.ui.norte.setStyleSheet('background-color:rgb(209, 250, 255);border-style:solid;border-width:1px;border-color:blue;')
            self.ui.sur.setStyleSheet('background-color:rgb(209, 250, 255);border-style:solid;border-width:1px;border-color:blue;')
            self.ui.este.setStyleSheet('background-color:rgb(209, 250, 255);border-style:solid;border-width:1px;border-color:blue;')
            self.ui.oeste.setStyleSheet('background-color:rgb(209, 250, 255);border-style:solid;border-width:1px;border-color:blue;')
            self.ui.central.setStyleSheet('background-color:rgb(209, 250, 255);border-style:solid;border-width:1px;border-color:blue;')

    def inNorte(self):
            self.isNorte = True
            daño=0
            
            self.ui.jugar.setText("Contraatacar")
            self.ui.salir.setText("Huir")
            daño=rd.randint(0,100)
            resu = "El ataque enemigo ha sido de: "+str(daño)
            if(daño<90):
                resu +=" Quieres contraatacar?"
            if(daño>=90):
                resu += " Has muerto \n Vuelves a la sala Central"
                self.ui.jugar.setText("Jugar")
                self.ui.salir.setText("Salir")
                self.navegar("c")
            self.ui.txtsala.setText(resu)

    def contra(self):
            self.ataque=rd.randint(0,100)
            resu = ("Tu contraataque ha sido de: "+str(self.ataque))
            
            if(self.ataque>=60):
                resu += " Enhorabuena has acabado con el enemigo \n Vuelves a la sala Central"
                self.ui.txtresultado.setText(resu)
                self.isNorte = False
                self.ui.jugar.setText("Jugar")
                self.ui.salir.setText("Salir")
                self.ui.norte.setEnabled(False)
                self.navegar("c")
            else:
                self.ui.txtresultado.setText(resu)
                self.inNorte()

            
    def inSur(self):
        self.ui.verticalFrame.setEnabled(True)
        self.isSur = True
        random = rd.randint(0,len(self.acertijos)-1)
        self.pregunta = self.acertijos[random][0]
        self.respuesta = self.acertijos[random][1]
        inco1 = self.acertijos[rd.randint(0,len(self.acertijos)-1)][1]
        inco2 = self.acertijos[rd.randint(0,len(self.acertijos)-1)][1]
        answers = [self.respuesta,inco1,inco2]
        answers = sorted(answers)
        self.ui.txtsala.setText(self.pregunta)
        self.ui.r1.setText(answers[0])
        self.ui.r2.setText(answers[1])
        self.ui.r3.setText(answers[2])

    def responder(self,sa):
        if(self.ui.r1.isChecked() and self.ui.r1.text()==self.respuesta):
            self.ui.txtresultado.setText("HAS ACERTADO \n Vuelves a la sala Central")
            if(sa=="sur"):
                self.ui.sur.setEnabled(False)
            else:
                self.ui.oeste.setEnabled(False)
            self.isSur = False
            self.navegar("c")
        elif(self.ui.r2.isChecked() and self.ui.r2.text()==self.respuesta):
            self.ui.txtresultado.setText("HAS ACERTADO \n Vuelves a la sala Central")
            if(sa=="sur"):
                self.ui.sur.setEnabled(False)
            else:
                self.ui.oeste.setEnabled(False)
            self.isSur = False
            self.navegar("c")
        elif(self.ui.r3.isChecked() and self.ui.r3.text()==self.respuesta):
            self.ui.txtresultado.setText("HAS ACERTADO \n Vuelves a la sala Central")
            if(sa=="sur"):
                self.ui.sur.setEnabled(False)
            else:
                self.ui.oeste.setEnabled(False)
            self.isSur = False
            self.navegar("c")
        else:
            self.ui.txtresultado.setText("HAS FALLADO, cambia tu respuesta")


    def inEste(self):
            num=0
            resu = ""
            num = rd.randint(0,101)
            resu = ("numero sacado: " + str(num))
            if(num<=63):
                resu =  resu+(" Parece que no es tu dia...")
                self.ui.txtresultado.setText(resu)
            else: 
                resu +=   " Lo has abiertoo!! \n Vuelves a la sala Central"
                self.ui.txtresultado.setText(resu)
                self.ui.este.setEnabled(False)
                self.navegar("c")
                    
    def inOeste(self):
            self.ui.verticalFrame.setEnabled(True)
            self.isSur = True
            random = rd.randint(0,len(self.preguntas)-1)
            self.pregunta = self.preguntas[random][0]
            self.respuesta = self.preguntas[random][1]
            inco1 = self.preguntas[rd.randint(0,len(self.preguntas)-1)][1]
            inco2 = self.preguntas[rd.randint(0,len(self.preguntas)-1)][1]
            answers = [self.respuesta,inco1,inco2]
            answers = sorted(answers)
            self.ui.txtsala.setText(self.pregunta)
            self.ui.r1.setText(answers[0])
            self.ui.r2.setText(answers[1])
            self.ui.r3.setText(answers[2])
    
    def inCentral(self):
            self.sala = "central"
            if(self.ui.norte.isEnabled() or self.ui.sur.isEnabled() or self.ui.este.isEnabled() or self.ui.oeste.isEnabled()):
                self.ui.txtsala.setText("Te encuentras en la sala central de la MAZMORRA DE JUAN")
            else:
                self.ui.txtsala.setText("HAS COMPLETADO LA MAZMORRA DE JUAN")
                self.ui.txtsala.setGeometry(250,150,271, 101)
                font = QtGui.QFont()
                font.setFamily("Noto Sans Lao")
                font.setPointSize(18)
                font.setBold(True)
                self.ui.txtsala.setFont(font)
                self.ui.frame.setVisible(False)
                self.ui.verticalFrame.setVisible(False)
                self.ui.jugar.setVisible(False)
                self.ui.salir.setVisible(False)
                self.ui.txtresultado.setVisible(False)
                self.ui.txtsala.setVisible(True)
                self.ui.horizontalLayoutWidget.setStyleSheet("background-color:white")
                self.ui.txtresultado.setText("")

    def ayudaPopUp(self):
        QMessageBox.information(self, "Ayuda", 
                    "Para empezar a jugar deberas darle a jugar en el segundo panel,"+
                    " una vez decidas a que sala viajar, te explicara de que ira la sala y para empezar a jugarla"+
                    " deberas volver a darle al boton de jugar,"+
                    " en cualquier momento dentro de una sala, si le das al boton de salir saldras a la sala central,"+
                    " si lo haces dentro de la sala central se cerrara la ventana."+
                    " La sala en la que te encuentras estara de color verde,"+
                    " mientras que las que hayas completado yo estaran deshabilitadas", QMessageBox.StandardButton.Ok, 
                    QMessageBox.StandardButton.Ok)

if __name__ == "__main__":
        app = QApplication(sys.argv)
        Keypad = MainWindow()
        sys.exit(app.exec())