"""
file: test_link_sort.py
author: Jarred Moyer
description: tester for functions in linked_insort.py
"""

from hw10 import linked_insort
from hw10 import linked_code


def read_file( fname ):
    """
       Open a file of containing one integer per line,
       prepend each integer to a linked sequence,
       and return the reverse of the sequence.
       :param fname: A string containing the name of the file
       :return: A linked list of the numbers in the file, ordered
                identically to how they are ordered in the file
    """
    f = open(fname)
    lst = []
    for i in f:
        lst.append(int(i))
    node = linked_code.mk_linked_list_rec(lst)
    return node


def main():
    """
       Read file, build sequence, print it, sort it, print result, and
       pretty-print both lists.
    """

    name = input( "Enter file name: " )
    if name == "":
        return

    original_s = read_file( name )
    print( "unsorted:", original_s )

    sorted_s = linked_insort.insort( original_s )

    print( "sorted:", sorted_s )

    print( "pretty printed original: ", end="")
    linked_insort.pretty_print( original_s )
    print( "pretty printed sorted: ", end="")
    linked_insort.pretty_print( sorted_s )



if __name__ == "__main__":
    main()
