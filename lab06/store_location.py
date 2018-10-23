import math
def import_data(path):
    f = open(path)
    lst = []
    for i in f:
        count = 0
        print(i)
        for k in i:
            if(k.isdigit()):
                break
            count += 1
        lst.append((i[count:-1]))

    return lst

def quick_sort(data):

    if data == []:
        return data
    else:
        print(data)
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
    length  = int(len(lst))
    if(length%2 == 0):
        return int(lst[length/2]+lst[length/2 -1])/2
    else:
        return int(lst[int(length/2)])

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

    shop = find_med(data)

    total_distance = distance(data,shop)
    print('The optimal shop placement is at ',shop)
    print('The total distances to offices is ',total_distance)

main()


