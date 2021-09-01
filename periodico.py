"""

@author:  MYA
"""
import random
import matplotlib.pyplot as plt
import numpy as np

#paquetes= 5 unidades
#ejemplar entregado= $1.50
#ejemplar vendido= $2.50
#Reembolso= 0.50
a=[]
p=[]
dias=30
compra=1.5
vende=2.5
reembolso=0.5
per_vendidos_tot=0
utilidad=0
per_comprados=random.randint(40,70)


for i in range(dias):
    per_vendidos_dia=random.randint(40,70)
    per_vendidos_tot+=per_vendidos_dia
    if per_vendidos_dia<=per_comprados:
        utilidad_dia= -per_comprados*compra + per_vendidos_dia*vende+(per_comprados-per_vendidos_dia)*reembolso
    else: #demanda es mayor a per comprados
        utilidad_dia=-per_comprados*compra+per_comprados*vende
    utilidad+=utilidad_dia
    a.append(utilidad)
    p.append(per_vendidos_dia)
    
a 
p
listautilidad= np.array(a) 
listaventas= np.array(p)   
listautilidad
listaventas
""" 

"""

c1=[]
c2=[]
c3=[]
c4=[]
c5=[]
c6=[]


for j in range(len(listaventas)):
    if listaventas[j]>=40 and listaventas[j]<45: 
        c1.append(listautilidad[j])
    if listaventas[j]>=45 and listaventas[j]<50:
        c2.append(listautilidad[j])
    if listaventas[j]>=50 and listaventas[j]<55:
        c3.append(listautilidad[j])
    if listaventas[j]>=55 and listaventas[j]<60:
        c4.append(listautilidad[j])
    if listaventas[j]>=60 and listaventas[j]<65:
        c5.append(listautilidad[j])
    if listaventas[j]>=65 and listaventas[j]<=70:
        c6.append(listautilidad[j])
        
coord=[1,2,3,4,5,6]
altura=[sum(c1),sum(c2),sum(c3),sum(c4),sum(c5),sum(c6)]
nombres= ["40-45", "45-50", "50-55","55-60","60-65","65-70"]
plt.title("Utilidad por ventas en un mes ")
plt.xlabel("Periodicos vendidos")
plt.ylabel("Utilidad")
plt.bar(coord,altura,width=0.5, color=["red", "green"],tick_label=nombres)
plt.legend()
plt.show()
    
                   
                    


