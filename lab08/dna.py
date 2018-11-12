from dataclasses import dataclass
from typing import Any, Union

'''
Author: Jarred Moyer <jam4936@rit.edu>
Title: dna.py
Language: python3
Description: Uses linked nodes to model dna
Assignment: Lab 8
'''


@dataclass(frozen=True)
class LinkNode:
    value: str
    rest: Union[None, 'LinkNode']


def convert_to_nodes(str):
    '''
    Converts a string to a linked list
    :param str: a string
    :return: a node representing the string
    '''
    if str:
        return LinkNode(str[0], convert_to_nodes(str[1:]))
    else:
        return None


def is_match(seq_1, seq_2):
    '''
    Checks if two linked lists match
    :param seq_1: linked list
    :param seq_2: linked list
    :return: boolean verdict
    '''
    if (seq_1 == None and seq_2 == None):
        return True
    elif seq_1 == None or seq_2 == None:
        return False
    elif seq_1.value != seq_2.value:
        return False
    else:
        return is_match(seq_1.rest, seq_2.rest)


def concatenate(lnk1, lnk2):
    '''
    Concatenates two linked lists
    :param lnk1: linked list
    :param lnk2: linked list
    :return: concatenated linked list
    '''
    if lnk1 == None:
        return lnk2
    else:
        return LinkNode(lnk1.value, concatenate(lnk1.rest, lnk2))



def insertion( n1,n2,idx):
    '''
    inserts a sequence at a given sequence of another function
    :param n1: linked sequence
    :param n2:  linked sequence
    :param idx: non-negative integer
    :return: linked list with operation preformed
    '''
    if idx == 0:
        return concatenate(n2,n1)
    if n1 == None:
        raise TypeError('One sequence is none')
    else:
        return LinkNode(n1.value, insertion(n1.rest,n2,idx-1))

def convert_to_string_accum(seq,a):
    '''
    converts a string to a node. Helper function for the convert_to_string function
    :param seq:
    :param a: Must be 0
    :return: string representing the linked sequence seq
    '''
    if seq == None:
        return a
    else:
        a.append(seq.value)
        return convert_to_string_accum(seq.rest,a)


def convert_to_string(seq):
    '''
    Converts a node to a string
    :param seq: a linked sequence
    :return: string representing the values of the linked sequence
    '''
    lst =  convert_to_string_accum(seq, [])
    st = ''
    for i in lst:
        st = st + i
    return st

def is_pairing(seq1,seq2):
    '''
    Compares two sequences to see if they have the corresponding bases in the correct spots

    :param seq1: A linked list
    :param seq2: A linked List
    :return: boolean verdict
    '''
    dic = {}
    dic['A'] = 'T'
    dic['T'] = 'A'
    dic['G'] = 'C'
    dic['C'] = 'G'
    if seq1 == None and seq2 == None:
        return True
    elif seq1 == None or seq2 == None:

        return False
    else:

        if(dic[seq1.value] == seq2.value):
            return is_pairing(seq1.rest,seq2.rest)
        else:

            return False

def palindrome(n1,n2):
    '''
    Helper function for is_palindrome. Checks to lists to see if they match
    Preconditions: n2 must be the reversed version n1
    :param n1: linked sequence
    :param n2: linked sequence
    :return: boolean verdict
    '''
    if n1 == None and n2 == None:
        return True
    elif n1.value == n2.value:
        return palindrome(n1.rest,n2.rest)

    else:
        return False
def reverse(node):
    '''
    Reverses a given node.
    :param node: A linked list
    :return: A reversed linked list
    '''
    if node == None:
        return None
    else:
        return concatenate(reverse(node.rest),LinkNode(node.value,None))
def is_palindrome(node):
    '''
    Checks to see if a node is a palindrome
    :param node: a linked list
    :return: a boolean statement on if a sequence is a palindrome
    '''
    node1 =  node
    node2 =  reverse(node)

    return palindrome(node1,node2)




def substitution(node,idx,base):
    '''
    Substititues the elelment of a linked list at a given index for with a new element
    :param node: A linked list
    :param idx: integer: index to operate at
    :param base: string: what to replace item at index i with
    :return: new linked list
    '''
    if idx == 0:
        return LinkNode(base,node.rest)
    elif node != None:
        return LinkNode(node.value,substitution(node,idx-1,base))




def deletion(n1,i,size):
    '''
    Deletes the element at a given index and over a size
    :param n1: A linked sequence
    :param i: integer: index to operate at
    :param size: integer: amount of elements to operate on.
    :return:
    '''
    if n1 == None:
        return None
    if i == 0:
        if size == 0:

            return LinkNode(n1.value,n1.rest)
        else:
            return deletion(n1.rest, 0, size - 1)

    elif n1 != None:
        return LinkNode(n1.value,deletion(n1.rest,i-1,size))
    else:
        return None

def dupe(n1, size):
    '''
    Helper function for duplication calculates the section of nodes that must be duplicated
    :param n1: a node
    :param size: the amount of indexes to be copied
    :return:
    '''
    if size != 0:
        return LinkNode(n1.value,dupe(n1.rest,size-1))
    else:
        return  None

def duplication(n1,idx,size):
    '''
    Duplicates a node at a given index and a given amount of index afterwards
    :param n1: linked list.
    :param idx: integer
    :param size: integer
    :return: node with operation preformed.
    '''
    if n1 == None:
        return None
    elif idx == 0:
        n2 = dupe(n1,size)
        n2 = concatenate(n2,n2)

        return concatenate(n2,n1.rest.rest)

    elif n1 != None:
        return LinkNode(n1.value,duplication(n1.rest,idx-1,size))
    else:
        return None




