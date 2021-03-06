# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new-ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageDraw, ImageFont
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(620,220)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 223)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(34, 25, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(430, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(34, 75, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(270, 70, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 140, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.generateCards)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bingo Card Generator"))
        self.label.setText(_translate("MainWindow", "How many bingo cards?"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Company name"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ABC Example Company</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Generate "))

    def generateCards(self):

        variations = [[[[0, 0, -1, -1, 0, -1, 0, -1, 0], [0, 0, 0, -1, 0, -1, 0, -1, -1], [-1, -1, 0, 0, -1, 0, -1, 0, 0]], [[-1, -1, -1, 0, 0, 0, -1, 0, 0], [0, -1, -1, -1, 0, 0, 0, -1, 0], [-1, 0, 0, 0, -1, -1, -1, 0, 0]], [[0, -1, -1, 0, 0, -1, 0, 0, -1], [-1, 0, 0, 0, -1, -1, -1, 0, 0], [-1, -1, 0, 0, -1, 0, 0, 0, -1]], [[-1, -1, 0, 0, 0, 0, -1, -1, 0], [-1, 0, 0, -1, 0, 0, 0, -1, -1], [0, 0, -1, 0, -1, 0, -1, 0, -1]], [[0, -1, 0, -1, -1, -1, 0, 0, 0], [-1, 0, -1, 0, 0, -1, 0, -1, 0], [0, 0, -1, -1, 0, 0, 0, -1, -1]], [[0, 0, 0, -1, -1, 0, -1, -1, 0], [0, -1, 0, -1, -1, 0, 0, 0, -1], [-1, 0, -1, 0, 0, -1, -1, 0, 0]]], [[[0, -1, 0, 0, 0, 0, -1, -1, -1], [0, -1, 0, -1, 0, -1, 0, 0, -1], [-1, 0, -1, 0, -1, 0, 0, -1, 0]], [[-1, 0, 0, 0, 0, -1, -1, -1, 0], [-1, 0, -1, 0, 0, 0, 0, -1, -1], [0, 0, -1, 0, -1, -1, -1, 0, 0]], [[0, -1, 0, -1, -1, -1, 0, 0, 0], [0, 0, -1, -1, 0, 0, -1, -1, 0], [-1, 0, -1, 0, -1, 0, 0, -1, 0]], [[-1, 0, 0, -1, -1, -1, 0, 0, 0], [0, -1, -1, -1, 0, 0, 0, -1, 0], [-1, 0, 0, 0, 0, -1, -1, 0, -1]], [[-1, -1, 0, 0, -1, 0, -1, 0, 0], [0, 0, 0, -1, -1, 0, -1, 0, -1], [-1, -1, -1, 0, 0, 0, 0, 0, -1]], [[0, -1, 0, -1, 0, 0, 0, -1, -1], [-1, -1, -1, 0, 0, -1, 0, 0, 0], [0, 0, 0, -1, -1, -1, -1, 0, 0]]], [[[-1, 0, 0, -1, 0, -1, -1, 0, 0], [0, 0, -1, -1, -1, -1, 0, 0, 0], [0, -1, -1, 0, -1, 0, 0, -1, 0]], [[-1, -1, 0, -1, 0, -1, 0, 0, 0], [0, 0, 0, 0, -1, 0, -1, -1, -1], [-1, 0, -1, -1, 0, 0, 0, -1, 0]], [[0, -1, 0, -1, 0, -1, 0, 0, -1], [-1, 0, -1, 0, -1, 0, -1, 0, 0], [0, 0, -1, 0, -1, -1, 0, -1, 0]], [[-1, 0, -1, 0, -1, 0, 0, 0, -1], [-1, -1, 0, 0, 0, 0, 0, -1, -1], [0, -1, 0, -1, -1, 0, -1, 0, 0]], [[-1, -1, 0, 0, 0, -1, -1, 0, 0], [0, 0, 0, -1, 0, -1, 0, -1, -1], [0, 0, 0, -1, -1, 0, -1, 0, -1]], [[-1, 0, -1, 0, 0, -1, 0, 0, -1], [-1, -1, 0, 0, 0, 0, -1, -1, 0], [0, -1, -1, 0, 0, 0, -1, -1, 0]]], [[[-1, 0, 0, -1, 0, -1, -1, 0, 0], [-1, 0, 0, -1, 0, -1, 0, -1, 0], [0, -1, -1, 0, -1, 0, -1, 0, 0]], [[0, -1, 0, -1, 0, 0, -1, -1, 0], [-1, 0, 0, 0, -1, 0, 0, -1, -1], [-1, 0, -1, 0, 0, -1, 0, 0, -1]], [[-1, -1, -1, -1, 0, 0, 0, 0, 0], [0, -1, 0, 0, -1, -1, 0, -1, 0], [0, 0, 0, 0, -1, -1, -1, 0, -1]], [[-1, 0, 0, 0, -1, 0, -1, -1, 0], [0, -1, -1, 0, 0, 0, -1, -1, 0], [-1, 0, -1, -1, 0, 0, 0, 0, -1]], [[-1, 0, 0, -1, 0, -1, 0, -1, 0], [0, -1, -1, -1, 0, 0, -1, 0, 0], [-1, 0, -1, 0, -1, 0, 0, 0, -1]], [[0, 0, 0, 0, -1, -1, 0, -1, -1], [0, -1, -1, 0, 0, 0, -1, 0, -1], [0, -1, 0, -1, -1, -1, 0, 0, 0]]], [[[0, -1, -1, 0, 0, 0, -1, 0, -1], [-1, -1, -1, -1, 0, 0, 0, 0, 0], [-1, 0, 0, 0, 0, -1, 0, -1, -1]], [[-1, 0, -1, 0, -1, 0, 0, 0, -1], [0, 0, -1, -1, 0, -1, -1, 0, 0], [-1, 0, 0, 0, -1, -1, 0, 0, -1]], [[0, 0, -1, 0, -1, 0, 0, -1, -1], [0, 0, 0, -1, 0, -1, -1, -1, 0], [0, -1, 0, -1, -1, 0, -1, 0, 0]], [[-1, 0, -1, 0, -1, 0, 0, -1, 0], [-1, 0, 0, -1, 0, -1, -1, 0, 0], [0, -1, 0, -1, 0, 0, 0, -1, -1]], [[0, -1, 0, -1, -1, 0, -1, 0, 0], [-1, -1, 0, 0, 0, -1, 0, 0, -1], [-1, 0, -1, 0, -1, 0, 0, -1, 0]], [[-1, -1, -1, -1, 0, 0, 0, 0, 0], [0, 0, 0, 0, -1, -1, -1, -1, 0], [0, -1, 0, 0, 0, -1, -1, -1, 0]]], [[[-1, -1, -1, 0, 0, 0, -1, 0, 0], [0, 0, -1, -1, -1, 0, 0, 0, -1], [-1, 0, 0, 0, 0, -1, 0, -1, -1]], [[-1, 0, 0, -1, 0, -1, 0, -1, 0], [0, -1, -1, 0, 0, -1, -1, 0, 0], [-1, 0, 0, -1, -1, 0, -1, 0, 0]], [[0, 0, 0, 0, 0, -1, -1, -1, -1], [0, -1, 0, -1, 0, 0, 0, -1, -1], [0, 0, 0, -1, -1, -1, -1, 0, 0]], [[-1, -1, 0, -1, 0, -1, 0, 0, 0], [-1, 0, -1, 0, -1, 0, -1, 0, 0], [0, -1, -1, -1, -1, 0, 0, 0, 0]], [[-1, 0, -1, -1, 0, 0, 0, -1, 0], [-1, 0, 0, 0, -1, 0, 0, -1, -1], [0, -1, -1, 0, -1, 0, -1, 0, 0]], [[0, -1, 0, 0, 0, -1, 0, -1, -1], [0, 0, -1, 0, -1, 0, -1, 0, -1], [-1, -1, 0, 0, 0, -1, 0, -1, 0]]], [[[0, -1, -1, -1, 0, 0, 0, 0, -1], [-1, -1, -1, 0, 0, 0, 0, -1, 0], [-1, 0, 0, -1, -1, 0, -1, 0, 0]], [[-1, 0, 0, 0, 0, -1, 0, -1, -1], [0, -1, 0, -1, -1, 0, -1, 0, 0], [-1, 0, -1, -1, -1, 0, 0, 0, 0]], [[-1, 0, 0, 0, -1, -1, -1, 0, 0], [0, -1, 0, -1, 0, 0, -1, -1, 0], [0, 0, -1, -1, -1, -1, 0, 0, 0]], [[-1, 0, -1, -1, 0, 0, 0, -1, 0], [0, 0, -1, 0, -1, -1, 0, -1, 0], [-1, 0, 0, -1, 0, 0, -1, 0, -1]], [[0, -1, 0, 0, -1, -1, -1, 0, 0], [0, -1, 0, 0, 0, 0, -1, -1, -1], [0, 0, -1, 0, 0, -1, 0, -1, -1]], [[0, -1, 0, 0, 0, -1, -1, 0, -1], [-1, -1, -1, 0, 0, 0, 0, 0, -1], [-1, 0, 0, 0, -1, -1, 0, -1, 0]]], [[[0, -1, -1, 0, -1, -1, 0, 0, 0], [-1, 0, 0, 0, -1, 0, -1, -1, 0], [-1, -1, 0, 0, 0, 0, 0, -1, -1]], [[0, -1, -1, -1, 0, 0, -1, 0, 0], [-1, 0, -1, 0, 0, 0, -1, 0, -1], [-1, 0, 0, 0, -1, -1, 0, -1, 0]], [[0, 0, -1, -1, 0, -1, 0, 0, -1], [-1, 0, 0, -1, -1, -1, 0, 0, 0], [-1, -1, -1, 0, 0, 0, -1, 0, 0]], [[-1, 0, 0, 0, -1, -1, 0, -1, 0], [-1, -1, 0, 0, 0, -1, 0, -1, 0], [0, 0, 0, -1, -1, 0, -1, 0, -1]], [[0, -1, 0, -1, 0, -1, 0, -1, 0], [0, 0, -1, -1, 0, 0, -1, 0, -1], [0, -1, 0, 0, 0, -1, -1, 0, -1]], [[0, 0, -1, -1, -1, 0, -1, 0, 0], [-1, 0, -1, 0, -1, 0, 0, -1, 0], [0, -1, 0, -1, 0, 0, 0, -1, -1]]], [[[0, -1, -1, -1, 0, 0, 0, 0, -1], [0, 0, -1, 0, -1, -1, 0, 0, -1], [0, -1, 0, -1, -1, -1, 0, 0, 0]], [[-1, 0, -1, 0, -1, 0, 0, -1, 0], [0, 0, 0, 0, -1, 0, -1, -1, -1], [0, -1, -1, -1, 0, 0, -1, 0, 0]], [[-1, -1, -1, 0, -1, 0, 0, 0, 0], [-1, 0, 0, 0, 0, -1, -1, 0, -1], [0, 0, 0, -1, -1, -1, 0, -1, 0]], [[-1, 0, 0, 0, 0, -1, -1, 0, -1], [0, -1, 0, 0, -1, 0, -1, -1, 0], [-1, 0, 0, -1, 0, 0, 0, -1, -1]], [[0, -1, -1, 0, 0, -1, -1, 0, 0], [-1, 0, -1, 0, 0, -1, 0, -1, 0], [-1, 0, 0, -1, 0, 0, 0, -1, -1]], [[0, -1, 0, 0, 0, -1, -1, -1, 0], [-1, -1, 0, -1, -1, 0, 0, 0, 0], [-1, 0, -1, -1, 0, 0, -1, 0, 0]]], [[[0, -1, -1, 0, -1, 0, 0, 0, -1], [0, 0, 0, 0, -1, -1, -1, -1, 0], [0, -1, -1, 0, 0, 0, 0, -1, -1]], [[-1, 0, 0, 0, -1, -1, -1, 0, 0], [0, -1, -1, -1, 0, 0, 0, -1, 0], [-1, 0, 0, -1, -1, -1, 0, 0, 0]], [[-1, -1, 0, 0, -1, -1, 0, 0, 0], [-1, 0, -1, -1, 0, 0, 0, 0, -1], [0, -1, 0, -1, 0, 0, -1, 0, -1]], [[-1, 0, 0, -1, 0, -1, -1, 0, 0], [0, 0, -1, -1, -1, 0, 0, -1, 0], [-1, -1, -1, 0, 0, 0, -1, 0, 0]], [[0, 0, 0, 0, -1, -1, 0, -1, -1], [-1, -1, -1, 0, -1, 0, 0, 0, 0], [0, 0, -1, 0, 0, 0, -1, -1, -1]], [[0, -1, 0, -1, 0, -1, 0, -1, 0], [-1, 0, 0, 0, 0, 0, -1, -1, -1], [-1, 0, 0, -1, 0, -1, -1, 0, 0]]]]

        font = ImageFont.truetype("arial.ttf", 18)
        font_company = ImageFont.truetype("arial.ttf", 11)
        pages = int(self.textEdit.toPlainText())

        for m in range(0,pages):
            bingopage=[]

            full_image = variations[random.randint(0,len(variations)-1)]
            random.shuffle(full_image)

            for i in range(0,9):
                col = []
                if(i==0):
                    for n in range(1,10):
                        col.append(n)
                elif(i==8):
                    for n in range(80,91):
                        col.append(n)
                else:
                    for n in range(i*10,i*10+10):
                        col.append(n)
                random.shuffle(col)
                #print(col)
                for j in range (0,6):
                    count=0
                    for k in range(0,3):
                        if(full_image[j][k][i]==0):
                            count+=1
                    ordered = col[:count]
                    col=col[count:]
                    ordered.sort()
                    for k in range(0,3):
                        if(full_image[j][k][i]==0):
                            full_image[j][k][i]=ordered[0]
                            ordered=ordered[1:]
            
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

                # ran15 = random.sample(range(1, 90), 15)
                # print(ran15)

                # for j in range(0,3):
                #     ran5=ran15[j*5:j*5+5]
                #     ran5.append(-1)
                #     ran5.append(-1)
                #     ran5.append(-1)
                #     ran5.append(-1)
                #     random.shuffle(ran5)
                #     print(ran5)
                #     for k in range(0,9):
                #         if(ran5[k]==-1):
                #             continue
                #         d =ImageDraw.Draw(image)
                #         d.text((k*50+14,j*50+14),str(ran5[k]),font=font)

                # ran27 = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

                # for i in range(0,3):
                #     spaces = random.sample(range(0, 9), 4)
                #     for j in range(0, 4):
                #         ran27[i][spaces[j]] =-1


                # for i in range(0,9):
                #     count = 0
                #     for j in range(0,3):
                #         if(ran27[j][i]==0):
                #             count = count+1
                #     if(i==0):
                #         col = random.sample(range(1,10), count)
                #     elif(i==8):
                #         col = random.sample(range(80,91), count)
                #     else:
                #         col = random.sample(range(i*10,i*10+10 ), count)
                #     col.sort()
                #     k=0
                #     skip=0
                #     while(k!=len(col)):
                #         if(ran27[k+skip][i]==0):
                #             ran27[k+skip][i]=col[k]
                #             k=k+1
                
                #         else:
                #             skip=skip+1
                ran27 = full_image[i]

                for j in range(0,3):
                    ran5=ran27[j]
                    
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
            dst.paste(bingopage[3], (550, 250))
            dst.paste(bingopage[4], (50, 450))
            dst.paste(bingopage[5], (550, 450))

            #writing the name
            text = self.textEdit_2.toPlainText()
            #text = ""
            named = ImageDraw.Draw(dst)
            named.text((150,220),text,font=font_company)
            named.text((650,220),text,font=font_company)
            named.text((150,420),text,font=font_company)
            named.text((650,420),text,font=font_company)
            named.text((150,620),text,font=font_company)
            named.text((650,620),text,font=font_company)

            dst.save(str(m+1)+'.png')




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bingo = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Bingo)
    Bingo.show()
    sys.exit(app.exec_())
