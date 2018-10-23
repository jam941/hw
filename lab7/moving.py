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

