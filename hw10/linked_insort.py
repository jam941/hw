"""
file: linked_insort.py
author: Jarred Moyer
description: homework
"""

from hw10 import linked_code


def insert(value, lnk):
    """
    Put the value in the proper spot in the linked list to keep it sorted.
    New nodes are created.
    :param value: the value to add to the sequence of values in the list
    :param lnk: the node at the head of the list
    :return: a (partially) new linked list with the value inserted
    :pre: the list headed by lnk is sorted.
    :post: the link returned refers to a list that is sorted.
    """
    if lnk == None:
        pass
    else:
        if (value < lnk.value):
            return linked_code.LinkNode(value, lnk)
        elif lnk != None:
            return linked_code.LinkNode(lnk.value,insert(value,lnk.rest))



def insort(lnk):
    """
    Return a copy of a linked list where all the values are sorted,
    with the lowest value at the head.
    :param lnk: the node at the head of the provided list
    :return: the head node of the sorted linked list
    """
    if lnk == None:
        return None
    sorted_lnk = linked_code.LinkNode(lnk.value,None)
    lnk = lnk.rest
    while lnk != None:

        value = lnk.value
        sorted_lnk = insert(value,sorted_lnk)
        lnk = lnk.rest

    return sorted_lnk






def pretty_print(lnk):
    """
    Print the contents of a linked list in standard Python format.
    [value, value, value] (Note the spaces.)
    :param lnk: the node at the head of the provided list
    :return: None
    """
    string = '['

    if(lnk == None):
        print('[]')
    else:
        while lnk != None:

            val = lnk.value

            string = string + str(val)+','
            lnk = lnk.rest
        string = string[:-1]
        string = string + ']'
        print(string)



