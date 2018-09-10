import turtle
import math
CURRENT_HEAD = 0

def turn_abs(head, current_head):
     
    turn_head = head*(math.pi/2)
    
    print("Turn head in RADS: ", turn_head)
    turtle.left(head)
turtle.left(-180)
print(math.asin(.5))

