# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:52:54 2020

@author: mohamad
"""


from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import random
import time    
class MatplotlibWidget(QMainWindow):
    
    def __init__(self):
        
        QMainWindow.__init__(self)

        loadUi("dising.ui",self)

        self.setWindowTitle("Simulate Perceptron")
        self.setFixedSize(950,700)
        # self.pushButton_generate_random_signal.clicked.connect(self.update_graph)
        self.Ok.clicked.connect(self.update_graph)
        self.pushButton_clear.clicked.connect(self.Clear)
        self.pushButton_p.clicked.connect(self.Perceptron)
        self.pushButton_h.clicked.connect(self.heb)        

 
        
                
    def Clear(self):
        self.pushButton_p.setEnabled(False)
        self.pushButton_h.setEnabled(False)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.draw()
        
       
        
     
        
        
        
    def heb(self):
        self.pushButton_p.setEnabled(False)
        st_repet=int(self.repet.text())
        teta,w1,w2=0,0,0
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(self.x1[:,0],self.x1[:,1],'ro')
        self.MplWidget.canvas.axes.plot(self.x2[:,0],self.x2[:,1],'bo')
        for t in range(0, st_repet): 
            for i in range(0, len(self.x1)):
                y=1
                w1=w1+self.x1[i,0]*y;w2=w2 + self.x2[i,1]*y;teta=teta+y
            for j in range(0, len(self.x1)):
                y=-1
                w1=w1+self.x2[j,0]*y;w2=w2 + self.x2[j,1]*y;teta=teta+y  
            a=np.linspace(-5,5,100)
            m=-(w1/w2)
            c=teta/w2
            b=m*a+c
            self.MplWidget.canvas.axes.plot(a, b,label=('line',t))
            self.MplWidget.canvas.axes.legend()
            self.MplWidget.canvas.draw() 
        
        
        
    def Perceptron(self):
        st_repet=int(self.repet.text())
        self.pushButton_h.setEnabled(False)
        #print(sampel)
        w0,w1,w2=0.0,0.0,0.0
        sample=np.concatenate((self.x1,self.x2))
        a=1/np.average(sample)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(self.x1[:,0],self.x1[:,1],'ro')
        self.MplWidget.canvas.axes.plot(self.x2[:,0],self.x2[:,1],'bo')
        for i in range(0, st_repet): 
            for var in range(0, self.num):
                t=0
                I=w0+w1*self.x1[var,0]+self.x1[var,1]*w2
                if I >=0:
                    y=1
                else:y=0
                w0=w0+ a*(t-y);w1=w1+a*(t-y)*self.x1[var,0];w2=w2+a*(t-y)*self.x1[var,1]
            for j in range(0, self.num):
                t=1
                I=w0+w1*self.x2[var,0]+self.x2[var,1]*w2
                if I >=0:
                    y=1
                else:y=0
                w0=w0+ a*(t-y);w1=w1+a*(t-y)*self.x2[j,0];w2=w2+a*(t-y)*self.x2[j,1]
            test=np.random.randint(-5,5,100)
            m=-(w1/w2)
            c=-(w0/w2)
            b=m*test+c
            self.MplWidget.canvas.axes.plot(test, b,label=('line',i))
            self.MplWidget.canvas.axes.legend()
            self.MplWidget.canvas.draw()     
            

    def update_graph(self):
        A1=float(self.lineEdit_Ave_A1.text())
        A2=float(self.lineEdit_Ave_A2.text())
        B1=float(self.lineEdit_Ave_B1.text())
        B2=float(self.lineEdit_Ave_B2.text())
        A11=float(self.lineEdit_A11.text())
        A12=float(self.lineEdit_A12.text())
        A21=float(self.lineEdit_A21.text())
        A22=float(self.lineEdit_A22.text())
        B11=float(self.lineEdit_B11.text())
        B12=float(self.lineEdit_B12.text())
        B21=float(self.lineEdit_B21.text())
        B22=float(self.lineEdit_B22.text())
        self.num=int(self.number.text())
        M1=[A1,A2]
        M2=[B1,B2]
        sigma1=[[A11,A12],[A21,A22]]
        sigma2=[[B11,B12],[B21,B22]]
        self.x1=np.random.multivariate_normal(M1,sigma1,self.num)
        self.x2=np.random.multivariate_normal(M2,sigma2,self.num)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(self.x1[:,0],self.x1[:,1],'ro')
        self.MplWidget.canvas.axes.plot(self.x2[:,0],self.x2[:,1],'bo')
        self.pushButton_p.setEnabled(True)
        self.pushButton_h.setEnabled(True)
        self.MplWidget.canvas.draw()
        
if __name__=="__main__":
    
    app = QApplication([])
    window = MatplotlibWidget()
    window.show()
    app.exec_()