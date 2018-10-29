import time
def import_data(path):
    f = open(path)
    lst = []
    for i in f:
        count = 0
        num = i.split()
        lst.append(int(num[1]))
    print(lst)
    return lst
def partition(pivot,lst):
    smaller = []
    same = []
    bigger = []
    for i in lst:

        if i>pivot:
            bigger.append(i)
        elif i<pivot:
            smaller.append(i)
        else:
            same.append(i)
    return smaller,bigger,same


def quick_select(data,k):

    if data != []:
        #print(data)

        pivot = data[(len(data)//2)]
        print('Pivot: ', pivot )
        small,big,same = partition(pivot,data)
        m = len(small)
        count = len(same)

        if k>= m and k < count:
            print('FINISHED: ', pivot)
            return pivot
        elif m>k:
            return quick_select(small,k)
        else:
            return quick_select(big,k-m-count)

def find_med(data):

    length  = int(len(data))


    if(length%2 == 0):
        pos1 = quick_select(data, 0)
        pos2 = quick_select(data, len(data) - 1)
        print(pos1)
        print(pos2)
        return ((pos1+pos2)/2)
    else:

        return quick_select(data,length/2)

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


