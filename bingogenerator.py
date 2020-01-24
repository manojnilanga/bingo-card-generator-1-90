# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt-bingo.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageDraw, ImageFont
import random


class Ui_Bingo(object):
    def setupUi(self, Bingo):
        Bingo.setFixedSize(395,187)
        Bingo.setObjectName("Bingo")
        Bingo.resize(398, 190)
        self.centralwidget = QtWidgets.QWidget(Bingo)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 100, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.generateCards)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(270, 30, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        Bingo.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Bingo)
        self.statusbar.setObjectName("statusbar")
        Bingo.setStatusBar(self.statusbar)

        self.retranslateUi(Bingo)
        QtCore.QMetaObject.connectSlotsByName(Bingo)

    def retranslateUi(self, Bingo):
        _translate = QtCore.QCoreApplication.translate
        Bingo.setWindowTitle(_translate("Bingo", "Bingo Card Generator"))
        self.label.setText(_translate("Bingo", "how many cards ?"))
        self.pushButton.setText(_translate("Bingo", "Generate"))
        self.textEdit.setHtml(_translate("Bingo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">10</span></p></body></html>"))

    def generateCards(self):
        
        font = ImageFont.truetype("arial.ttf", 18)
        pages = int(self.textEdit.toPlainText())

        for m in range(0,pages):
            print(m)
            bingopage=[]
            
            for i in range (0,6):
                height = 451
                width = 151
                image = Image.new(mode='L', size=(height, width), color=255)

                # Draw some lines
                draw = ImageDraw.Draw(image)
    
                y_start = 0
                y_end = image.height
                step_size = int(image.width / 9)

                for x in range(0, image.width, step_size):
                    line = ((x, y_start), (x, y_end))
                    draw.line(line, fill=128)

                x_start = 0
                x_end = image.width
                step_size = int(image.height / 3)

                for y in range(0, image.height, step_size):
                    line = ((x_start, y), (x_end, y))
                    draw.line(line, fill=128)

                del draw

                ran15 = random.sample(range(1, 90), 15)
                

                for j in range(0,3):
                    ran5=ran15[j*5:j*5+5]
                    ran5.append(-1)
                    ran5.append(-1)
                    ran5.append(-1)
                    ran5.append(-1)
                    random.shuffle(ran5)
                    
                    for k in range(0,9):
                        if(ran5[k]==-1):
                            continue
                        d =ImageDraw.Draw(image)
                        d.text((k*50+14,j*50+14),str(ran5[k]),font=font)

                bingopage.append(image)

            dst = Image.new(mode='L', size=(1050, 650), color=255)
            dst.paste(bingopage[0], (50, 50))
            dst.paste(bingopage[1], (550, 50))
            dst.paste(bingopage[2], (50, 250))
            dst.paste(bingopage[1], (550, 250))
            dst.paste(bingopage[0], (50, 450))
            dst.paste(bingopage[1], (550, 450))

            dst.save(str(m+1)+'.png')
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bingo = QtWidgets.QMainWindow()
    ui = Ui_Bingo()
    ui.setupUi(Bingo)
    Bingo.show()
    sys.exit(app.exec_())
