import turtle

'''
Author: Jarred Moyer <jam4936@rit.edu>
Title: bowties.py
Language: python3
Description: Uses recursive functions to draw a bowtie pattern to a specific depth and at a set size. Depth given as user input
Assignment: Lab 3
'''

def draw_circle(size):
    '''
    Draws a circle centered on the initial point

    Pre-condition: Turtle is facing east, pen down
    Post-condition: Turtle is facing east, pen down, fill color set to red
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

    Pre-condition: turtle facing east, pen down

    Post-condition: Turtle facing east, pen down
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
    Draws a pattern of bowties given the size of the base bowtie and how deep the recursive function should run

    int(size): size>0
    int(depth): depth>1

    Precondition: turtle facing east, pen down

    Postcondition: turtle facing east, pen down
    '''
    if(depth >1):
        draw_bowtie1(size)
        turtle.up()
        turtle.left(30)
        turtle.forward(2*size)
        turtle.down()
        draw_bowtie(size/3,depth-1)
        
        turtle.up()
        turtle.backward(2*size)
        turtle.left(120)
        turtle.forward(2*size)
        turtle.down()
        
        draw_bowtie(-size/3,depth-1)
        turtle.up()
        turtle.backward(2*size)
        turtle.left(60)
        turtle.forward(2*size)
        turtle.down()
        
        draw_bowtie(-size/3,depth-1)
        turtle.up()
        turtle.backward(2*size)
        turtle.left(120)
        turtle.forward(2*size)
        turtle.down()
        
        draw_bowtie(-size/3,depth-1)

        turtle.up()
        turtle.backward(size*2)
        turtle.left(30)
        turtle.down()
        

def init():
    '''
    Creates a set sized window and returns the depth of the recursive funciton should run until

    '''
    turtle.setup(600,600)
    return(int(input('What depth would you like to run the program until (depth>=1)')))
def main():
    '''
    Draws a bowtie pattern with a base size of 100 pixels to a depth createed by user input.
    Precondition: turtle facing east, pen down
    Postcondition: turtle facing east, pen down
    :return:
    '''
    draw_bowtie(600/6,init())
main()
