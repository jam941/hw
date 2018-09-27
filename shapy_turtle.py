import turtle


def get_num(ch):
    temp_list = ""
    if(!(ch[0].isdigit())):
        return None
    for i in ch:
        if(i.isdigit()):
            temp_list = temp_list + i

        else:
            return

def proccess_left(string):
    pass


def proccess_right(string):
    pass

def proccess_square(string):
    pass

def process_triangle(string):
    pass

def proccess_circle(string):
    pass

def proccess_forward(string):
    pass
def proccess_backward(string)
    pass

def proccess_up(string):
    pass

def proccess_down(string):
    pass

def proccess_rectangle(string):
    pass

def proccess_polygon(string):
    pass
def proccess_goto(string):
    pass
def proccess_color(string):
    pass
def process_commands(string):

    if(string[0] == '<'):
        
       return proccess_left(string[1:])

    if(string[0] == '>'):
        
        return proccess_right(string[1:])

    if(string[0] == 'S'):
        
        return proccess_square(string[1:])

    if(string[0] == 'T'):
        
        return proccess_triangle(string[1:])
    
    if(string[0] == 'C'):
        
        return proccess_circle(string[1:])
    
    if(string[0] == 'F'):
        
        return proccess_forward(string[1:])
    
    if(string[0] == 'B'):
        
        return proccess_backward(string[1:])
    
    if(string[0] == 'U'):
        
        return proccess_up((string[1:]))
    
    if(string[0] == 'D'):
        
        return proccess_down(string[1:])
    
    if(string[0] == 'R'):
        
        return proccess_rectangle(string[1:])
    
    if(string[0] == 'P'):
        
        return proccess_polygon(string[1:])
    
    if(string[0] == 'G'):
        
        return proccess_goto(string[1:])
    
    if(string[0] == 'Z'):
        
        return proccess_color(string[1:])



















