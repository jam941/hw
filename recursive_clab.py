import turtle
def draw_circle(size):
    '''
    Draws a circle centered on the initial point

    Pre-condition: turtle is positioned at the center of a bowtie

    Post-condition: turtle is returned to the center of the bowtie
    '''
    turtle.right(90)
    turtle.up()
    turtle.forward(size/4)
    turtle.left(90)
    turtle.down()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.circle(size/4)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(size/4)
    turtle.right(90)
    turtle.down()

def draw_bowtie1(size):
    '''
    Draws a bowtie, as well as one 2 times its height and 30 degrees offset from its horizontal,
    as well as one 120 degrees out from its horizontal and 2 times its size away

    Pre-condition: Turtle is at the location where a bowtie will be drawn (the to-be bowtie's center)

    Post-condition: Turtle is returned to the center of the original bowtie
    '''
    turtle.pencolor('blue')
    turtle.left(30)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(2*size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.right(30)
    draw_circle(size)

def draw_bowtie(size,depth):
    '''
    
    '''
    if(depth != 0):
        draw_bowtie1(size)
        turtle.up()
        turtle.left(30)
        turtle.forward(2*size)
        turtle.down()
        draw_bowtie(size/3,depth-1)
        turtle.up()
        turtle.backward(2*size)
        turtle.left(90)
        turtle.forward(2*size)
        turtle.down()
        draw_bowtie(-size/3,depth-1)
        turtle.up()
        turtle.backward(2*size)
        turtle.left(90)
        turtle.forward(2*size)
        turtle.down()
        draw_bowtie(-size/3,depth-1)
        turtle.up()
        turtle.backward(2*size)
        turtle.left(90)
        turtle.forward(2*size)
        turtle.down()
        draw_bowtie(-size/3,depth-1)

def init():
    turtle.setup(600,600)
    return(int(input('What depth would you like to run the program until (depth>=1)')))
def main():
    draw_bowtie(600/6,init())
main()
