import time
'''
Author: Jarred Moyer <jam4936@rit.edu>
Title: store_location.py
Language: python3
Description: Uses file reading, looping, and lists, to calculate the optimum position fo a shop. Uses 
quick sort rather than quick select. 
Assignment: Lab 6
'''
def import_data(path):
    '''
    Imports data from a file and formats it for further processing
    Path must be a string
    Returns a list of numbers from the file
    '''
    f = open(path)
    lst = []
    for i in f:
        count = 0
        num = i.split()
        lst.append(int(num[1]))

    return lst

def quick_sort(data):
    '''
    Preforms a quick sort on a list
    Data must be a list
    Returns the sorted list
    '''
    if data == []:
        return data
    else:

        pivot = data[0]

        less  = []
        same = []
        more = []

        for i in data:
            if i > pivot:
                more.append(i)
            elif i<pivot:
                less.append(i)
            else:
                same.append(i)

        return quick_sort(less) + same + quick_sort(more)

def find_med(data):
    '''
    Finds the optimum shop placement
    data must be a list
    '''
    lst = quick_sort(data)

    length  = int(len(lst))
    if(length%2 == 0):
        end = time.time()
        print(end)
        return int(lst[int(length/2)]+lst[int(length/2) -1])/2
    else:
        end = time.time()
        return int(lst[int(length/2)])

def distance(lst, shop):
    '''
    Calculates the distance between a list of offices and the shop
    lst must be a list, shop must be a number
    '''
    sum = 0
    for i in lst:
        dis = abs(shop-i)
        sum += dis
    return sum


def main():
    '''
    Calculates the optimimim shop placement and its distance to each building.
    '''
    path = input('What file would you like to open?: ')

    data = import_data(path)
    start = time.time()
    shop = find_med(data)
    end = time.time()
    elapsed = end-start
    total_distance = distance(data,shop)
    print('The optimal shop placement is at ',shop)
    print('The total distances to offices is ',total_distance)
    print('Elapsed time : ', elapsed)

main()


