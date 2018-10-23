

def input_data():
    f = open('words.txt')
    lst = []
    for i in f:
        lst.append(i[:-1])

    return lst

def lex(letters):
    lst = []
    for i in letters:

        lst.append(i)

    return sorted(lst)




def configure_key(data):
    dic = {}
    for i in data:

        dic[i].append(lex(i))


    return dic

def find_words(letters,check):
    sorted_letters = lex(letters)



    pass
def main():
    lex('bench')
    check = configure_key(input_data())
    print(check['bad'])
    #w1 = input('What letters would you like to unscramble')
    #w1_results = find_words(w1,check)

main()