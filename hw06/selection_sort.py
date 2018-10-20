'''
Author: Jarred Moyer <jam4936@rit.edu>
Title: selection_sort.py
Language: python3
Description: Uses selective sorting to sort a list from a file specified by the user.
Assignment: Hw07

1: Insertion sort preforms better than selection sort the more sorted the list is initially.
    For example: the test case [1,2,3,4,6,5,7,9,8] will sort faster in insertion sort rather than
    substitution sort.
2: Insertion sort only moves numbers that must be moved, while substitution sort will always move
all but one number at least once.
'''
def get_next_idx(lst):
    '''
    Takes a list and returns the index of its smallest value
    '''
    best = int(lst[0])
    best_count = 0
    count = 0
    for i in lst:

        if i < best:
            best = i
            best_count = count
        count += 1
    return best_count



def selection_sort(data):
    '''
    Sorts a list by the paramater data using selection sort. returns the sorted list
    data must be a list
    '''


    for i in range(0,len(data)):
        x = get_next_idx(data[i:])
        sliced = data[i:]
        if(x!=0):
            y = data[i]
            data[i] = data[x+i]
            data[x+i] = y
        else:
            pass
    return data


def import_data(path):
    '''
    Converts a text file into a list of numbers.
    returns a list where each cell is one line from the file
    path must be a string
    '''
    f = open(path)
    lst = []
    for i in f:
        lst = lst + [int(i)]


    return lst

def main():
    '''
    Queries the user for a file to sort, then sorts the numbers from said file. prints the unsorted and sorted file.
    :return:
    '''
    path = input('What file would you like to sort?:  ')
    data = import_data(path)
    print('Initial list: ', data)
    print(' Sorted list: ',selection_sort(data))

main()