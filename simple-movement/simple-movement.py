from __future__ import division
from visual import *
import math



## background color
scene.background = (1,1,1)

scene.autoscale = False
scene.range = (30,30,30)

def drawReferential((x,y,z)):
    xaxis = arrow(pos=(x,y,z), axis=(5,0,0), shaftwidth=0.5, color=(1,0,0))
    yaxis = arrow(pos=(x,y,z), axis=(0,5,0), shaftwidth=0.5, color=(0,1,0))
    zaxis = arrow(pos=(x,y,z), axis=(0,0,5), shaftwidth=0.5, color=(0,0,1))

drawReferential((15,15,0))
print "\n\n"



##################################################################
#                                                                #
#                PHYSICS HERE                                    #
#                                                                #
##################################################################

# body (it's a ball), sets its initial position as pos = (x,y,z)
ball = sphere(pos = (0,0,0), color = color.red, make_trail=True)

# ball characteristics
ball.velocity = vector(5,0,0) #m/s
ball.acceleration = vector(0,0,0) #m/s^2



# timer
timer = 0 #s
dt = 0.01 # increment to timer

raw_input("press enter to start the animation")

# starts the animation
while True:
    # sets the framerate
    rate(100)
   
    # updates the projectile position 
    ball.pos += ball.velocity*dt
    
    

    
