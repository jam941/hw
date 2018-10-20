'''
Author: Jarred Moyer <jam4936@rit.edu>
Title: shapy_turtle.py
Language: python3
Description: Uses user input to implement a given set of turtle commands
Assignment: Lab 5
'''

import turtle

WINDOW_DIM = 1000 # Controls the length of each side of the turtle window
def init():
    '''
    Initialize turtle board

    '''
    turtle.setup(WINDOW_DIM, WINDOW_DIM, 0, 0)


def get_num(ch):
    '''
    Finds the numbers after a character in the string ch
    Preconditions: the first character in the string is a number
    Returns: the string section that is the number at the beginning of ch

    '''
    temp_list = ""
    if ((ch[0].isdigit() == False)):
        return None
    for i in ch:
        if (i.isdigit()):
            temp_list = temp_list + i


        else:
            return temp_list
    return temp_list


def proccess_left(string):
    '''
    Turns the turtle a certain amount of degrees left, as described in command
    the parameter string must start with a number
    Returns the string starting at the next command

    '''

    x = get_num(string)
    if (x == None):
        return 1
    turtle.left(int(x))
    return string[len(str(x)):]


def proccess_right(string):
    '''
    Turns the turtle a certain amount of degrees right, as described in command
    the parameter string must start with a number
    Returns the string starting at the next command

    '''

    x = get_num(string)
    if (x == None):
        return None
    turtle.left(int(x))
    return string[len(str(x)):]


def proccess_square(string):
    '''
    Draws a square, as described in command
    the parameter string must start with a number
    Returns the string starting at the next command
    '''
    x = get_num(string)
    if (x == None):
        return None
    for i in range(0, 4):
        turtle.left(90)
        turtle.forward(int(x))
    return string[len(str(x)):]


def proccess_triangle(string):
    '''
    Draws a triangle, as described in command
    the parameter string must start with a number
    Returns the string starting at the next command
    '''
    x = get_num(string)
    if (x == None):
        return None
    for i in range(0, 3):
        turtle.forward(int(x))
        turtle.left(120)
    return string[len(str(x)):]


def proccess_circle(string):
    '''
    Draws a circle, as described in command
    the parameter string must start with a number
    Returns the string starting at the next command
    '''
    x = get_num(string)
    if (x == None):
        return None
    turtle.circle(int(x))
    return string[len(str(x)):]


def proccess_forward(string):
    '''
    moves turtle forward, as described in command
    the parameter string must start with a number
    Returns the string starting at the next command
    '''
    x = get_num(string)
    if (x == None):
        return None
    turtle.forward(int(x))
    return string[len(str(x)):]


def proccess_backward(string):
    '''
    moves turtle backward, as described in command
    the parameter string must start with a number
    Returns the string starting at the next command
    '''
    x = get_num(string)
    if (x == None):
        return None
    turtle.backward(int(x))
    return string[len(str(x)):]


def proccess_up(string):
    '''
    picks pen up, as described in command
    the parameter string must start with next command
    Returns the string starting at the next command
    '''
    turtle.up()
    return string[:]


def proccess_down(string):
    '''
    puts pen down, as described in command
    the parameter string must start next command
    Returns the string starting at the next command
    '''
    turtle.down()
    return string[:]


def proccess_rectangle(string):
    '''
    Draws a recangle, as described in command
    the parameter string must start with a number
    Length and width must be seperated by a non-numerical character
    Returns the string starting at the next command
    '''
    x = get_num(string)
    if (x == None):
        return None
    temp = string[len(str(x)):]
    y = get_num(temp[1:])
    if (y == None):
        return None
    turtle.forward(int(y))
    turtle.left(90)
    turtle.forward(int(x))
    turtle.left(90)
    turtle.forward(int(y))
    turtle.left(90)
    turtle.forward(int(x))
    turtle.left(90)
    return temp[len(str(y))+1:]


def proccess_polygon(string):
    '''
    Draws a polygon, as described in command
    the parameter string must start with a number
    side count and length must be seperated by a non-numerical character
    Returns the string starting at the next command
    '''
    x = get_num(string)
    if (x == None):
        return None
    temp = string[len(str(x)):]
    y = get_num(temp[1:])
    if (y == None):
        return None
    for i in range(0, int(x)):
        turtle.forward(int(y))
        turtle.left(360 / int(x))
    return temp[len(str(y))+1:]


def proccess_goto(string):
    '''
    Goes to a position, as described in command
    the parameter string must start with a number
    x and y coordinates must be separated by a non-numerical character
    Returns the string starting at the next command
    '''
    x_pol = 1
    y_pol = 1
    if(string[0]) == '-':
        string = string[1:]
        x_pol = -1



    x = get_num(string)
    temp = string[len(str(x))+1:]
    print(temp)
    if(temp[0]) == '-':
        temp = temp[1:]
        y_pol = -1

    y = get_num(temp[1:])
    print(y)
    if (x == None):
        return None
    if (y == None):
        return None
    turtle.up()
    turtle.goto(int(x)*x_pol, int(y)*y_pol)
    turtle.down()
    return temp[len(str(y)) + 1:]


def proccess_color(string):
    '''
    Sets pen color, as described in command
    the parameter string must start with a number
    Returns the string starting at the next command
    '''
    x = int(get_num(string))
    if (x == None):
        return None
    if (x == 0):
        turtle.pencolor('red')
    elif (x == 1):
        turtle.pencolor('blue')
    elif (x == 2):
        turtle.pencolor('green')
    elif (x == 3):
        turtle.pencolor('yellow')
    elif (x == 4):
        turtle.pencolor('brown')
    else:
        turtle.pencolor('black')
    return string[1:]


def process_commands(string):
    '''
    Analyzes a string and runs a given shapey command
    the first character in the string must be a command symbol
    returns the string starting at the next command
    '''

    if (string[0] == '<'):

        return proccess_left(string[1:])

    elif (string[0] == '>'):

        return proccess_right(string[1:])

    elif (string[0] == 'S'):

        return proccess_square(string[1:])

    elif (string[0] == 'T'):

        return proccess_triangle(string[1:])

    elif (string[0] == 'C'):

        return proccess_circle(string[1:])

    elif (string[0] == 'F'):

        return proccess_forward(string[1:])

    elif (string[0] == 'B'):

        return proccess_backward(string[1:])

    elif (string[0] == 'U'):

        return proccess_up((string[1:]))

    elif (string[0] == 'D'):

        return proccess_down(string[1:])

    elif (string[0] == 'R'):

        return proccess_rectangle(string[1:])

    elif (string[0] == 'P'):

        return proccess_polygon(string[1:])

    elif (string[0] == 'G'):

        return proccess_goto(string[1:])

    elif (string[0] == 'Z'):

        return proccess_color(string[1:])
    else:
        print('Error producing string, No command visible:' + string)
        return ''


def main():
    '''
    Prompts the user for an input of commands. Attempts to run inputted commands
    '''
    string = input('Please input commands to be processed: ')
    init()
    while (string != ''):
        hold = string
        string = process_commands(string)
        if (string == None):
            print('Error producing string:  ' + hold)
            break
    turtle.done()


main()
