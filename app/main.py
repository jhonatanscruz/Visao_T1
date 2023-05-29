# -------------------- DESCRIÇÃO --------------------

#    AUTOR: JHONATAN DA SILVA CRUZ
#    DISCIPLINA: VISÃO COMPUTACIONAL [ UFES - 2023/01 ]
#    PROF.: RAQUEL FRIZERA VASSALLO
#    TRABALHO 1: MOVIMENTO DE CORPO RÍGIDO E PROJEÇÃO PINHOLE COM INTERFACE GRÁFICA

# ------------------------- \\ -----------------------

# -------------------- BIBLIOTECAS --------------------

import sys
import matplotlib
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import matplotlib.pyplot as plt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout)
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from math import pi,cos,sin

# ------------------------- \\ -------------------------

# ---------------------- CLASSES -----------------------

class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")

        self.button.clicked.connect(self.openSystem)

    def openSystem(self):
        if (self.getLogin.text() == "visao") and (self.getPass.text() == "2023-01"):
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            self.label_erro.setText("Usuário ou Senha incorretos!")

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, project=None):
        self.fig = plt.figure()
        self.axes = self.fig.add_subplot(111, projection=project)
        super(MplCanvas, self).__init__(self.fig)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setupUi(self)

        self.cam = Cam(Referencial())
        self.obj = Object(object())

        # 2D Parameters
        self.layout2D = QVBoxLayout()
        self.figure2D = MplCanvas()
        self.layout2D.addWidget(self.figure2D)

        # 3D Parameters
        self.layout3D = QVBoxLayout()
        self.figure3D = MplCanvas("3d")
        self.layout3D.addWidget(self.figure3D)

        self._2D_frame.setLayout(self.layout2D)
        self._3D_frame.setLayout(self.layout3D)
        self.setWindowTitle("Trabalho 01")

        # set RESET condition
        self.resetAlterar()
        self.resetTransform()

        # Button Events
        self.alterarOptions.clicked.connect(self.alterar)
        self.resetOptions.clicked.connect(self.resetAlterar)
        self.transformar.clicked.connect(self.transform)
        self.resetTransformar.clicked.connect(self.resetTransform)

    def alterar(self):
        if self.getDFocal.text() != "":
            self.cam.setdistFocal(int(self.getDFocal.text()))

        if self.getCCD_X.text() != "":
            self.cam.setCCDX(int(self.getCCD_X.text()))

        if self.getCCD_Y.text() != "":
            self.cam.setCCDY(int(self.getCCD_Y.text()))

        if self.getIMG_X.text() != "":
            self.cam.setIMGX(int(self.getIMG_X.text()))

        if self.getIMG_Y.text() != "":
            self.cam.setIMGY(int(self.getIMG_Y.text()))

        self.update2D()
        self.setAlterarBoxToBlank()

    def resetAlterar(self):
        self.cam.setdistFocal(10)
        self.cam.setCCDX(36)
        self.cam.setCCDY(24)
        self.cam.setIMGX(1280)
        self.cam.setIMGY(720)
        self.update2D()
        self.setAlterarBoxToBlank()

    def setAlterarBoxToBlank(self):
        self.getDFocal.setText("")
        self.getCCD_X.setText("")
        self.getCCD_Y.setText("")
        self.getIMG_X.setText("")
        self.getIMG_Y.setText("")

    def update2D(self):
        projection = self.cam._2D_object_projection(self.obj.object)
        self.figure2D.axes.clear()
        self.figure2D.axes.set_xlim([0,self.cam.getIMGX()])
        self.figure2D.axes.set_ylim([self.cam.getIMGY(),0])
        self.figure2D.axes.plot(projection[0,:],projection[1,:])
        self.figure2D.axes.grid('True')
        self.figure2D.axes.set_aspect('equal')
        self.figure2D.draw()
        self.figure2D.flush_events()

    def update3D(self):
        self.figure3D.axes.clear()
        self.figure3D.axes.set_xlim([-30,15])
        self.figure3D.axes.set_ylim([-15,15])
        self.figure3D.axes.set_zlim([-15,15])
        self.figure3D.axes.plot(self.obj.object[0,:],self.obj.object[1,:],self.obj.object[2,:])
        draw_arrows(self.cam.referencial.getCurrentPoint(),self.cam.referencial.getCurrentBase(),self.figure3D.axes)
        self.figure3D.axes.set_aspect('equal')
        self.figure3D.draw()
        self.figure3D.flush_events()

    def transform(self):
        if self.refCAM.isChecked() == True:
            refer = "self"
        else:
            refer = "world"

        if self.getRX.text() != "":
            self.cam.referencial.rotate("x",float(float(self.getRX.text())*pi/180),refer)

        if self.getRY.text() != "":
            self.cam.referencial.rotate("y",float(float(self.getRY.text())*pi/180),refer)

        if self.getRZ.text() != "":
            self.cam.referencial.rotate("z",float(float(self.getRZ.text())*pi/180),refer)

        if self.getTX.text() == "" and self.getTY.text() == "" and self.getTZ.text() == "":
            pass
        else:
            if self.getTX.text() == "":
                tx = 0
            else:
                tx = float(self.getTX.text())
            
            if self.getTY.text() == "":
                ty = 0
            else:
                ty = float(self.getTY.text())

            if self.getTZ.text() == "":
                tz = 0
            else:
                tz = float(self.getTZ.text())

            self.cam.referencial.transfer(createVector(tx,ty,tz),refer)

        self.update2D()
        self.update3D()
        self.setTransformBoxToBlank()

    def resetTransform(self):
        self.cam.referencial.fila = []
        self.cam.referencial.rotate("x",-pi/2,"world")
        self.cam.referencial.rotate("z",pi/2,"world")
        self.cam.referencial.transfer(createVector(15,-5,6),"world")
        self.update2D()
        self.update3D()
        self.setTransformBoxToBlank()

    def setTransformBoxToBlank(self):
        self.getRX.setText("")
        self.getRY.setText("")
        self.getRZ.setText("")
        self.getTX.setText("")
        self.getTY.setText("")
        self.getTZ.setText("")

class Referencial:
    def __init__(self):
        self.fila = []

        # base vector values
        e1 = np.array([[1],[0],[0],[0]]) # X
        e2 = np.array([[0],[1],[0],[0]]) # Y
        e3 = np.array([[0],[0],[1],[0]]) # Z
        self.base = np.hstack((e1,e2,e3))

    def tamanho(self):
        return len(self.fila)

    def enfileirar(self, elemento):
        self.fila.append(elemento)

    def desenfileirar(self):
        if self.tamanho() > 0:
            elemento_removido = self.fila[0]
            self.fila = self.fila[1:]
            return elemento_removido
        else:
            return None

    def transformation_matrice(self):
        base = np.eye(4)

        if self.tamanho() > 0:
            tm = base
            for m in self.fila:
                tm = np.dot(m,tm)
            return tm
        else:
            return base

    def getCurrentPoint(self):
        if self.tamanho() > 0:
            p = self.transformation_matrice()[:,3]
            return np.array([[p[0]],[p[1]],[p[2]],[p[3]]])
        else:
            return origem()

    def getCurrentBase(self):
        if self.tamanho() > 0:
            return self.transformation_matrice()[:,0:3]
        else:
            return self.base

    # Retorna as coordenadas em um novo referencial
    def changeReferential(self, newReferencial):
        tm = np.linalg.inv(newReferencial.transformation_matrice())
        p = np.dot(tm,self.getCurrentPoint())

        return p

    # Retorna a Matriz de translação para um deslocamento no Mundo ou no próprio Referencial
    def transfer(self,desloca,refer=None):
        if refer == "self":
            # Coordenadas, no referencial do mundo, do ponto para onde será deslocado
            tm = np.dot(self.transformation_matrice(), createPoint(desloca[0],desloca[1],desloca[2]))
            self.enfileirar(translation(self.getCurrentPoint(), tm))
        else:
            self.enfileirar(translation(self.getCurrentPoint(), self.getCurrentPoint()+desloca))

    def rotate(self, axis, angle, refer=None):
        if refer == "self":
            tm = self.transformation_matrice()
            inv = np.linalg.inv(tm)
            self.enfileirar(inv)
            if axis == "x" or axis == "X":
                self.enfileirar(x_rotation(angle))
            elif axis == "y" or axis == "Y":
                self.enfileirar(y_rotation(angle))
            elif axis == "z" or axis == "Z":
                self.enfileirar(z_rotation(angle))
            self.enfileirar(tm)

        else:
            if axis == "x" or axis == "X":
                self.enfileirar(x_rotation(angle))
            elif axis == "y" or axis == "Y":
                self.enfileirar(y_rotation(angle))
            elif axis == "z" or axis == "Z":
                self.enfileirar(z_rotation(angle))

class Cam:
    def __init__(self, referencial, distFocal=10, ccdX=36, ccdY=24, imgX=1280, imgY=720):
        self.referencial = referencial
        self.distFocal = distFocal
        self.ccdX = ccdX
        self.ccdY = ccdY
        self.imgX = imgX
        self.imgY = imgY

    def plotCam(self, ax):
        plot(self.referencial.transformation_matrice(),ax=ax) # Plota a camera na posição atual

    # GET FUNCTIONS
    def getReferencial(self):
        return self.referencial

    def getdistFocal(self):
        return self.distFocal

    def getCCDX(self):
        return self.ccdX

    def getCCDY(self):
        return self.ccdY

    def getIMGX(self):
        return self.imgX

    def getIMGY(self):
        return self.imgY

    # SET FUNCTIONS
    def setReferencial(self, ref):
        self.referencial = ref

    def setdistFocal(self, distFocal):
        self.distFocal = distFocal

    def setCCDX(self, ccdX):
        self.ccdX = ccdX

    def setCCDY(self, ccdY):
        self.ccdY = ccdY

    def setIMGX(self, imgX):
        self.imgX = imgX

    def setIMGY(self, imgY):
        self.imgY = imgY

    def _2D_object_projection(self, object):
        f       = self.distFocal
        sx      = self.imgX/self.ccdX
        sy      = self.imgY/self.ccdY
        s_theta = 0
        Ox      = self.imgX/2
        Oy      = self.imgY/2

        # Matriz de parametros intrinsecos
        Int = np.array([[f*sx, f*s_theta, Ox],[0, f*sy, Oy],[0, 0, 1]])
        # Matriz de parametros extrinsecos
        Ext = np.linalg.inv(self.referencial.transformation_matrice())
        # Matriz de projeção
        m = np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0]])
        # Projeção e criação da imagem
        _2D_projection = np.dot(Int, np.dot(np.dot(m, Ext),object))

        # Preparação das coordenadas na forma cartesiana
        _2D_projection[0,:] = _2D_projection[0,:] / _2D_projection[2,:]
        _2D_projection[1,:] = _2D_projection[1,:] / _2D_projection[2,:]
        _2D_projection[2,:] = _2D_projection[2,:] / _2D_projection[2,:]

        return _2D_projection

class Object:
    def __init__(self,object):
        self.object = np.vstack([np.transpose(object), np.ones(np.size(np.transpose(object),1))])

    def transformObject(self,transformation):
        self.object = np.dot(transformation,self.object)

    # PLOT OBJECT
    def plotObject(self,lim=None,color=None,ax=None):
        if color == None:
            color = 'red'
        if lim == None:
            lim = [-10,10]
        if ax == None:
            ax = set_plot(lim=lim)

        ax.plot3D(self.object[0,:], self.object[1,:], self.object[2,:], color)

# ------------------------- \\ -------------------------

# ------------------------- FUNÇÕES --------------------
def createPoint(px,py,pz):
        return np.array([[px],[py],[pz],[1]])

def origem():
    return createPoint(0,0,0)

def createVector(px,py,pz):
        return np.array([[px],[py],[pz],[0]])

# Definição da Matriz de Translação (Pontos na referência do mundo)
def translation(from_point, to_point):
    T = np.eye(4)
    T[:3,-1] = (to_point - from_point)[:3].T

    # Retorna a matriz de translação partindo do ponto "from_point" para o ponto "to_point"
    return T

# Definição das Matrizes de rotação em torno da origem
def z_rotation(angle):
    rotation_matrix=np.array([[cos(angle),-sin(angle),0,0],[sin(angle),cos(angle),0,0],[0,0,1,0],[0,0,0,1]])
    return rotation_matrix

def x_rotation(angle):
    rotation_matrix=np.array([[1,0,0,0],[0, cos(angle),-sin(angle),0],[0, sin(angle), cos(angle),0],[0,0,0,1]])
    return rotation_matrix

def y_rotation(angle):
    rotation_matrix=np.array([[cos(angle),0, sin(angle),0],[0,1,0,0],[-sin(angle), 0, cos(angle),0],[0,0,0,1]])
    return rotation_matrix

def set_plot(ax=None, figure = None, title = None, lim=[-2,2]):
    if figure == None:
        figure = plt.figure(figsize=(8,8))
    if ax == None:
        ax = plt.axes(projection='3d')
    if title == None:
        title = ""

    ax.set_title(title)
    ax.set_xlim(lim)
    ax.set_xlabel("x axis")
    ax.set_ylim(lim)
    ax.set_ylabel("y axis")
    ax.set_zlim(lim)
    ax.set_zlabel("z axis")
    return ax

# Adding quivers to the plot
def draw_arrows(point,base,axis,length=1.5):
    # The object base is a matrix, where each column represents the vector 
    # of one of the axis, written in homogeneous coordinates (ax,ay,az,0)

    # Plot vector of x-axis
    axis.quiver(point[0],point[1],point[2],base[0,0],base[1,0],base[2,0],color='red',pivot='tail', length=length)
    # Plot vector of y-axis
    axis.quiver(point[0],point[1],point[2],base[0,1],base[1,1],base[2,1],color='green',pivot='tail', length=length)
    # Plot vector of z-axis
    axis.quiver(point[0],point[1],point[2],base[0,2],base[1,2],base[2,2],color='blue',pivot='tail', length=length)

    return axis

# PLOT
def plot(matrice,lim=None,ax=None):
    if lim == None:
        lim = [-10,10]
    if ax == None:
        ax = set_plot(lim=lim)
    
    draw_arrows(matrice[:,3], matrice[:,0:3], ax)

# ------------------------- \\ -------------------------

# ------------------------- EXECUÇÃO -------------------------

def createHouse():
    house = np.array([[0,         0,         0],
            [0,  -10.0000,         0],
            [0, -10.0000,   12.0000],
            [0,  -10.4000,   11.5000],
            [0,   -5.0000,   16.0000],
            [0,         0,   12.0000],
            [0,    0.5000,   11.4000],
            [0,         0,   12.0000],
            [0,         0,         0],
    [-12.0000,         0,         0],
    [-12.0000,   -5.0000,         0],
    [-12.0000,  -10.0000,         0],
            [0,  -10.0000,         0],
            [0,  -10.0000,   12.0000],
    [-12.0000,  -10.0000,   12.0000],
    [-12.0000,         0,   12.0000],
            [0,         0,   12.0000],
            [0,  -10.0000,   12.0000],
            [0,  -10.5000,   11.4000],
    [-12.0000,  -10.5000,   11.4000],
    [-12.0000,  -10.0000,   12.0000],
    [-12.0000,   -5.0000,   16.0000],
            [0,   -5.0000,   16.0000],
            [0,    0.5000,   11.4000],
    [-12.0000,    0.5000,   11.4000],
    [-12.0000,         0,   12.0000],
    [-12.0000,   -5.0000,   16.0000],
    [-12.0000,  -10.0000,   12.0000],
    [-12.0000,  -10.0000,         0],
    [-12.0000,   -5.0000,         0],
    [-12.0000,         0,         0],
    [-12.0000,         0,   12.0000],
    [-12.0000,         0,         0]])

    house = np.transpose(house)

    #add a vector of ones to the house matrix to represent the house in homogeneous coordinates
    house = np.vstack([house, np.ones(np.size(house,1))])

    cam = Cam(Referencial())
    cam.referencial.rotate("x", -pi/2, "world")
    cam.referencial.rotate("z", pi/2, "world")
    cam.referencial.transfer(createVector(15,-5,6),"world")

    return cam._2D_object_projection(house)

def createHouse2():
    house = np.array([[0,         0,         0],
            [0,  -10.0000,         0],
            [0, -10.0000,   12.0000],
            [0,  -10.4000,   11.5000],
            [0,   -5.0000,   16.0000],
            [0,         0,   12.0000],
            [0,    0.5000,   11.4000],
            [0,         0,   12.0000],
            [0,         0,         0],
    [-12.0000,         0,         0],
    [-12.0000,   -5.0000,         0],
    [-12.0000,  -10.0000,         0],
            [0,  -10.0000,         0],
            [0,  -10.0000,   12.0000],
    [-12.0000,  -10.0000,   12.0000],
    [-12.0000,         0,   12.0000],
            [0,         0,   12.0000],
            [0,  -10.0000,   12.0000],
            [0,  -10.5000,   11.4000],
    [-12.0000,  -10.5000,   11.4000],
    [-12.0000,  -10.0000,   12.0000],
    [-12.0000,   -5.0000,   16.0000],
            [0,   -5.0000,   16.0000],
            [0,    0.5000,   11.4000],
    [-12.0000,    0.5000,   11.4000],
    [-12.0000,         0,   12.0000],
    [-12.0000,   -5.0000,   16.0000],
    [-12.0000,  -10.0000,   12.0000],
    [-12.0000,  -10.0000,         0],
    [-12.0000,   -5.0000,         0],
    [-12.0000,         0,         0],
    [-12.0000,         0,   12.0000],
    [-12.0000,         0,         0]])

    house = np.transpose(house)

    #add a vector of ones to the house matrix to represent the house in homogeneous coordinates
    house = np.vstack([house, np.ones(np.size(house,1))])

    cam = Cam(Referencial())
    cam.referencial.transfer(createVector(15,-5,6),"world")

    return cam._2D_object_projection(house)

def object():
    house = np.array([[0,         0,         0],
            [0,  -10.0000,         0],
            [0, -10.0000,   12.0000],
            [0,  -10.4000,   11.5000],
            [0,   -5.0000,   16.0000],
            [0,         0,   12.0000],
            [0,    0.5000,   11.4000],
            [0,         0,   12.0000],
            [0,         0,         0],
    [-12.0000,         0,         0],
    [-12.0000,   -5.0000,         0],
    [-12.0000,  -10.0000,         0],
            [0,  -10.0000,         0],
            [0,  -10.0000,   12.0000],
    [-12.0000,  -10.0000,   12.0000],
    [-12.0000,         0,   12.0000],
            [0,         0,   12.0000],
            [0,  -10.0000,   12.0000],
            [0,  -10.5000,   11.4000],
    [-12.0000,  -10.5000,   11.4000],
    [-12.0000,  -10.0000,   12.0000],
    [-12.0000,   -5.0000,   16.0000],
            [0,   -5.0000,   16.0000],
            [0,    0.5000,   11.4000],
    [-12.0000,    0.5000,   11.4000],
    [-12.0000,         0,   12.0000],
    [-12.0000,   -5.0000,   16.0000],
    [-12.0000,  -10.0000,   12.0000],
    [-12.0000,  -10.0000,         0],
    [-12.0000,   -5.0000,         0],
    [-12.0000,         0,         0],
    [-12.0000,         0,   12.0000],
    [-12.0000,         0,         0]])

    return house

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()