import turtle


def draw_circle(width, depth):
    if depth == 1:
        #turtle.circle(width)
        pass
    else:
        turtle.circle(width/depth)
        turtle.up()
        turtle.forward(width/depth)
        turtle.left(90)
        turtle.forward(width/depth)
        turtle.right(90)
        turtle.down()
        draw_circle(width/2,depth-1)
        turtle.up()
        turtle.backward(width)
        turtle.down()
        draw_circle(width*.5,depth-1)
draw_circle(100,2)
    
