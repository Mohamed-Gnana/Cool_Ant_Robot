from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
def circle (n1,n2,r1,r2,sh1,sh2):
    for theta in np.arange(n1,n2,0.01):
        x=(r1*cos(theta))+sh1
        y=(r2*sin(theta))+sh2
        glVertex2d(x,y)
def square (x1,y1,x2,y2,x3,y3,x4,y4):
    glVertex2d(x1,y1)
    glVertex2d(x2,y2)
    glVertex2d(x3,y3)
    glVertex2d(x4,y4)
def triangle (x1,y1,x2,y2,x3,y3):
    glVertex2d(x1,y1)
    glVertex2d(x2,y2)
    glVertex2d(x3,y3)
def coolRobot():
    glClearColor(0,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON) #Body
    glColor(0.9764705882352941,0.7294117647058824,0.0549019607843137)
    circle(0,2*pi,0.5,0.7,0,0)
    glEnd()
    glBegin(GL_POLYGON)
    R1=0.8588235294117647
    G1=0.4901960784313725
    B1=0.003921568627451
    n=0.6
    m=0.8
    for i in range(10):
        n=n-0.05
        m=m-0.07
        glColor(R1,G1,B1)
        circle(0,2*pi,n,m,0,0)
        R1=R1-0.0352941176470588
        G1=G1+0.0117647058823529
        B1=B1+0.0705882352941176
    glEnd()
    glBegin(GL_POINTS)
    glColor(0,0,0)
    n=0.5
    m=0.7
    for i in range(10):
        n=n-0.05
        m=m-0.07
        circle(0,2*pi,n,m,0,0)
    glEnd()
    #cutting####################################
    glBegin(GL_POLYGON) #cutting Body
    glColor(0,1,1)
    circle(0,2*pi,0.5,0.7,0,1.1)
    glEnd()
    glBegin(GL_POLYGON) #upper hands
    glColor(0,1,1)
    circle(0,2*pi,0.06,0.06,0.4,0.4)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,1,1)
    circle(0,2*pi,0.06,0.06,-0.4,0.4)
    glEnd()
    glBegin(GL_POLYGON) #lower legs
    glColor(0,1,1)
    circle(0,2*pi,0.06,0.06,0.4,-0.4)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,1,1)
    circle(0,2*pi,0.06,0.06,-0.4,-0.4)
    glEnd()
    glBegin(GL_POLYGON) #central hands
    glColor(0,1,1)
    circle(0,2*pi,0.06,0.06,0.5,0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,1,1)
    circle(0,2*pi,0.06,0.06,-0.5,0)
    glEnd()
    glBegin(GL_POLYGON) #legs
    glColor(0,1,1)
    circle(0,2*pi,0.06,0.06,0.185,-0.65)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,1,1)
    circle(0,2*pi,0.06,0.06,-0.185,-0.65)
    glEnd()
  #####################################################
    glBegin(GL_POLYGON)#HEAD
    glColor(0.8313725490196078,0.007843137254902,0.007843137254902)
    square (-0.2,.9,0.2,0.9,0.2,0.6,-0.2,0.6)
    glEnd()
    glBegin(GL_POLYGON)
    R1=0.8313725490196078
    G1=0.007843137254902
    B1=0.007843137254902
    n=0.22
    m=0.1515
    for i in range(10):
        n=n-0.02
        m=m-0.015
        R1=R1-0.0431372549019608
        G1=G1+0.0156862745098039
        B1=B1+0.0156862745098039
        glColor(R1,G1,B1)
        circle(0,2*pi,n,m,0,0.75)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,0,0)
    square (0.2,0.85,-0.2,0.85,-0.2,0.82,0.2,0.82)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,0,0)
    circle(pi,2*pi,0.08,0.08,0.12,0.82)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,0,0)
    circle(pi,2*pi,0.08,0.08,-0.12,0.82)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,0,0)
    square (0.1,0.64,-0.1,0.64,-0.1,0.7,0.1,0.7)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(1,1,1)
    triangle(0.1,0.7,0.05,0.7,0.075,0.675)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(1,1,1)
    triangle(0.05,0.7,0,0.7,0.025,0.675)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(1,1,1)
    triangle(0,0.7,-0.05,0.7,-0.025,0.675)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(1,1,1)
    triangle(-0.05,0.7,-0.1,0.7,-0.075,0.675)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(1,1,1)
    triangle(0.1-0.02,0.64,0.05-0.02,0.64,0.075-0.02,0.67)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(1,1,1)
    triangle(0.05-0.02,0.64,0-0.02,0.64,0.025-0.02,0.67)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(1,1,1)
    triangle(0-0.02,0.64,-0.05-0.02,0.64,-0.025-0.02,0.67)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.9333333333333333,0.6549019607843137,0.1764705882352941)
    square(-0.05-0.02,0.66,-0.05-0.02,0.6455,-0.115,0.6455,-0.115,0.66)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(1,1,1)
    square(-0.115,0.6455,-0.115,0.66,-0.18,0.66,-0.18,0.6455)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.8980392156862745,0.0313725490196078,0.0313725490196078)
    square (0.075,0.6,-0.075,0.6,-0.075,0.55,0.075,0.55)
    glEnd()
    glBegin(GL_LINES)
    glColor(0,0,0)
    square (0.075,0.6,-0.075,0.6,-0.075,0.55,0.075,0.55)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.8980392156862745,0.0313725490196078,0.0313725490196078)
    square (0.05,0.5,-0.05,0.5,-0.05,0.55,0.05,0.55)
    glEnd()
    glBegin(GL_LINES)
    glColor(0,0,0)
    square (0.05,0.5,-0.05,0.5,-0.05,0.55,0.05,0.55)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.8980392156862745,0.0313725490196078,0.0313725490196078)
    square (0.025,0.5,-0.025,0.5,-0.025,0.45,0.025,0.45)
    glEnd()
    glBegin(GL_LINES)
    glColor(0,0,0)
    square (0.025,0.5,-0.025,0.5,-0.025,0.45,0.025,0.45)
    glEnd()
    #############################################################
    glBegin(GL_POLYGON) #building central hands
    glColor(0,0,0)
    square (0.45,0.03,0.7,0.03,0.7,-0.03,0.45,-0.03)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,0,0)
    square (-0.45,0.03,-0.7,0.03,-0.7,-0.03,-0.45,-0.03)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.03,0.03,0.44,0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.03,0.03,-0.44,0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,0,0)
    square (0.67,-0.03,0.7,0.03,0.8,-0.15,0.75,-0.18)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,0,0)
    square (-0.67,-0.03,-0.7,0.03,-0.8,-0.15,-0.75,-0.18)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.031,0.031,0.684,0)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.031,0.031,-0.684,0)
    glEnd()
    glBegin(GL_POLYGON)#fest
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.06,0.06,0.78,-0.18)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (0.78,-0.18,0.755,-0.18,0.755,-0.28,0.78,-0.28)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (0.79,-0.18,0.81,-0.18,0.81,-0.28,0.79,-0.28)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (0.78,-0.18,0.78,-0.21,0.88,-0.21,0.88,-0.18)
    glEnd()
    glBegin(GL_POLYGON)#fest
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.06,0.06,-0.78,-0.18)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (-0.78,-0.18,-0.755,-0.18,-0.755,-0.28,-0.78,-0.28)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (-0.79,-0.18,-0.81,-0.18,-0.81,-0.28,-0.79,-0.28)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (-0.78,-0.18,-0.78,-0.21,-0.88,-0.21,-0.88,-0.18)
    glEnd()
    ############################################
    glBegin(GL_POLYGON) #upper right and left hands
    glColor(0,0,0)
    square (0.375,0.345,0.6,0.57,0.56,0.59,0.345,0.375)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.03,0.03,0.37,0.37)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,0,0)
    square (0.6,0.57,0.3,0.8,0.29,0.77,0.55,0.56)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.03,0.03,0.58,0.58)
    glEnd()
    glBegin(GL_POLYGON) #top left hand
    glColor(0,0,0)
    square (-0.375,0.345,-0.6,0.57,-0.56,0.59,-0.345,0.375)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.03,0.03,-0.37,0.37)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,0,0)
    square (-0.6,0.57,-0.3,0.8,-0.29,0.77,-0.55,0.56)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.03,0.03,-0.58,0.58)
    glEnd()

    glBegin(GL_POLYGON)#fest
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.08,0.08,0.3,0.75)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (0.3,0.71,0.3,0.74,0.17,0.74,0.17,0.71)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (0.3,0.76,0.3,0.79,0.17,0.79,0.17,0.76)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (0.3,0.71,0.27,0.71,0.27,0.88,0.3,0.88)
    glEnd()
    glBegin(GL_POLYGON)#fest
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.08,0.08,-0.3,0.75)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (-0.3,0.71,-0.3,0.74,-0.17,0.74,-0.17,0.71)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (-0.3,0.76,-0.3,0.79,-0.17,0.79,-0.17,0.76)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (-0.3,0.71,-0.27,0.71,-0.27,0.88,-0.3,0.88)
    glEnd()
    ###############################################################
    glBegin(GL_POLYGON) #lower right hand
    glColor(0,0,0)
    square (0.375,-0.345,0.6,-0.57,0.56,-0.59,0.345,-0.375)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.03,0.03,0.37,-0.37)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,0,0)
    square (0.6,-0.57,0.6,-0.75,0.56,-0.75,0.56,-0.57)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.03,0.03,0.58,-0.58)
    glEnd()
    glBegin(GL_POLYGON) #lowr left hand
    glColor(0,0,0)
    square (-0.375,-0.345,-0.6,-0.57,-0.56,-0.59,-0.345,-0.375)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.03,0.03,-0.37,-0.37)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,0,0)
    square (-0.6,-0.57,-0.6,-0.75,-0.56,-0.75,-0.56,-0.57)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.03,0.03,-0.58,-0.58)
    glEnd()
    glBegin(GL_POLYGON)#fest
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.06,0.06,0.58,-0.77)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (0.58,-0.77,0.555,-0.77,0.555,-0.87,0.58,-0.87)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (0.59,-0.77,0.61,-0.77,0.61,-0.87,0.59,-0.87)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (0.58,-0.77,0.58,-0.8,0.68,-0.8,0.68,-0.77)
    glEnd()
    glBegin(GL_POLYGON)#fest
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.06,0.06,-0.58,-0.77)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (-0.58,-0.77,-0.555,-0.77,-0.555,-0.87,-0.58,-0.87)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (-0.59,-0.77,-0.61,-0.77,-0.61,-0.87,-0.59,-0.87)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (-0.58,-0.77,-0.58,-0.8,-0.68,-0.8,-0.68,-0.77)
    glEnd()
    #####################################
    glBegin(GL_POLYGON)#last legs
    glColor(0,0,0)
    square (.165,-0.589,0.34,-0.76,0.3,-0.78,0.13,-0.627)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.03,0.03,0.145,-0.605)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,0,0)
    square (0.34,-0.76,0.3,-0.78,0.3,-0.9,0.35,-0.9)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.03,0.03,0.32,-0.77)
    glEnd()
    glBegin(GL_POLYGON)#last legs
    glColor(0,0,0)
    square (-.165,-0.589,-0.34,-0.76,-0.3,-0.78,-0.13,-0.627)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.03,0.03,-0.145,-0.605)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0,0,0)
    square (-0.34,-0.76,-0.3,-0.78,-0.3,-0.9,-0.35,-0.9)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    circle(0,2*pi,0.03,0.03,-0.32,-0.77)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (-0.4,-0.9,-0.25,-0.9,-0.25,-0.97,-0.4,-0.97)
    glEnd()
    glBegin(GL_POLYGON)
    glColor(0.5,0.5,0.5)
    square (0.4,-0.9,0.25,-0.9,0.25,-0.97,0.4,-0.97)
    glEnd()
    #####################################################
    glFlush()
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Cool Robot")
glutDisplayFunc(coolRobot)
glutMainLoop()
