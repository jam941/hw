"""
141 Tree Lab - Derp the Interpreter

Derp is a simple interpreter that parses and evaluates prefix expressions 
containing basic arithmetic operators (*,//,-,+).  It performs arithmetic with
integer only operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, produces the expression infix with 
parentheses to denote order of operation, and evaluates/produces the result of 
the expression.

Author: Scott C Johnson (scj@cs.rit.edu)

Author: Jarred Moyer
"""

from dataclasses import dataclass
from typing import Union


@dataclass
class LiteralNode:
    """Represents an operand node"""

    val: int


@dataclass
class VariableNode:
    """Represents a variable node"""

    name: str


@dataclass
class MathNode:
    """Represents a mathematical operation"""

    left: Union['MathNode', LiteralNode, VariableNode]
    op: str
    right: Union['MathNode', LiteralNode, VariableNode]


##############################################################################
# parse
############################################################################## 

def parse(tokens):
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    """
    val = tokens[0]
    if val.isdigit():
        return LiteralNode(int(val)), tokens[1:]
    elif val.isidentifier():
        return VariableNode(val), tokens[1:]
    else:
        left, lst = parse(tokens[1:])
        right, lst = parse(tokens)
        return MathNode(left, val, right)


##############################################################################
# infix
##############################################################################

def infix(node):
    """infix: Node -> String | TypeError
    Perform an inorder traversal of the node and return a string that
    represents the infix expression."""

    if isinstance(node, LiteralNode):
        return str(node.val)
    elif isinstance(node, VariableNode):
        return node.name
    else:

        left = node.left
        right = node.right
        val = node.operator

        string = '(' + infix(left) + val + infix(right) + ')'
        return string


##############################################################################
# evaluate
##############################################################################    

def evaluate(node, symTbl):
    """evaluate: Node * dict(key=String, value=int) -> int | TypeError
    Given the expression at the node, return the integer result of evaluating
    the node.
    Precondition: all variable names must exist in symTbl"""
    if isinstance(node,LiteralNode):
        val =  node.val
        return val
    elif isinstance(node,VariableNode):
        name = node.name
        return symTbl[name]
    else:
        op = node.operation

        if op == '//':
            return evaluate(node.left)//evaluate(node.right)
        elif op == '*':
            return evaluate(node.left) * evaluate(node.right)
        elif op == '+':
            return evaluate(node.left) + evaluate(node.right)
        else:
            return evaluate(node.left) - evaluate(node.right)






def make_table(file):
    f = open(file)
    dic = {}
    for i in f:
        l, r = i.split()
        dic[l] = int(r)
    return dic

def make_lst(string):
    lst = []
    for i in string:
        lst.append(i)
    return lst
##############################################################################
# main
##############################################################################

def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""

    print("Hello Herp, welcome to Derp v1.0 :)")

    inFile = input("Herp, enter symbol table file: ")

    table = make_table(inFile)

    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")

    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefixExp = input("derp> ")
        if prefixExp == "":
            break

        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        lst = make_lst(prefixExp)

        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF 
        # THE PARSE TREE.
        tree = parse(lst)

        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING.
        infix_exp = infix(tree)
        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.    
        print("Derping the infix expression:", infix_exp)

        # STUDENT: EVALUTE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        # INTEGER RESULT.
        solution= evaluate(infix_exp)
        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print("Derping the evaluation:")

    print("Goodbye Herp :(")


if __name__ == "__main__":
    main()
