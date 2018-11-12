from Lab09 import ball_puzzle_animate

from Lab09 import stack
from ball_puzzle_animate import *


def convert_to_stack(str, Stack):
    '''
    Converts a string into a stack
    :param str: A string
    :param Stack: A stack, must be empty
    :return: stack where each layer is a character from the string
    '''
    for i in str:
        stack.push(Stack, i)
    return Stack


def move(c1, c2):
    '''
    Moves the top element from stack c1 to the top of the stack c2
    :param c1: A stack with at least one element
    :param c2: A stack with at least one element
    :return: None
    '''
    push(c2,  pop(c1))



def solve(cans):
    '''
    Solves the puzzle with corresponding animations
    :param cans: a list of stacks where the first stack is populated with th leters G,B, and R. Other stacks are empty
    :return: None
    '''
    while not is_empty(cans[0]):
        top_val = top(cans[0])

        if top_val == 'R':
            move(cans[0],cans[1])
            animate_move(cans,0,1)
        else:

            move(cans[0], cans[2])
            animate_move(cans, 0, 2)
    while  not is_empty(cans[1]):
        move(cans[1], cans[0])
        animate_move(cans, 1, 0)

    while  not is_empty(cans[2]):

        temp = top(cans[2])

        if temp == 'G':
            move(cans[2], cans[1])
            animate_move(cans, 2, 1)
        else:
            move(cans[2], cans[0])
            animate_move(cans, 2, 0)

    stop =  True
    while stop:
        if top(cans[0]) != 'R':
            move(cans[0], cans[2])
            animate_move(cans,0,2)
        else:
            stop = False
    return cans


def main():
    '''
    Prompts the user for an input string. This string is then converted to a stack of balls with the ball represented
    by the first character of the string o the bottom of the stack. An algorithm then sorts the balls into their
    corresponding cups animates them using a provided file.
    '''

    init_string = input('Please enter the intial stack: ')

    print(init_string)
    animate_init(init_string)
    red = stack.make_empty_stack()
    blue = stack.make_empty_stack()
    green = stack.make_empty_stack()
    red = convert_to_stack(init_string, red)
    cans = [red, green, blue]
    solved = solve(cans)
    animate_finish()

main()