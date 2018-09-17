import turtle

'''
File: circles.py
Assignment: Homework
Author: Jarred Moyer <jam4936@rit.edu>
Languange: Python3
Purpose: Generates a pattern of circles given the radius of the biggest circle and how deep the 
recursive function should run

'''

def draw_circles(size):
    '''
    Draws a circle with a radius size. Draws starting at the lowest point of the circle

    size(int): the size of the radius of the circle being drawn in hte recursive layer

    Preconditions:
        size >0
        turtle is facing east
        turtle pen is down

    Postconditions:
        circle for a recursive layer is drawn
        turtle is facing east
        turtle pen is down

    '''
    turtle.circle(size)


def draw_many_circles(size, depth):
    '''
        Draws a circle with a radius size. Draws starting at the lowest point of the circle

        size(int): the size of the radius of the circle being drawn in hte recursive layer

        depth(int): The current depth of the recursion

        Preconditions:
            size >0
            depth>0
            turtle is facing east
            turtle pen is down

        Postconditions:
            circle for a recursive layer is drawn
            turtle is facing east
            turtle pen is down

        '''

    if(depth == 1):
        draw_circles(size)
    elif(depth >1):
        draw_circles(size)
        turtle.up()
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.right(90)
        turtle.down()
        draw_many_circles(size/2, depth -1)
        turtle.up()
        turtle.backward(2*size)
        turtle.down()
        draw_many_circles(size/2, depth -1)
        turtle.up()
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.down()

def main():
    '''
    Prompt the user for the amount of recursivbe layers they would like to run, then generate the given circle pattern
    '''
    dep = int(input('What depth should the recursion run to:  '))
    draw_many_circles(100,dep)
    turtle.done()

main()
