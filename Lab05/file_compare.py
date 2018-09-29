def get_line_count(f):
    count = 0
    for i in f:
        for k in i:
            if(k == '\n'):
                count += 1
    return count

def get_file_length(f):
    count = 0
    f = open(f)
    for i in f:

        for k in i:

            count += 1
    return count


def char_by_char(file_1, file_2):
    count = 1
    mismatch = 0
    mismatch_line = 0
    f1 = open(file_1)
    f2 = open(file_2)

    for p in range(0,3):
        f1_data = f1.readline()

        f2_data = f2.readline()

        if(len(f1_data)!=len(f2_data)):
            mismatch_line += 1
            print('Mismatched line: ', count)
        else:

            for i in range(0,len(f1_data)-1):

                if(f1_data[i] == f2_data[i]):

                    pass
                else:
                    print('Unmatched Characters:')
                    print('Line: ', count ,'Char: ', i +1 )
                    mismatch += 1

        count += 1
    print('File ', file_1, 'is ', get_file_length(file_1))
    print('File ', file_2, 'is ', get_file_length(file_2))
    print('There were ', mismatch, 'mismatched characters')
    print('There were', mismatch_line, 'Mismatched line lengths' )
char_by_char('t1.txt','t2.txt')
