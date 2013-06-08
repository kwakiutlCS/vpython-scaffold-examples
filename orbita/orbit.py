from visual import *
import math


## background color
#scene.background = (1,1,1)
scene.autoscale = False
scene.range = (2e8, 2e8, 2e8)
print "\n\n"


	
##################################################################
#                                                                #
#                PHYSICS HERE                                    #
#                                                                #
##################################################################

# 
planet = sphere(color=color.blue, pos=(0,0,0), radius=6e6)

moon = sphere(color=color.white, pos=(8e7,0,0), radius=3e6, make_trail=True)
moon2 = sphere(color=color.red, pos=(1.6e8,0,0), radius=3e6, make_trail=True)


#planet characteristics
planet.mass = 6e24

# moon characteristics
moon.mass = 1e23
moon.velocity = vector(0,2500,0)

moon2.mass = 2e23
moon2.velocity = vector(0,1500,0)


G = 6.67e-11

timer = 0
dt = 1

def getPotentialEnergy():
	return -G*planet.mass*moon.mass/moon.pos.mag

def getKineticEnergy():
	return moon.mass/2*moon.velocity.mag2
	
def getMechanicEnergy():
	return getPotentialEnergy()+getKineticEnergy()


# starts the animation
while True:
    # sets the framerate
	rate(10000)

	moon.Fg = -G*planet.mass*moon.mass/(moon.pos.mag**3)*moon.pos+G*moon2.mass*moon.mass/((moon2.pos-moon.pos).mag**3)*(moon2.pos-moon.pos)
	moon.accel = moon.Fg/moon.mass
	moon.pos += moon.velocity*dt
	moon.velocity += moon.accel*dt
	
	moon2.Fg = -G*planet.mass*moon2.mass/(moon2.pos.mag**3)*moon2.pos+G*moon2.mass*moon.mass/((moon2.pos-moon.pos).mag**3)*(moon.pos-moon2.pos)
	moon2.accel = moon2.Fg/moon2.mass
	moon2.pos += moon2.velocity*dt
	moon2.velocity += moon2.accel*dt
	
	timer += dt
	if timer%(24*365) == 0:
		print getMechanicEnergy()
    
