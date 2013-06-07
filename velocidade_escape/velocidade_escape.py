# -*- coding: cp1252 -*-
from __future__ import division
from visual import *
import math


## background color
scene.background = (1,1,1)

print "\n\n"



##################################################################
#                                                                #
#                F�SICA COME�A                                   #
#                                                                #
##################################################################

# planeta
planeta = sphere(color=color.green)

# carater�sticas do planeta
planeta.densidade = 5500 #kg/m**3
planeta.radius = 6.37e6 # raio do planeta em metros
planeta.massa = 4*math.pi*planeta.radius**3/3*planeta.densidade #kg

# proj�til (� uma bola)
bola = sphere(color=color.red, radius = planeta.radius/20, make_trail = True)

# altura inicial do proj�til h = x (medido a partir do solo)
h = 0.001 # percentagem do raio do planeta
bola.pos.y = planeta.radius*(1+h/100) + bola.radius

# carater�sticas do proj�til
bola.massa = 1 # kg
bola.magnitude_velocidade = 600 # m/s
bola.angulo_graus = 0 # �ngulo medido com a horizontal (em graus)

# converte o �ngulo em radianos
bola.angulo = bola.angulo_graus/180*math.pi 

# velocidade do proj�til calculado a partir da magnitude da velocidade e do �ngulo
bola.velocidade = vector(bola.magnitude_velocidade*math.cos(bola.angulo),bola.magnitude_velocidade*math.sin(bola.angulo),0)

# constante grav�tica
G = 6.67e-11

# incremento ao cron�metro 
dt = 1 #s
t = 0


# starts the animation
while True:
    # sets the framerate
    rate(1000)

    # updates the projectile position 
    bola.pos += bola.velocidade*dt

    # ends the animation if projectile hits the ground
    if (bola.pos-planeta.pos).mag < planeta.radius:
        break
   
    # calculates the gravitional force
    Fg = -G*planeta.massa*bola.massa/(bola.pos-planeta.pos).mag**3*(bola.pos-planeta.pos)

    
    # sets the total force
    F = Fg

    # calculates the projectile acceleration
    bola.aceleracao = F / bola.massa
    
    # updates the projectile velocity
    bola.velocidade += bola.aceleracao * dt

    t += dt
    


