# -*- coding: cp1252 -*-
from __future__ import division
from visual import *
import math



## cor de fundo
scene.background = (1,1,1)
scene.width = 600
scene.height = 600
scene.title = "Movimento Simples"
scene.autoscale = False
scene.range = (30,30,30)

def drawReferential((x,y,z)):
    xaxis = arrow(pos=(x,y,z), axis=(5,0,0), shaftwidth=0.5, color=(1,0,0))
    yaxis = arrow(pos=(x,y,z), axis=(0,5,0), shaftwidth=0.5, color=(0,1,0))
    zaxis = arrow(pos=(x,y,z), axis=(0,0,5), shaftwidth=0.5, color=(0,0,1))

drawReferential((15,15,0))
print "\n\n"



##################################################################
#                                                                #
#                FÍSICA COMEÇA                                   #
#                                                                #
##################################################################

# corpo, escolher a posição inicial como pos = (0,0,0)
corpo = sphere(pos = (0,0,0), color = color.red, make_trail=True, trail_type = "points", interval = 50, retain = 20)

# caraterísticas do corpo
corpo.velocidade = vector(5,0,0) #m/s
corpo.aceleracao = vector(-2,0,0) #m/s^2


# cronómetro
t = 0 #s
dt = 0.01 # incremento ao cronómetro


##################################################################
#                                                                #
#                ANIMAÇÃO                                        #
#                                                                #
##################################################################

while True:
    # frames por segundo
    rate(30)
   
    # atualiza a posição do corpo
    corpo.pos += corpo.velocidade*dt
    
    corpo.velocidade += corpo.aceleracao*dt

    
