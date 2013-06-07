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

# projectile (it's a ball), sets its initial position - pos = (x,y,z)
ball = sphere(color=color.red, pos=(0,30,0))



##################################################################
#                PHYSICS ENDS                                    #
##################################################################
scene.center=(ball.pos.y+15,ball.pos.y/2,0)
building = box(color=color.blue, pos=(0,(ball.pos.y-ball.radius)/2,0), size=(4,ball.pos.y-ball.radius,4))
terrain = box(color=color.green, pos=(ball.pos.y+10,0,0), size=((ball.pos.y+15)*2,ball.pos.y/30,ball.pos.y/3))


##################################################################
#                                                                #
#                PHYSICS HERE                                    #
#                                                                #
##################################################################

# projectile characteristics
ball.mass = 1 # kg
ball.speed = 20 # m/s
ball.angle_degree = 0 # angle measured with the horizontal (degrees)

# converts the angle to radians
ball.angle = ball.angle_degree/180*math.pi 

# projectile velocity calculated from the speed and angle
ball.velocity = vector(ball.speed*math.cos(ball.angle),ball.speed*math.sin(ball.angle),0)

# gravititional acceleration vector
g = vector(0,-9.8,0) # m/s^2

# time increment 
dt = 0.01 #s


# starts the animation
while True:
    # sets the framerate
    rate(100)

    # updates the projectile position 
    ball.pos += ball.velocity*dt

    # ends the animation if projectile hits the ground
    if ball.pos.y < ball.radius:
        break
   
    # calculates the gravitional force
    Fg = ball.mass * g
    
    # sets the total force
    F = Fg

    # calculates the projectile acceleration
    ball.accel = F / ball.mass
    
    # updates the projectile velocity
    ball.velocity += ball.accel * dt

    
    

