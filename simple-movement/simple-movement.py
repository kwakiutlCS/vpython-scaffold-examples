from __future__ import division
from visual import *
import math


## background color
scene.background = (1,1,1)
scene.foreground = (0,1,1)
print "\n\n"



##################################################################
#                                                                #
#                PHYSICS HERE                                    #
#                                                                #
##################################################################

# projectile (it's a ball), sets its initial position as pos = (x,y,z)
ball = sphere(color = color.red, pos = (0,0,0), make_trail= True, trail_type="points", interval=10, retain=50)


##################################################################
#                PHYSICS ENDS                                    #
##################################################################
scene.autoscale = False
scene.range = (30,30,30)

##################################################################
#                                                                #
#                PHYSICS HERE                                    #
#                                                                #
##################################################################

# projectile characteristics
ball.mass = 1 # kg
ball.velocity = vector(-4,0,0) # m/s

# sets up a timer
timer = 0.00 #s

# timer increment
dt = 0.01 #s



# starts the animation
while True:
    # sets the framerate
    rate(100)
   
    # updates the projectile position 
    ball.pos = ball.pos + ball.velocity*dt
    
    # sets the total force
    F = vector(2,0,0) 

    # calculates the projectile acceleration
    ball.accel = F / ball.mass 
    
    # updates the projectile velocity
    ball.velocity = ball.velocity + ball.accel * dt

    # updates the timer
    timer = timer + dt
    
    
