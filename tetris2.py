import turtle

'''
Title: Tetris
Author: Jarred Moyer

This program will create a tetris image using 4 shapes twice (totaling 8 shapes)on a valid tetris board

'''
TURTLE_OFFSET = 0


def shift_up():
    '''
    Shifts the cursor up one block
    Precondition: turtle is at a position on the graph
    Postcondition: turtle is shifted one cell up
    '''
    turtle.up()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.down()
    # turtle.speed(0)


def shift_left():
    '''
    Shifts the cursor left 1 block
    Precondition: turtle is at a position on the graph
    Postcondition: turtle is shifted one cell left
    '''
    turtle.backward(10)


def shift_up_3():
    '''
    Shifts the cursor up 3 cells
    Precondition: turtle is at a position on the graph
    Postcondition: turtle is shifted three cells up
    '''
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)


def draw_board():
    '''
    draws the tetris board

    '''
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)


def draw_block():
    '''
    draws 1 block (10x10 pixels)

    '''
    turtle.begin_fill()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.end_fill()


def draw_square():
    '''
    draws the square shape
    Precondition: turtle is at a position on the graph and will not break the rules of tetris from said position
    Postcondition: turtle is at the same location and orientation it started in

    '''
    turtle.fillcolor('blue')
    draw_block()
    turtle.forward(10)
    draw_block()
    shift_up()
    turtle.down()
    draw_block()
    turtle.backward(10)
    draw_block()

    turtle.up()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.down()


def draw_line():
    '''
    draws the vertical line shape
    Precondition: turtle is at a position on the graph and will not break the rules of tetris from said position
    Postcondition: turtle is at the same location and orientation it started in

    '''
    turtle.fillcolor('red')
    draw_block()
    turtle.up()
    shift_up()
    draw_block()
    shift_up()
    draw_block()
    shift_up()
    draw_block()
    turtle.up()
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)


def shift_down_3():
    '''
    shifts the cursor down 3 blocks
    Precondition: turtle is at a position on the graph
    Postcondition: turtle is shifted down three cells
    '''
    turtle.up()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.down()


def shift_right():
    '''
    shifts the cursor right 1
    Precondition: turtle is at a position on the graph
    Postcondition: turtle is shifted one cell right
    '''
    turtle.up()
    turtle.forward(10)
    turtle.down()


def draw_el():
    '''
    draws the el shape (L)
    Precondition: turtle is at a position on the graph and will not break the rules of tetris from said position
    Postcondition: turtle is at the same location and orientation it started in

    '''
    turtle.fillcolor('yellow')
    draw_block()
    shift_up()
    draw_block()
    shift_up()
    draw_block()
    shift_down_3()
    shift_right()
    draw_block()
    turtle.up()
    turtle.backward(10)
    turtle.down()


def backward_el():
    '''
    Draws the backward el shape
    Precondition: turtle is at a position on the graph and will not break the rules of tetris from said position
    Postcondition: turtle is at the same location and orientation it started in
    '''
    turtle.fillcolor('green')
    draw_block()
    shift_right()
    draw_block()
    shift_up()
    draw_block()
    shift_up()
    draw_block()
    turtle.up()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.backward(10)
    turtle.down()


def return_home(x, y):
    '''
    Moves the cursor left x and down y; used to return the cursor to the home position
    Precondition: cursor is at the endpoint of a shape facing right
    Postcondition: cursor is facing the right and at the bottom left of the tetris board.
    '''
    turtle.up()
    turtle.right(90)
    turtle.forward(y * 10)
    turtle.right(90)
    turtle.forward(x * 10)
    turtle.right(180)
    TURTLE_OFFSET = 0
    turtle.down()


def move(x, y):
    '''
    Moves the cursor right x and up y

    Precondition: at the bottom left corner of the tetris table
    Postcondition: at the bottom left corner of the desiered cell
    '''
    turtle.up()
    turtle.forward(x * 10)
    turtle.left(90)
    turtle.forward(y * 10)
    turtle.right(90)
    turtle.down()


def rotate_shape(angle):
    '''
    Rotates the shape that is about to be constructed by a given angle, returns the angle such that it can be accounted
    for globally

    Precondition: at the starting cell for a tetris shape
    Postcondition: rotated a set amount to the left of the original orientation.

    '''
    turtle.left(angle)
    return angle


def revert_rotate(angle):
    '''
    Reverts the rotation of rotate_shape

    Precondition: turtle is rotated
    Postcondition: turtle is facing towards the right side of the screen
    '''
    turtle.right(angle)


def shift_down():
    '''
    shifts the WIP block down one
    Precondition: turtle is at a position on the graph
    Postcondition: turtle is shifted one cell down
    '''
    turtle.up()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.down()


def draw_s():
    '''
    Draws the s shape
    Precondition: turtle is at a position on the graph and will not break the rules of tetris from said position
    Postcondition: turtle is at the same location and orientation it started in
    '''
    turtle.fillcolor('purple')
    draw_block()
    shift_right()
    draw_block()
    shift_up()
    draw_block()
    shift_right()
    draw_block()
    turtle.up()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.backward(20)
    turtle.down()


def draw_z():
    '''
    Draws the z shape
    Precondition: turtle is at a position on the graph and will not break the rules of tetris from said position
    Postcondition: turtle is at the same location and orientation it started in
    '''
    turtle.fillcolor('orange')
    draw_block()
    shift_right()
    draw_block()
    turtle.up()
    turtle.backward(10)
    turtle.down()
    shift_up()
    draw_block()
    shift_left()
    draw_block()
    turtle.up()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)


def draw_t():
    '''
    Draws the t shape
    Precondition: turtle is at a position on the graph and will not break the rules of tetris from said position
    Postcondition: turtle is at the same location and orientation it started in
    '''
    turtle.fillcolor('grey')
    draw_block()
    shift_right()
    draw_block()
    shift_up()
    draw_block()
    shift_down()
    shift_right()
    draw_block()
    turtle.up()
    turtle.backward(20)
    turtle.down()


def interpret_input(input_shape, angle):
    '''
    Draws a shape given a letter input

    Precondition: Cursor is at correct location at any given angle facing right

    Postcondition: Cursor is at the same point defined in the precondition with the same orientation
    '''
    if (input_shape == 'b' or input_shape == 'B'):
        draw_square()
    elif (input_shape == 'i' or input_shape == 'I'):

        draw_line()
    elif (input_shape == 'l' or input_shape == 'L'):
        draw_el()
    elif (input_shape == 'j' or input_shape == 'J'):
        backward_el()
    elif (input_shape == 's' or input_shape == 'S'):
        draw_s()
    elif (input_shape == 'z' or input_shape == 'Z'):
        draw_z()
    elif (input_shape == 't' or input_shape == 'T'):
        draw_t()


#turtle.speed(0)
draw_board()
interpret_input('b', 0)
move(0, 2)
interpret_input('i', 0)
return_home(0, 2)
move(3, 0)
interpret_input('s', 0)
return_home(3, 0)
move(5, 0)
interpret_input('t', 0)
return_home(5, 0)
move(8, 0)
interpret_input('z', 0)
return_home(8, 0)
move(4, 2)
interpret_input('l', 0)
return_home(4, 2)
move(7, 2)
interpret_input('j', 0)
return_home(7, 2)

shape_input = input('Enter a letter {BILJZST} to choose the shape to place: ')
angle_input = input('Enter 0,90,180,or 270 for the rotation: ')
row_input = input('Enter row number (0 to 19) from the bottom left space: ')
col_input = input('Enter column number (0 to 19) from the bottom left space: ')
move(int(row_input), int(col_input))
TURTLE_OFFSET = rotate_shape(int(angle_input))
interpret_input(shape_input, angle_input)
revert_rotate(TURTLE_OFFSET)
return_home(int(row_input), int(col_input))
turtle.done()