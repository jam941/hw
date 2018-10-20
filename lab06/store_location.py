import math
def import_data(path):
    f = open(path)
    data = []
    line = f.readline()

    
    return data

def quick_sort(data):

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

def find_med(lst):
    sort = quick_sort(lst)
    length  = len(lst)
    if(length%2 == 0):
        return (lst[length/2]+lst[length/2 -1])/2
    else:
        return lst[int(length/2)]

def distance(lst, shop):
    sum = 0
    for i in lst:
        #sum += abs(i-shop)
        pass
    return sum


def main():
    #path = input('What file would you like to open?  ')
    path = 'data'
    data = import_data(path)
    print(data)
    shop = find_med(data)

    total_distance = distance(data,shop)
    print('The optimal shop placement is at ',shop)
    print('The total distances to offices is ',total_distance)

main()


