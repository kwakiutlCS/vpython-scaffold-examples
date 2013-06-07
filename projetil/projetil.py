# -*- coding: cp1252 -*-
from visual import *
import math

scene.background = (1,1,1)

print "\n\n"


##################################################################
#                                                                #
#                F�SICA COME�A                                   #
#                                                                #
##################################################################

# proj�til (� uma bola), escolhe o raio da bola (radius=x, em metros)
bola = sphere(color=color.red, radius=1)

# escolher a altura inicial da bola (bola.pos.y)
bola.pos.y = 30



##################################################################
#                F�SICA ACABA                                    #
##################################################################
if bola.pos.y < bola.radius:
    bola.pos.y = bola.radius+0.45

scene.center=(bola.pos.y+15,bola.pos.y/2,0)
predio = box(color=color.blue, pos=(0,(bola.pos.y-bola.radius)/2,0), size=(4,bola.pos.y-bola.radius,4))
terreno = box(color=color.green, pos=(bola.pos.y+15,0,0), size=((bola.pos.y+25)*2,1,5))
##################################################################
#                                                                #
#                F�SICA COME�A                                   #
#                                                                #
##################################################################



# carater�sticas do proj�til
bola.massa = 1 # kg
bola.magnitude_velocidade = 30 # m/s (magnitude da velocidade da bola)
bola.angulo_graus = 0 # �ngulo medido com a horizontal (graus)

# converte o �ngulo para radianos
bola.angulo = bola.angulo_graus/180.0*math.pi 

# velocidade do projetil, calculada atrav�s da magnitude da velocidade e do �ngulo
bola.velocidade = vector(bola.magnitude_velocidade*math.cos(bola.angulo), bola.magnitude_velocidade*math.sin(bola.angulo), 0)

# vector acelera��o grav�tica
g = vector(0,-9.8,0) # m/s^2

# cron�metro
t = 0 #s
# incremento ao cron�metro
dt = 0.01 #s

print "Energia mec�nica inicial"
print math.floor(bola.massa*bola.pos.y*g.mag+bola.massa/2.0*bola.velocidade.mag**2)

######################################################################
#                                                                    #    
#                    ANIMA��O                                        #
#                                                                    #
######################################################################

while True:
    # n�mero de frames por segundo
    rate(60)

    # atualiza o cron�metro
    t += dt
	
    # atualiza a posi��o do proj�til
    bola.pos += bola.velocidade*dt

    # acaba a anima��o se o proj�til atingir o ch�o
    if bola.pos.y < bola.radius:
        print t
        break
   
    # calcula a for�a grav�tica
    Fg = bola.massa * g
    
    # define a for�a total
    F = Fg+(-0.0*bola.velocidade.mag*bola.velocidade)

    # calcula a acelera��o do proj�til
    bola.aceleracao = F / bola.massa
    
    # atualiza a velocidade do proj�til
    bola.velocidade += bola.aceleracao * dt
    
print "Energia mec�nica final"
print math.floor(bola.massa*bola.pos.y*g.mag+bola.massa/2.0*bola.velocidade.mag**2)
