from dataclasses import dataclass
from typing import Any, Union


@dataclass(frozen=True)
class LinkNode:
    value: str
    rest: Union[None, 'LinkNode']


def convert_to_node(str):
    if str:
        return LinkNode(str[0], convert_to_node(str[1:]))
    else:
        return None


def is_match(seq_1, seq_2):
    if (seq_1 == None and seq_2 == None):
        return True
    elif seq_1 == None or seq_2 == None:
        return False
    elif seq_1.value != seq_2.value:
        return False
    else:
        return is_match(seq_1.rest, seq_2.rest)


def concatenate(lnk1, lnk2):
    if lnk1 == None:
        return lnk2
    else:
        return LinkNode(lnk1.value, concatenate(lnk1.rest, lnk2))


def insetion(idx, seq_1, seq_2):
    if idx == 0:
        return concatenate(seq_2, seq_1)

    elif seq_1 == None:
        raise IndexError("Invalid Insertion Index")
    else:
        return LinkNode(seq_1.value, insetion(idx - 1, seq_1.rest, seq_2))



def convert_to_string_accum(seq,a):
    if seq == None:
        return a
    else:
        a.append(seq.value)
        return convert_to_string_accum(seq.rest,a)


def convert_to_string(seq):
    lst =  convert_to_string_accum(seq, [])
    st = ''
    for i in lst:
        st = st + i
    return st

def is_pairing(seq1,seq2):
    if seq1 == None and seq2 == None:
        return True
    elif seq1 == None or seq2 == None:
        print()
        return False
    else:
        dic = {}
        dic['A'] = 'T'
        dic['T'] = 'A'
        dic['G'] = 'C'
        dic['C'] = 'G'
        if(dic[seq1.value] == seq2.value):
            return is_pairing(seq1.rest,seq2.rest)
        else:
            print('No match')
            return False



seq1 = convert_to_node('A')
seq2 = convert_to_node('T')
print(is_pairing(seq1,seq2))
