from dataclasses import dataclass
'''
Author: Jarred Moyer <jam4936@rit.edu>
Title: moving.py
Language: python3
Description: Attempts to sort items into various sized boxes using loops, and custom dat structures. 
Assignment: Lab 7
'''

@dataclass()
class item:
    '''
    Item class that defines an item
    has atributes weight and name
    '''

    name: str
    weight: int


@dataclass()
class boxes:
    '''
    Boxes store items. Contains a list of items, a maximum capacity, and a capacity remaining.
    '''
    capacity: int
    remaining_cap: int
    items: list


def import_data(path):
    '''
    Imports data from the file specified by a parameter. Formats data into data structures
    :param path: must be string
    :return: returns an list of items and a list of boxes
    '''
    box_list = []
    item_list = []
    lst = []
    file = open(path)
    line = file.readline()
    lst = line.split()
    for i in lst:
        bx = boxes(int(i), int(i), [])
        box_list.append(bx)
    for line in file:
        lst = line.split()
        it = item(lst[0], int(lst[1]))
        item_list.append(it)
    return box_list, item_list


def vertical_print(lst, misfit):
    '''
    Prints data vertically rather than horizontally
    :param lst: list of packed boxes. Must be a list.
    :param misfit: list of items that couldn't make it into boxes
    :return: None
    '''
    count = 1
    for i in lst:
        print('Box number ', count, 'with capacity', i.capacity, 'contains:')
        for k in i.items:
            print('  ', k.name, 'of weight', k.weight)
        # print(' Box number', count, 'Has a remaining', i.remaining_cap, 'capacity')
        count += 1
    for l in misfit:
        print(l.name, 'of weight', l.weight, 'got left behind')


def sort_data(lst, order):
    '''
    Preforms a quick sort on a list of items
    :param lst: a list only containing items
    :param order: Boolean: true for sorting biggest to smallest, false for smallest to biggest
    :return: sorted list
    '''
    if not lst:
        return []

    pivot = lst[0].weight

    less, same, more = [], [], []

    for i in lst:
        var = i.weight

        if var > pivot:
            more.append(i)
        elif var < pivot:
            less.append(i)
        else:
            same.append(i)
    if (order):
        return sort_data(more, order) + same + sort_data(less, order)
    else:
        return sort_data(less, order) + same + sort_data(more, order)


def strat1(boxes, items):
    '''
    Sorts data using the roomiest strategy
    :param boxes: A list of boxes
    :param items: A list of Items
    :return: A list of filled boxes and a list of items that couldn't fit
    '''
    sorted_items = sort_data(items, True)
    unsorted = []
    for i in sorted_items:

        test_cap = 0
        best = 0
        count = 0
        fit = False
        for k in boxes:
            cap = k.remaining_cap

            if (cap >= test_cap and cap >= i.weight):
                fit = True
                best = count
                test_cap = cap
            count += 1
        if (fit):
            boxes[best].items.append(i)
            boxes[best].remaining_cap = boxes[best].remaining_cap - i.weight
        else:
            unsorted.append(i)
            print('NOT ABLE TO FIT: ', i)
    return boxes, unsorted


def strat2(box_data, item_data):
    '''
    Sorts data using the tightest fit strategy
    :param boxes: A list of boxes
    :param items: A list of Items
    :return: A list of filled boxes and a list of items that couldn't fit
    '''
    sorted_items = sort_data(item_data, True)
    unsorted = []
    for i in sorted_items:

        best_cap = 0
        best_idx = 0
        count = 0
        fit = False
        for k in box_data:

            if (k.remaining_cap - i.weight >= best_cap and k.remaining_cap - i.weight >= 0):
                fit = True
                best_cap = k.remaining_cap - i.weight
                best_idx = count
            count += 1
        if fit:
            box_data[best_idx].items.append(i)
            box_data[best_idx].remaining_cap = box_data[best_idx].remaining_cap - i.weight
        else:
            unsorted.append(i)

    return box_data, unsorted


def strat3(box, item):
    '''
    Sorts data using the roomiest strategy
    :param boxes: A list of boxes
    :param items: A list of Items
    :return: A list of filled boxes and a list of items that couldn't fit
    '''
    items = sort_data(item, True)
    for select in box:
        idx = 0
        while True:
            if idx == len(items):
                break
            elif select.remaining_cap >= items[idx].weight:
                select.remaining_cap -= items[idx].weight
                select.items.append(items[idx])
                items.pop(idx)
            else:
                idx += 1

    return box, items


def clear_boxes(lst):
    '''
    clears a box and resets it's remaining capacity
    :param lst: list of boxes
    :return: reset list of boxes
    '''
    for i in lst:
        i.items.clear()
        i.remaining_cap = i.capacity
    return lst


def main():
    '''
    Prompts user for a file to import. Formats the file and then tries various greedy strategies on it.
    :return: None
    '''
    path = input('Enter file name: ')
    box_data, item_data = import_data(path)
    print('Sorting using strategy 1')
    data, misfit = strat1(box_data, item_data)
    if misfit != []:
        print('Unable to pack all items!!!!')
    vertical_print(data, misfit)
    print('\n \n \n')

    print('Sorting using strategy 2')
    box_data = clear_boxes(box_data)
    data, misfit = strat2(box_data, item_data)
    if misfit != []:
        print(misfit)
        print('Unable to pack all items!!!!')
    vertical_print(data, misfit)
    print('\n \n \n')

    print('Sorting using strategy 3')
    box_data = clear_boxes(box_data)
    data, misfit = strat3(box_data, item_data)
    if misfit == []:
        print('Unable to pack all items!!!!')
    vertical_print(data, misfit)


main()
