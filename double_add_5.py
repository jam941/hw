'''
Author: Jarred Moyer <jam4936@rit.edu>
Title: double_add_5.py
Language: python3
Description: Uses recursive and iterative functions to analyze the double plus 5 pattern
Assignment: Homework 4
'''


def print_sequence_rec(start,count):
    '''
    Generates a secuence recursively according to the time 2  plus 5 pattern.
     Prints the sequence directly to the console
    
    Preconditions: count >0
    Postconditions: None
    '''
    if(count <0):
        pass
    elif(count == 0):
        print(start)

    else:
        print(start, end=" ")
        print_sequence_rec((2*start)+5, count -1)


def print_sequence_iter(start,count):
    '''
    Generates a secuence iteratively according to the time 2  plus 5 pattern.
     Prints the sequence directly to the console
    
    Preconditions: count >0
    Postconditions: None
    '''
    while (count>=0):
        print(start, end=" ")
        start = (2*start) +5
        count = count -1


def find_end_rec(start, count):
    '''
    Generates the last number in a times 2 plus 5 sequence recursively. Returns this value
    Preconditions: count>0
    Postconditions: Nonme
    '''
    if(count == 0):
        return start
    else:
        return find_end_rec((start*2)+5,count-1)

def find_end_iter(start,count):
    '''
    Generates a secuence iteratively  according to the time 2  plus 5 pattern.
     Prints the sequence directly to the console
    
    Preconditions: count >0
    Postconditions: None

    '''
    while(count >0):
        start = 2*start + 5
        count = count -1
    return start


def acc_find_start_rec(goal,count,a):
    '''
    Finds the best start value that corresponds to a end point and a given amount of counts recursively. 
    Returns the initial number that first equals or exceeds the end value
    Preconditions: goal>-0  ,  count>0,    a == 0
    Postconditions: None
    '''
    if(find_end_rec(a,count)>goal):
        return a
    else:
        return acc_find_start_rec(goal,count,a+1)


def find_start_rec(goal, count):
    '''
    Wrapper function that allows the recursively version of finding the start value to run with an accumulator and
    still follow the lab restrictions:

    Preconditions: goal>=0, count>0
    '''

    return acc_find_start_rec(goal,count,0)




def find_start_iter(goal,count):
    '''
        Finds the best start value that corresponds to a end point and a given amount of counts iteratively. 
        Returns the initial number that first equals or exceeds the end value
        Preconditions: goal>-0  ,  count>0
        Postconditions: None
        '''
    val = 0
    while(True):
        if(find_end_iter(val,count)>goal):
            return val
        else:
            val = val +1



def gen_tests():
    '''
    Generates test cases for all of the functions
    '''

    print('Recursive: end: 0 intitial, count 10:  ', find_end_rec(0,10))
    print('Iterative: end: 0 intitial, count 10:  ', find_end_iter(0, 10))
    
    print('Recursive: end: 10 intitial, count 0:  ', find_end_rec(10, 0))
    print('Iterative: end: 10 intitial, count 0:  ', find_end_iter(10, 0))

    print('Recursive: end: 0 intitial, count 100:  ', find_end_rec(0, 100))
    print('Iterative: end: 0 intitial, count 100:  ', find_end_iter(0, 100))

    print('Recursive: start: 103 intitial, count 4:  ', find_start_rec(103, 4))
    print('Iterative: start: 103 intitial, count 4:  ', find_start_iter(103, 4))

    print('Recursive: start: 100 intitial, count 3:  ', find_start_rec(100, 3))
    print('Iterative: start: 100 intitial, count 3:  ', find_start_iter(100, 3))

    print('Recursive: start: 49 intitial, count 2:  ', find_start_rec(49, 2))
    print('Iterative: start: 49 intitial, count 2:  ', find_start_iter(49, 2))

    print('Recursive: start: 60 intitial, count 7:  ', find_start_rec(60, 7))
    print('Iterative: start: 60 intitial, count 7:  ', find_start_iter(60, 7))


    print('Recursrive: Sequence: Seed 0, count 10')
    print_sequence_rec(0,10)

    print('Iterative: Sequence: Seed 0, count 10')
    print_sequence_iter(0,10)

    print('Recursrive: Sequence: Seed 3, count 65')
    print_sequence_rec(3,65)

    print('Iterative: Sequence: Seed 3, count 65')
    print_sequence_iter(3,65)

    print('Recursrive: Sequence: Seed 12, count 6')
    print_sequence_rec(12, 6)

    print('Iterative: Sequence: Seed 12, count 6')
    print_sequence_iter(12, 6)


gen_tests()
