from visual import *
import math, random


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
planet = sphere(color=color.blue, pos=(0,0,0), radius=6e7)

moon = sphere(color=color.red, pos=(1.6e8,0,0), radius=3e6, make_trail=True)


#planet characteristics
planet.mass = 1e27

# moon characteristics

moon.mass = 2e23
moon.velocity = vector(0,20000,0)


G = 6.67e-11

def createRings():
	
	for i in range(3000):
		dist = random.random()*0.6e8+1.2e8
		angle = random.random()*2*3.141592
		
		v = math.sqrt(G*planet.mass/dist)
		
		position = vector(dist*math.cos(angle), dist*math.sin(angle),0)
		
		rings.append(sphere(color=color.white, pos=position, radius=7e5))
		rings[-1].velocidade = vector(-v*sin(angle),v*cos(angle),0)
		rings[-1].massa = 10
		rings[-1].position = position
		
rings = []
createRings()



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

	moon.Fg = -G*planet.mass*moon.mass/(moon.pos.mag**3)*moon.pos
	moon.accel = moon.Fg/moon.mass
	moon.pos += moon.velocity*dt
	moon.velocity += moon.accel*dt
	
	for body in rings:
		body.Fg = -G*planet.mass*body.massa/(body.pos.mag**3)*body.pos+G*moon.mass*body.massa/((body.pos-moon.pos).mag**3)*(moon.pos-body.pos)
		body.accel = body.Fg/body.massa	
		body.position += body.velocidade*dt
		body.velocidade += body.accel*dt
		if timer % 100000:
			body.pos = body.position
	
	timer += dt
	
	
