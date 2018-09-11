import turtle 
'''
Title: Tetris
Author: Jarred Moyer

This program will create a tetris image using 4 shapes twice (totaling 8 shapes)on a valid tetris board

'''
TURTLE_OFFSET = 0
X_OFFSET = 0
Y_OFFSET = 0
def shift_up():
    '''
    Shifts the cursor up one block

    '''
    turtle.up()
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.down()
    turtle.speed(0)
def shift_left():
    '''
    Shifts the cursor left 1 block

    '''
    turtle.backward(10)
def shift_up_3():
    '''
    Shifts the cursor up 3 cells

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

    '''
    turtle.up()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.down()
    
def shift_right():
    '''
    shifts the cursor right 1
    '''
    turtle.up()
    turtle.forward(10)
    turtle.down()
    
def draw_el():
    '''
    draws the el shape (L)

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

def reset_stack():
    '''
    resets the cursor back to the bottom of the grid a set distance from the block set being used
    '''
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(110)
    turtle.left(90)
    turtle.down()
def return_home(x,y):
    turtle.up()
    revert_rotate()
    turtle.right(90)
    turtle.forward(y*10)
    turtle.right(90)
    turtle.forward(x*10)
    turtle.right(180)
    TURTLE_OFFSET = 0
    turtle.down()

def move(x,y):
    turtle.up()
    turtle.forward(x*10)
    turtle.left(90)
    turtle.forward(y*10)
    turtle.right(90)
    turtle.down()


    
def rotate_shape(angle):
    turtle.left(angle)
    return angle

def revert_rotate(angle):
    turtle.right(angle)

def interpret_input(input_shape):
    if(input_shape == 's' or input_shape == 'S'):
        draw_square()
    elif(input_shape == 'i' or input_shape == 'I'):
        draw_line()
    elif(input_shape == 'l' or input_shape == 'L'):
        draw_el()
    elif(input_shape == 'j' or input_shape =='J'):
        backward_el()
    

turtle.speed(0)
draw_board()
inp = input('What shape')
TURTLE_OFFSET=rotate_shape(90)
test = input('go?')
print(TURTLE_OFFSET)
revert_rotate(TURTLE_OFFSET)
interpret_input(inp)
turtle.done()


