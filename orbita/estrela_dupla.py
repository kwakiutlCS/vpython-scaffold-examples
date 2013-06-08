from visual import *
import math


## background color
#scene.background = (1,1,1)
scene.autoscale = False
scene.range = (5e9, 5e9, 5e9)
scene.width = 600
scene.height = 600
print "\n\n"


	
##################################################################
#                                                                #
#                PHYSICS HERE                                    #
#                                                                #
##################################################################

# 
estrela1 = sphere(color=color.yellow, pos=(0,0,0), radius=1e8, make_trail = True)

estrela2 = sphere(color=color.white, pos=(3e9,0,0), radius=5e7, make_trail=True)


# carateristicas das estrelas
estrela1.massa = 6e30 # kg
estrela2.massa = 3e30 # kg

estrela1.velocidade = vector(0,0,0)
estrela2.velocidade = vector(0,3e5,0) # m/s



G = 6.67e-11

timer = 0
dt = 1


# starts the animation
while True:
    # sets the framerate
	rate(2000)

	estrela2.Fg = G*estrela1.massa*estrela2.massa/((estrela1.pos-estrela2.pos).mag**3)*(estrela1.pos-estrela2.pos)
	estrela2.aceleracao = estrela2.Fg / estrela2.massa
	estrela2.pos += estrela2.velocidade*dt
	estrela2.velocidade += estrela2.aceleracao*dt
	"""
	estrela1.Fg = -estrela2.Fg
	estrela1.aceleracao = estrela1.Fg / estrela1.massa
	estrela1.pos += estrela1.velocidade*dt
	estrela1.velocidade += estrela1.aceleracao*dt
"""
	timer += dt
	
