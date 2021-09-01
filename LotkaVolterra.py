#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 19:07:21 2021

@author: MYA
"""
import matplotlib.pyplot as plt

DInicial=	12
PInicial=12
a=0.2
b=0.01
c=0.02
d=0.05
dt=0.075
	
	
Tsim=300
Observaciones=4001
t=[0]
x=[12] #presa
y=[12] #depredador

NacDepredadores=[]
MuerteDepredador=[]
NacimMuerteD=[]
NacPresas=[]
MuertePresa=[]
NacimMuerteP=[]

for i in range(1,Observaciones):
    t.append(t[i-1]+dt)
    
    NacDepredadores.append(y[i-1]*b*x[i-1])
    
    MuerteDepredador.append(a*y[i-1])
    
    NacimMuerteD.append(NacDepredadores[i-1]-MuerteDepredador[i-1])
    
    y.append(y[i-1]+dt*NacimMuerteD[i-1])
    
    NacPresas.append(d*x[i-1])
    
    MuertePresa.append(c*x[i-1]*y[i-1])
    
    NacimMuerteP.append(NacPresas[i-1]-MuertePresa[i-1])
    
    x.append(x[i-1]+dt*NacimMuerteP[i-1])

plt.plot(t,x, label="presa")
plt.plot(t,y, label="depredador")
plt.xlim(0,310) 
plt.ylim(0,60) 
plt.xlabel("Tiempo")
plt.ylabel("Poblacion")
plt.title("Modelo Lotka-Volterra")

plt.legend()
plt.show()



 
    
    
    
    
   


    