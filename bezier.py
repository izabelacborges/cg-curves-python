import numpy as np
import matplotlib.pyplot as plt
from collections import namedtuple


def bezier_linear(p1, p2, t):
    return (1.0 - t) * p1 + t * p2

def interpolar_pontos(pontos, t):
    return [bezier_linear(p1, p2, t) for p1, p2 in zip(pontos, pontos[1:])]

def bezier(pontos_controle, t, parada=2):
    pontos = array_pontos(pontos_controle)
    while len(pontos) > parada:
        pontos = interpolar_pontos(pontos, t)
        
    return bezier_linear(pontos[0], pontos[1], t)

def array_pontos(tupla_pontos):
    return [np.array(p) for p in tupla_pontos]

def plot_curva_bezier(pontos_controle):
    tempo = np.linspace(0, 1, num=1000)
    curva = [bezier(pontos_controle, t) for t in tempo]
    x, y = list(zip(*pontos_controle))
    curva_x, curva_y = zip(*curva)
    
    plt.plot(x, y, 'bo-', curva_x, curva_y, 'r') 

def callback(evento):
   
    global  lista_pontos
    if evento.button==1 and evento.inaxes:
        x, y = evento.xdata, evento.ydata
      
        lista_pontos.append((x,y))  
        plt.plot(x, y, 'bo') 
       
    elif evento.button==3:
        plot_curva_bezier(lista_pontos) 
        plt.draw()     
    
    else: pass

def eixos_bezier():
    figura = plt.figure(figsize=(6, 5))
    eixo = figura.add_subplot(111)

    eixo.set_xlim([0, 1])
    eixo.set_ylim([0, 1])
    eixo.grid('on')   
    eixo.set_autoscale_on(False)
    figura.canvas.mpl_connect('button_press_event', callback)

lista_pontos = []
eixos_bezier()