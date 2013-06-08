from visual import *
import math


## background color
#scene.background = (1,1,1)
scene.autoscale = False
scene.range = (1e8, 1e8, 1e8)
print "\n\n"

def getPotencialEnergy():
    return -G*planet.mass*moon.mass/moon.pos.mag

def getKineticEnergy():
    return 1/2*moon.mass*moon.velocity.mag2

def getMechanicEnergy():
    return getPotencialEnergy()+getKineticEnergy()


##################################################################
#                                                                #
#                PHYSICS HERE                                    #
#                                                                #
##################################################################

# 
planet = sphere(color=color.blue, pos=(0,0,0), radius=6e6)

moon = sphere(color=color.white, pos=(8e7,0,0), radius=1.5e6, make_trail=True)


#planet characteristics
planet.mass = 6e24

# moon characteristics
moon.mass = 1e23
moon.velocity = vector(0,2400,0)

moon.trail = curve(color=moon.color)

G = 6.67e-11

dt = 100

# starts the animation
while True:
    # sets the framerate
    rate(100)

    Fg = -G*planet.mass*moon.mass/(moon.pos.mag**3)*moon.pos

    moon.accel = Fg/moon.mass

    moon.pos += moon.velocity*dt
    
    moon.velocity += moon.accel*dt

    if moon.pos.mag < moon.radius+planet.radius:
        break
    
    moon.trail.append(moon.pos)
    print getMechanicEnergy()


