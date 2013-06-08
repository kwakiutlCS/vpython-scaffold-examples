# -*- coding: cp1252 -*-
from __future__ import division
from visual import *
import math



## cor de fundo
scene.background = (1,1,1)

scene.autoscale = False
scene.range = (10,10,100)


print "\n\n"



##################################################################
#                                                                #
#                F�SICA COME�A                                   #
#                                                                #
##################################################################

# corpo, escolher a posi��o inicial como pos = (0,0,0)
corpo = box(pos = (0,0,0), color = color.red, size=(3,1,2))


plataforma = box(pos=(0,-corpo.size.y/2-0.1,0), size=(100,0.2,3), color=color.green)


# carater�sticas do corpo
corpo.velocidade = vector(20,0,0) #m/s
corpo.massa = 2


# cron�metro
t = 0 #s
dt = 0.0001 # incremento ao cron�metro


k = 20

##################################################################
#                                                                #
#                ANIMA��O                                        #
#                                                                #
##################################################################

while True:
    # frames por segundo
    rate(6000)
    
    F = - k * corpo.pos

    corpo.aceleracao = F/corpo.massa
    
    # atualiza a posi��o do corpo
    pos_anterior = corpo.pos.x
    corpo.pos += corpo.velocidade*dt
    if corpo.pos.x * pos_anterior < 0 and corpo.pos.x > 0:
        print t
        
    corpo.velocidade += corpo.aceleracao * dt

    t += dt
