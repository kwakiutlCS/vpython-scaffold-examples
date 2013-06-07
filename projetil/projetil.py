# -*- coding: cp1252 -*-
from visual import *
import math

scene.background = (1,1,1)

print "\n\n"


##################################################################
#                                                                #
#                FÍSICA COMEÇA                                   #
#                                                                #
##################################################################

# projétil (é uma bola), escolhe o raio da bola (radius=x, em metros)
bola = sphere(color=color.red, radius=1)

# escolher a altura inicial da bola (bola.pos.y)
bola.pos.y = 30



##################################################################
#                FÍSICA ACABA                                    #
##################################################################
if bola.pos.y < bola.radius:
    bola.pos.y = bola.radius+0.45

scene.center=(bola.pos.y+15,bola.pos.y/2,0)
predio = box(color=color.blue, pos=(0,(bola.pos.y-bola.radius)/2,0), size=(4,bola.pos.y-bola.radius,4))
terreno = box(color=color.green, pos=(bola.pos.y+15,0,0), size=((bola.pos.y+25)*2,1,5))
##################################################################
#                                                                #
#                FÍSICA COMEÇA                                   #
#                                                                #
##################################################################



# caraterísticas do projétil
bola.massa = 1 # kg
bola.magnitude_velocidade = 30 # m/s (magnitude da velocidade da bola)
bola.angulo_graus = 0 # ângulo medido com a horizontal (graus)

# converte o ângulo para radianos
bola.angulo = bola.angulo_graus/180.0*math.pi 

# velocidade do projetil, calculada através da magnitude da velocidade e do ângulo
bola.velocidade = vector(bola.magnitude_velocidade*math.cos(bola.angulo), bola.magnitude_velocidade*math.sin(bola.angulo), 0)

# vector aceleração gravítica
g = vector(0,-9.8,0) # m/s^2

# cronómetro
t = 0 #s
# incremento ao cronómetro
dt = 0.01 #s

print "Energia mecânica inicial"
print math.floor(bola.massa*bola.pos.y*g.mag+bola.massa/2.0*bola.velocidade.mag**2)

######################################################################
#                                                                    #    
#                    ANIMAÇÃO                                        #
#                                                                    #
######################################################################

while True:
    # número de frames por segundo
    rate(60)

    # atualiza o cronómetro
    t += dt
	
    # atualiza a posição do projétil
    bola.pos += bola.velocidade*dt

    # acaba a animação se o projétil atingir o chão
    if bola.pos.y < bola.radius:
        print t
        break
   
    # calcula a força gravítica
    Fg = bola.massa * g
    
    # define a força total
    F = Fg+(-0.0*bola.velocidade.mag*bola.velocidade)

    # calcula a aceleração do projétil
    bola.aceleracao = F / bola.massa
    
    # atualiza a velocidade do projétil
    bola.velocidade += bola.aceleracao * dt
    
print "Energia mecânica final"
print math.floor(bola.massa*bola.pos.y*g.mag+bola.massa/2.0*bola.velocidade.mag**2)
