# -*- coding: cp1252 -*-
from __future__ import division
from visual import *
import math



## cor de fundo
scene.background = (1,1,1)

scene.autoscale = False
scene.range = (50,50,50)
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

#bola 
bola = sphere(color=color.green, radius=1)

# liquido, escolher a posição inicial como pos = (0,0,0)
liquido = box(pos = (0,-3,0), color = color.blue, opacity = 0.3, size=(1000,6,1000))

# caraterísticas do liquido
liquido.densidade = 1 #g/cm³


# altura inicial da bola
bola.pos.y = -45 # m
# velocidade inicial da bola
bola.velocidade = vector(0,0,0) # m/s
# massa da bola
bola.densidade = 0.5 # g/cm^3
bola.massa = bola.densidade * bola.radius**3 *4/3*math.pi

g = vector(0,-9.8,0)

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
    rate(60)
    
    bola.pos += bola.velocidade * dt

    # força gravítica
    Fg = bola.massa * g
    # impulsão
    I = - bola.radius**3 * 4/3*math.pi * liquido.densidade * g
    # força arrasto
    Fa = -3*bola.velocidade
    
    # força total aplicada na bola 
    if bola.pos.y > 0:
        F = Fg
    else:
        F = Fg+I+Fa
    
    bola.aceleracao = F/bola.massa

    bola.velocidade += bola.aceleracao * dt

    t += dt
