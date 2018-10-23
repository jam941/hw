from dataclasses import dataclass

@dataclass()
class item:
    name:str
    weight:int
@dataclass()
class boxes:
    capacity:int
    remaining_cap:int
    items: list

def import_data(path):
    box_list = []
    item_list = []
    lst = []
    file = open(path)
    line = file.readline()
    lst = line.split()
    for i in lst:
        bx = boxes(int(i),int(i),[])
        box_list.append(bx)
    for line in file:
        lst  = line.split()
        it = item(lst[0],int(lst[1]))
        item_list.append(it)
    return box_list,item_list

def sort_data(lst):
    return sorted(lst, 'weight',)
def strat1(boxes,items):
    sorted_items = sort_data(items)

    for i in sorted_items:

        test_cap = 0
        best = 0
        count = 0
        for k in boxes:
            cap = k.remaing_cap()

            if(cap>test_cap):
                best = count
                test_cap = cap
            count += 1
        boxes[best].items.append(i)
        boxes[best].remaining_cap = boxes[best].remaining_cap - i.weight


data = import_data('data.txt')
print(data)
print('Line break to show next is sorted         S')
print(sort_data(data))