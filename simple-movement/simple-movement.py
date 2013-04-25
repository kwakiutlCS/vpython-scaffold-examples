from __future__ import division
from visual import *
import math


## background color
scene.background = (1,1,1)

scene.autoscale = False
scene.range = (30,30,30)

print "\n\n"



##################################################################
#                                                                #
#                PHYSICS HERE                                    #
#                                                                #
##################################################################

# body (it's a ball), sets its initial position as pos = (x,y,z)
ball = sphere(pos = (0,0,0), color = color.red, make_trail= True, trail_type="points", interval=10, retain=50)


# starts the animation
while True:
    # sets the framerate
    rate(100)
   
    # updates the projectile position 
    ball.pos = vector(0,0,0)
    
    
    
