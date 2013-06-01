def drawReferential((x,y,z)):
    xaxis = arrow(pos=(x,y,z), axis=(5,0,0), shaftwidth=0.5, color=(1,0,0))
    yaxis = arrow(pos=(x,y,z), axis=(0,5,0), shaftwidth=0.5, color=(0,1,0))
    zaxis = arrow(pos=(x,y,z), axis=(0,0,5), shaftwidth=0.5, color=(0,0,1))
