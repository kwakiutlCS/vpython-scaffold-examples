from visual import *
import math


## background color
scene.background = (1,1,1)

print "\n\n"



##################################################################
#                                                                #
#                PHYSICS HERE                                    #
#                                                                #
##################################################################

# planet
planet = sphere(color=color.blue)

# planet characteristics
planet.mass = 6e24 #kg
planet.r = 6.37e6 #m


# projectile (it's a ball), sets its initial position - pos = (x,y,z)
ball = sphere(color=color.red, pos=(0,4,0))


# projectile characteristics
ball.mass = 1 # kg
ball.speed = 2000 # m/s
ball.angle_degree = 90 # angle measured with the horizontal (degrees)

# converts the angle to radians
ball.angle = ball.angle_degree/180*math.pi 

# projectile velocity calculated from the speed and angle
ball.velocity = vector(ball.speed*math.cos(ball.angle),ball.speed*math.sin(ball.angle),0)

# gravititional constant
G = 6.67e-11

# time increment 
dt = 0.01 #s


# starts the animation
while True:
    # sets the framerate
    rate(100)

    # updates the projectile position 
    ball.pos += ball.velocity*dt

    # ends the animation if projectile hits the ground
    #if ball.pos.y < ball.radius:
     #   break
   
    # calculates the gravitional force
    #Fg = G*planet.mass*ball.mass/(ball.pos-planet.pos).mag**3*(ball.pos-planet.pos)
    
    # sets the total force
    #F = Fg

    # calculates the projectile acceleration
    #ball.accel = F / ball.mass
    
    # updates the projectile velocity
    #ball.velocity += ball.accel * dt

    
    

