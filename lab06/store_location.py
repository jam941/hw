import time
def import_data(path):
    f = open(path)
    lst = []
    for i in f:
        count = 0
        num = i.split()
        lst.append(int(num[1]))

    return lst

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

def find_med(data):

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
    sum = 0
    for i in lst:
        dis = abs(shop-i)
        sum += dis
    return sum


def main():
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


