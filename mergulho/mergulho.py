# -*- coding: cp1252 -*-
from __future__ import division
from visual import *
import math



## cor de fundo
scene.background = (1,1,1)

scene.autoscale = False
scene.range = (100,50,5)
scene.userspin = False
scene.userzoom = False
scene.width = 600
scene. height = 600

scene.title = "Mergulho"

print "\n\n"



##################################################################
#                                                                #
#                FÍSICA COMEÇA                                   #
#                                                                #
##################################################################

# liquido, escolher a posição inicial como pos = (0,0,0)
liquido = box(pos = (0,-3,0), color = color.blue, opacity = 0.3, size=(1000,6,1000))

# caraterísticas do liquido
liquido.densidade = 1 #g/cm³


#bola 
bola = sphere(color=color.green, radius=1)

bola.pos.y = 20

# cronómetro
t = 0 #s
dt = 0.0001 # incremento ao cronómetro


##################################################################
#                                                                #
#                ANIMAÇÃO                                        #
#                                                                #
##################################################################

while True:
    # frames por segundo
    rate(6000)
    
    
    t += dt
