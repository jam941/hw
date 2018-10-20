'''
Author: Jarred Moyer
Title: file_compare.py
Language: python3
Description: Uses file handling and for loops to compare two text files
Assignment: Lab 5
'''

def get_file_char_count(f):
    '''
    Gets the total character length of a file f

    Preconditions: f is an opened file. 
    Preconditions: None
    
    Returns the total amount of characters 
    '''
    count = 0
    f = open(f)
    for i in f:

        for k in i:
            if (k != '\n'):
                count += 1
    return count


def char_by_char(file_1, file_2):
    '''
    Compares two files, file_1 and file_2. Prints information regarding their similarities
    Preconditions: file_1 and file_2 are valid inputs
    Postconditions: None
    '''
    report_list = ''
    count = 1
    mismatch = 0
    mismatch_line = 1
    f1 = open(file_1)
    f2 = open(file_2)

    for p in range(0, 3):
        f1_data = f1.readline()

        f2_data = f2.readline()

        if (len(f1_data) != len(f2_data)):
            report_list = report_list + str(mismatch_line) + ',  '
            mismatch_line += 1
        else:

            for i in range(0, len(f1_data) - 1):

                if (f1_data[i] == f2_data[i]):

                    pass
                else:

                    report_list = report_list + (str(count) + ':' + str(i + 1) + ' , ')

                    mismatch += 1
            mismatch_line += 1
        count += 1

    print('mismatched cases: ', report_list)
    print('There are ', get_file_char_count(file_1), 'in ', file_1)
    print('There are ', get_file_char_count(file_2), 'in ', file_2)
    print('There were ', mismatch, 'mismatched characters in these files')
    print('There were', mismatch_line, ' lines of different length')
    f1.close()
    f2.close()


def main():
    '''
    Compares two files specified via a input
    '''
    file1 = input('What is the first file you would like to compare? (format as NAME.txt)  ')
    file2 = input('What is the second file you would like to compare? (format as NAME.txt)  ')
    char_by_char(file1, file2)

main()