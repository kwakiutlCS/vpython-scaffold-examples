from visual import *
import math


## background color
#scene.background = (1,1,1)
scene.autoscale = False
scene.range = (1e12, 1e12, 1e12)
print "\n\n"


	
##################################################################
#                                                                #
#                PHYSICS HERE                                    #
#                                                                #
##################################################################

# 
sol = sphere(color=color.yellow, pos=(0,0,0), radius=3e10)

terra = sphere(color=color.blue, pos=(1.5e11,0,0), radius=1.5e10, make_trail=True)
jupiter = sphere(color=color.red, pos=(7e11,0,0), radius=2e10, make_trail=True)


#planet characteristics
sol.massa = 2e30

# moon characteristics
terra.massa = 6e24
terra.velocidade = vector(0,30000,0)

jupiter.massa = 1e27
jupiter.velocidade = vector(0,12000,0)


G = 6.67e-11

timer = 0
dt = 1000

def getPotentialEnergy():
	return -G*planet.mass*moon.mass/moon.pos.mag

def getKineticEnergy():
	return moon.mass/2*moon.velocity.mag2
	
def getMechanicEnergy():
	return getPotentialEnergy()+getKineticEnergy()


# starts the animation
while True:
    # sets the framerate
	rate(5000)

	terra.Fg = -G*sol.massa*terra.massa/((terra.pos-sol.pos).mag**3)*(terra.pos-sol.pos)-G*jupiter.massa*terra.massa/((terra.pos-jupiter.pos).mag**3)*(terra.pos-jupiter.pos)
	terra.aceleracao = terra.Fg/terra.massa
	terra.pos += terra.velocidade*dt
	terra.velocidade += terra.aceleracao*dt	
	
	jupiter.Fg = -G*sol.massa*jupiter.massa/((jupiter.pos-sol.pos).mag**3)*(jupiter.pos-sol.pos)+G*jupiter.massa*terra.massa/((terra.pos-jupiter.pos).mag**3)*(terra.pos-jupiter.pos)
	jupiter.aceleracao = jupiter.Fg/jupiter.massa
	jupiter.pos += jupiter.velocidade*dt
	jupiter.velocidade += jupiter.aceleracao*dt	
	
	timer += dt
	if timer%(60*60*24*30) == 0:
		print timer/30/24/3600
	
	
	
    
