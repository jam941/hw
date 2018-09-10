'''
Author: Jarred Moyer
File roots.py
Date 09/08/2018
This file allows a user to calculate the roots of a function if they are real using a function. 
'''
import math


def generate_sqrt(a,b,c):
    '''
    Generates the number that goes inside the square root in the quadratic formula
    '''
    return b**2 -4*a*c
def root_quantity(a,b,c):
    '''
    Generates the number of roots based on the value of the generate_sqrt() function.
    '''
    if(generate_sqrt(a,b,c)>0):
        return 2
    elif(generate_sqrt(a,b,c) == 0):
        return 1
    elif(generate_sqrt(a,b,c) <0):
        return 0







def gen_root_one(a,b,c):
    '''
    Generates the first root in cases where there is 1 root or
    generates the only root if there is 1 root
    '''

    if(root_quantity(a,b,c) ==1):
        return (-b/(2*a))
    elif(root_quantity(a,b,c) == 2):
        return ((-b + math.sqrt(generate_sqrt(a,b,c)))/(2*a))
    
    
def gen_root_two(a,b,c):
    '''
    Generates the secondroot if there are 2 roots ()
    '''
    return ((-b - math.sqrt(generate_sqrt(a,b,c)))/(2*a))
    
def gen_equation(a,b,c):
    '''
    Generates the algebraic equation
    '''
    print('Equation: ',a,'x^2', '+' ,b,'x', '+' ,c ,'=' , 0)
    
def respace():
    '''
    Generates the some visual spacing to differenctiate between uses
    '''
    print('=======================')
    print(' ')
    print('=======================')
    print(' ')
    print(' ')
    print(' ')

    
def gen_one_report(a,b,c):
    '''
    Generates report of the one root cases
    '''
    gen_equation(a,b,c)
    print('One Root')
    print('x = ', gen_root_one(a,b,c))
    respace()


def gen_two_report(a,b,c):
    '''
    Generates report of the two root cases
    '''
    gen_equation(a,b,c)
    print('Two Roots')
    print('x = ', gen_root_one(a,b,c))
    print('x = ', gen_root_two(a,b,c))
    respace()


def gen_zero_report(a,b,c):
    '''
    Generates report of zero root cases
    '''
    gen_equation(a,b,c)
    print('No Roots')
    respace()

def gen_roots(a,b,c):
    '''
    Calculates and shows the roots of the function and the visual representation
    of the function given values a,b, and c.
    '''
    if(root_quantity(a,b,c) == 1):
        gen_one_report(a,b,c)
    elif(root_quantity(a,b,c) == 2):
        gen_two_report(a,b,c)
    elif(root_quantity(a,b,c) == 0):
        gen_zero_report(a,b,c)
    

gen_roots(1,0,-9)
gen_roots(1,0,7)
gen_roots(1,7,26)
gen_roots(7/2, -1.6, math.pi)
gen_roots(math.e,1,1)
gen_roots(1,0,0)
gen_roots(1/3,1/3,-1/3)
gen_roots(-100,.6,-9.3)
gen_roots(1,6,8)
gen_roots(math.pi,-17,5)



