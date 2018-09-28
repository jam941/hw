import turtle as t
t.colormode(255)
import math
import random
'''
Author: Jarred Moyer
Title: arrows.py
Language: python3
Description: Uses recursive and iterative functions to draw a randomly generated pattern of triagles inside a binding box
Assignment: Lab 4
'''
MAX_ANGLE = 30

MAX_DISTANCE = 30

MAX_SIZE =30

WINDOW_SIZE = 400
def init():
    '''
    Initialize the window and set the speed to maximum
    No pre/post conditions
    '''
    t.speed(0)
    t.setup(WINDOW_SIZE,WINDOW_SIZE,0,0)

def draw_box():
    '''
    Generates the bounding box using a global constant

    Precondition: pen down, turtle facing east

    Post condition: pen down, turtle facing east
    '''
    t.up()
    t.forward(WINDOW_SIZE/2)
    t.left(90)
    t.down()
    t.forward(WINDOW_SIZE/2)
    t.left(90)
    
    t.forward(WINDOW_SIZE)
    t.left(90)
    
    t.forward(WINDOW_SIZE)
    t.left(90)
    
    t.forward(WINDOW_SIZE)
    
    t.left(90)
    t.forward(WINDOW_SIZE/2)
    t.up()
    t.right(90)
    t.backward(WINDOW_SIZE/2)
    t.down()
    
def get_area(side):
    '''
    Generates the area of a triangle painted using the equilateral triangle formula
    returns the area calculated
    '''
    return ((math.sqrt(3)/4)*(side*side))
def check(x,y):
    '''
    Checks to see if a given point is within the bounding box
    returns a verdict of true(In the box) or false (outside the box)
    '''
    if(x>0 and x< WINDOW_SIZE ) or(y>0 and y< WINDOW_SIZE ):
        return True
    else:
        return False
def check_bounds(size):
    '''
    Checks to see if the would be triangle is inside the bounding box

    Precondition: pen down
    Postcondition: pen down
    '''
    t.up()
    t.forward(size)
    if(check(t.xcor()+250,t.ycor()+250) == False):
       
        return False
    t.left(120)
    
    t.forward(size)
    if(check(t.xcor()+250,t.ycor()+250) == False):
    
        return False
    t.left(120)
    t.up()
    t.forward(size)
    if(check(t.xcor()+250,t.ycor()+250) == False):
        
        return False
    t.left(120)
    t.down()
    
    return True
def draw_triangle(size):
    '''
    Draws an equilateral triangle with side length size
    '''
    t.down()
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
def rand_angle():
    '''
    Generates a random angle, range -MAX_ANGLE, +MAX_ANGLE
    returns the angle
    '''
    return random.randint(-MAX_ANGLE,MAX_ANGLE)
def rand_distance():
    '''
    Generates a random distance in range of (1,MAX_DISTANCE)
    returns the distance
    '''
    return random.randint(1,MAX_DISTANCE)
def rand_length():
    '''
    Generates a random length in range (1,MAX_DISTANCE)
    returns the length
    '''
    return random.randint(1,MAX_SIZE)

def rand_color():
    '''
    Generates a value in range (1,255) to specify the R,g, or b of a fill color
    returns this value
    '''
    return random.randint(1,255)

def draw_figure_rec(number,side,total):
    '''
    Draws a randomly generated triangular pattern recursivly.
    Returns the total area painted with the fill comands
    Paramaters: number>0, side>0, total == 0
    '''
    if(number != 0):
        if(check_bounds(side)):
            #t.pencolor("#ffffff")o
            t.fillcolor((rand_color(),rand_color(),rand_color()))
            t.begin_fill()
            draw_triangle(side)
            t.end_fill()
            t.up()
            t.left(rand_angle())
            t.forward(rand_distance())
            t.down()
            total = total + get_area(side)
            return draw_figure_rec(number-1,rand_length(),total)

        else:
            t.left(90)
            return draw_figure_rec(number,side,total)
    else:
        return total
    
    
    
def draw_figure_iter(number,total):
    '''
    Draws a randomly generated triangular pattern Iteratively.
    Returns the total area painted with the fill comands
    Paramaters: number>0, total == 0
    
    '''
    while number != 0:
        side = rand_length()
        if(check_bounds(side)):
            #t.pencolor("#ffffff")o
            t.fillcolor((rand_color(),rand_color(),rand_color()))
            t.begin_fill()
            draw_triangle(side)
            t.end_fill()
            t.up()
            t.left(rand_angle())
            t.forward(rand_distance())
            t.down()
            total = total + get_area(side)
            number= number -1
            

        else:
            t.left(90)
            
    return total

def main():
    '''
    Generates a triangle pattern using random numbers and user input. HAlf of the triangles drawn are drawn recursively, while the others are drawn iteratively
    '''

    triangles = int(input('How many total triangles would you like the code to produce? (0-500)'))
    print('Arrows(0-500)', triangles)
    if(triangles<=0 or triangles>500):
        print('Arrows must be between 0 and 500 inclusive')
        pass
    
    init()

    
    draw_box()
    print('The total area painted was ', draw_figure_rec(triangles/2,20,0), ' Units')
    input('Press any key to countinue')
    t.reset()
    init()
    draw_box()
    print('The total area painted was ', draw_figure_iter(triangles/2,0), ' Units')
    print('Close the window to quit')
    t.done()
    
    
main()
