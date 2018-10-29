from dataclasses import dataclass


@dataclass()
class item:
    name: str
    weight: int


@dataclass()
class boxes:
    capacity: int
    remaining_cap: int
    items: list


def import_data(path):
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


def vertical_print(lst,misfit):
    count = 1
    for i in lst:
        print('Box number ', count, 'with capacity', i.capacity , 'contains:')
        for k in i.items:
            print('  ',k.name , 'of weight', k.weight)
        #print(' Box number', count, 'Has a remaining', i.remaining_cap, 'capacity')
        count += 1
    for l in misfit:
        print(l.name, 'of weight', l.weight, 'got left behind')


def sort_data(lst, order):
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


def strat3(box_data, item_data):
    sorted_items = sort_data(item_data, True)

    unsorted = []
    for i in box_data:

        for k in sorted_items:

            if i.remaining_cap >= k.weight:
                i.items.append(k)
                i.remaining_cap = i.remaining_cap - k.weight
                sorted_items.remove(k)
    print(sorted_items)
    for i in sorted_items:
        unsorted.append(i)
    return box_data, unsorted


def main():
    path = input('Enter file name: ')
    box_data, item_data = import_data(path)

    data, misfit = strat3(box_data, item_data)
    if not misfit:
        print('Unable to pack all items!!!!')
    vertical_print(data,misfit)



main()
