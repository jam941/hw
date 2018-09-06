import math
def generate_sqrt(a,b,c):
    return b**2 -4*a*c
def root_quantity(a,b,c):
    
    if(generate_sqrt(a,b,c)>0):
        return 2
    elif(generate_sqrt(a,b,c) == 0):
        return 1
    elif(generate_sqrt(a,b,c) <0):
        return 0







def gen_root_one(a,b,c):

    if(root_quantity(a,b,c) ==1):
        return (-b/(2*a))
    elif(root_quantity(a,b,c) == 2):
        return ((-b + math.sqrt(generate_sqrt(a,b,c)))/(2*a))
    
    
def gen_root_two(a,b,c):
      
        return ((-b - math.sqrt(generate_sqrt(a,b,c)))/(2*a))
    
def gen_equation(a,b,c):
    print('Equation: ',a,'x^2', '+' ,b,'x', '+' ,c ,'=' , 0)
    
def respace():
    print('=======================')
    print(' ')
    print('=======================')
    print(' ')
    print(' ')
    print(' ')

    
def gen_one_report(a,b,c):
    gen_equation(a,b,c)
    print('One Root')
    print('x = ', gen_root_one(a,b,c))
    respace()


def gen_two_report(a,b,c):
    gen_equation(a,b,c)
    print('Two Roots')
    print('x = ', gen_root_one(a,b,c))
    print('x = ', gen_root_two(a,b,c))
    respace()


def gen_zero_report(a,b,c):
    gen_equation(a,b,c)
    print('No Roots')
    respace()

def gen_roots(a,b,c):
    if(root_quantity(a,b,c) == 1):
        gen_one_report(a,b,c)
    elif(root_quantity(a,b,c) == 2):
        gen_two_report(a,b,c)
    elif(root_quantity(a,b,c) == 0):
        gen_zero_report(a,b,c)
    
def main():
    
    gen_roots(1,0,-9)
    gen_roots(0,0,7)
    gen_roots(0,7,26)
    gen_roots(7,4,2)
    gen_roots(7/2, 1.6, math.pi)
    gen_roots(math.e,1,1)


main()
