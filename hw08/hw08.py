"""
File: HW08.py
Author: Jarred Moyer
Language: Python3
Description: Test and compares various sorting methods using their time to sort on various data sets.
Assignment: hw08
"""

import random
import time
import insertion_sort
import quick_sort
import merge_sort

def get_list1(n):
    """
    :param n: the length of a list
    :return: a list with random elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L+[random.random()]
    return L

def get_list2(n):
    """
    :param n: the length of a list
    :return: a list with many repeated elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L+[random.randint(1,100)]
    return L


def get_list3(n):
    """
    Expected behavior of quick sort: poor
    :param n: the length of a list
    :return: a list of elements increasing overall
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.random()*i]
    return L

def get_list4(n):
    """
    :param n: the length of a list
    :return: a list with many zeros but neither increasing nor decreasing
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.randint(-8, 8)*i]
    return L
def get_pivot(lst):
    '''
    Finds the pivot value to use in quick-merge sort. Accounts for occasions where the half string may be empty
    Paramaters: lst must be a list
    Returns: An integer or empty list representing the pivot value
    '''
    if(lst == []):
        return []
    else:
        return lst[0]

def quick_merge_sort(lst):
    '''
    Sorts an unsorted list using a hybrid of quick and merge sort
    Parameters: lst must be a list
    Returns: Sorted list
    '''
    if lst == []:
        return []
    half1,half2 = merge_sort.split(lst)
    (less1,same1,more1) = quick_sort.partition(get_pivot(half1),half1)
    (less2, same2, more2) = quick_sort.partition(get_pivot(half1),half2)
    lst1 = quick_merge_sort(less1) + same1 + quick_merge_sort(more1)
    lst2 = quick_merge_sort(less2) + same2 + quick_merge_sort(more2)
    return merge_sort.merge(lst1,lst2)

def test_merge_quick_sort():
    '''
    Tests the quick-merge hybrid sort with a randomly generated data set of integers.
     Prints the sorted and unsorted data set.
    '''
    data = get_list2(20)
    print('Quick_merege_sort unsorted data: ', data)
    print('')
    print('quick_merge_sort sorted data: ', quick_merge_sort(data))


def test_compare():
    '''
    Tests all four insert, merge, quick, and merge-quick sorting methods on four data sets. Prints the sorting
    time in console
    '''
    print('Testing with list 1, random elements')
    lst = get_list1(10000)
    start = time.time()
    quick_sort.quick_sort(lst)
    end = time.time()
    print('Quick sort elapsed: ', end-start, 'seconds')
    start = time.time()
    merge_sort.merge_sort(lst)
    end = time.time()
    print('Merge_sort elapsed: ', end - start, 'seconds')
    start = time.time()
    insertion_sort.insertion_sort(lst)
    end = time.time()
    print('Insertion sort elapsed: ', end - start, 'seconds')
    print('')

    print('Testing with list 2, repeated elements')
    lst = get_list2(10000)
    start = time.time()
    quick_sort.quick_sort(lst)
    end = time.time()
    print('Quick sort elapsed: ', end - start, 'seconds')
    start = time.time()
    merge_sort.merge_sort(lst)
    end = time.time()
    print('Merge_sort elapsed: ', end - start, 'seconds')
    start = time.time()
    insertion_sort.insertion_sort(lst)
    end = time.time()
    print('Insertion sort elapsed: ', end - start, 'seconds')
    start = time.time()
    quick_merge_sort(lst)
    end = time.time()
    print('Merge quick sort elapsed: ', end - start, 'seconds')
    print('')


    print('Testing with list 3, Overall increasing elementss, not favorable to quick sort')
    lst = get_list3(10000)
    start = time.time()
    quick_sort.quick_sort(lst)
    end = time.time()
    print('Quick sort elapsed: ', end - start, 'seconds')
    start = time.time()
    merge_sort.merge_sort(lst)
    end = time.time()
    print('Merge_sort elapsed: ', end - start, 'seconds')
    start = time.time()
    insertion_sort.insertion_sort(lst)
    end = time.time()
    print('Insertion sort elapsed: ', end - start, 'seconds')
    start = time.time()
    quick_merge_sort(lst)
    end = time.time()
    print('Merge quick sort elapsed: ', end - start, 'seconds')
    print('')


    print('Testing with list 4, not favorable to quick sort')
    lst = get_list4(10000)
    start = time.time()
    quick_sort.quick_sort(lst)
    end = time.time()
    print('Quick sort elapsed: ', end - start, 'seconds')
    start = time.time()
    merge_sort.merge_sort(lst)
    end = time.time()
    print('Merge_sort elapsed: ', end - start, 'seconds')
    start = time.time()
    insertion_sort.insertion_sort(lst)
    end = time.time()
    print('Insertion sort elapsed: ', end - start, 'seconds')
    start = time.time()
    quick_merge_sort(lst)
    end = time.time()
    print('Merge quick sort elapsed: ', end - start, 'seconds')
    print('')

    print('Time comparison finished')

test_merge_quick_sort()
test_compare()

