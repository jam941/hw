'''
Author: Jarred Moyer <jam4936@rit.edu>
Title: anagrams.py
Language: python3
Description: Uses file reading, looping, lists, and dictionaries, assists a user cracking anagram puzzles
Assignment: Homework 09
'''


def input_data():
    '''
    Inputs data from a text file and converts it to a list where each element is one line.
    Returns: a list containing the data from the file.
    '''
    f = open('american-english.txt', encoding='utf8')
    lst = []
    for i in f:
        lst.append(i[:-1])

    for k in lst:
        if k[0].isupper():
            fix = k[0].lower()
            k = (fix + k[1:])

    return lst


def lex(letters):
    '''
    Takes a list of letters and orders them  lexicographically
    Parameters: letters must be a string
    Returns the sorted string
    '''

    s = sorted(letters)
    val = ''.join(s)
    return val


def configure_key(data):
    '''
    Takes a list of strings and converts it into a dictionary where the key is
    the string sorted lexicographically and the value is a list of strings that have that
    sorted value

    Parameters: data must be a list
    returns a dictionary.
    '''
    l = ['ate', 'tea', 'eta', 'eat']
    dic = {}
    for i in data:
        k = lex(i)

        if (k in dic):

            dic[k].append(i)

        else:
            dic[k] = [i]

    return dic


def phase_2(check):
    '''
    Countinously asks the user to input a string to be checked for possible decoded message.
    The input does not have to be lexicographically sorted.
    Parameters: check must be a dictionary
    '''
    while True:
        word = input('What string of characters should be decoded? Press enter to go to task 2 : ')
        l = lex(word)

        if (l == ''):
            break
        if l in check:
            print(check[l])
        else:
            print('Error, no word corresponds to the string', word)


def get_anagram_count(check, length):
    '''
    Compiles a list of words that area ll identical when lexicographically sorted and of the same length.
    Parameters: Check must be a dictionary to check against, length must an integer.
    Returns: a list of all words that have a common sorted value and are the same length.
    '''
    best = []
    for i in check:

        if len(i) == length and len(check[i]) > len(best):
            best = check[i]

    return best


def phase_3(check):
    '''
    Countinously asks the user to input a string to be checked for decoded message sets given
    a word length
    Parameters: check must be a dictionary
    '''
    while True:
        length = input('Enter word length or press enter to go to task 4: ')
        if (length == ''):
            break
        length = int(length)
        best = get_anagram_count(check, length)
        print('Max anagrams for length ', length, ':', len(best))
        print('Anagram list: ', best)


def phase_4(check):
    '''
    Checks for the amount of possible scramble words until the user inputs an empty string
    Parameters: check must be a dictionary.
    '''
    while True:
        length = input('Enter a word length or press enter to quit : ')
        if (length == ''):
            break
        count = 0
        for i in check:

            if len(i) == int(length) and len(check[i]) == 1:
                count += 1

        print('Number of usable jumbled words with length 5 is: ', count)


def main():
    '''
    Countinously asks the user for inputs to process.
    Phase two checks for possible decoded words.
    Phase three checks for words that share the same sorted value and length
    Phase four checks for possible scramble words of a given length
    In all modules, the user specifies when they are done via pressing enter in an empty input

    '''
    check = configure_key(input_data())
    phase_2(check)
    print('')
    phase_3(check)
    print('')
    phase_4(check)


main()
