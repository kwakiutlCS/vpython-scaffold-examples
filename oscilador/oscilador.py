# -*- coding: cp1252 -*-
from __future__ import division
from visual import *
import math



## cor de fundo
scene.background = (1,1,1)

scene.autoscale = False
scene.range = (10,10,10)
scene.title = "Oscilador"
scene.width = 600
scene.height = 600

print "\n\n"



##################################################################
#                                                                #
#                FÍSICA COMEÇA                                   #
#                                                                #
##################################################################



# corpo, escolher a posição inicial como pos = (0,0,0)
corpo = box(pos = (0,0,0), color = color.red, size=(3,3,2))

bloco = box(pos = (-10,0,0), color = color.blue, size = (3,3,3))
mola = helix(pos = (-8.5,0,0), axis = (7,0,0), coils=15)

plataforma = box(pos=(0,-corpo.size.y/2-0.1,0), size=(100,0.2,3), color=color.green)


# caraterísticas do corpo
corpo.velocidade = vector(15,0,0) #m/s
corpo.massa = 2


# cronómetro
t = 0 #s
dt = 0.0001 # incremento ao cronómetro


k = 20

##################################################################
#                                                                #
#                ANIMAÇÃO                                        #
#                                                                #
##################################################################

while True:
    # frames por segundo
    rate(6000)
    
    F = - k * corpo.pos

    corpo.aceleracao = F/corpo.massa
    
    # atualiza a posição do corpo
    pos_anterior = corpo.pos.x
    corpo.pos += corpo.velocidade*dt
    mola.axis = corpo.pos+vector(-1.5,0,0)-mola.pos
    
    if corpo.pos.x * pos_anterior < 0 and corpo.pos.x > 0:
        print t
        
    corpo.velocidade += corpo.aceleracao * dt

    t += dt
