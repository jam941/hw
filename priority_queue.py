from hw11 import node

from dataclasses import dataclass
from typing import Union



@dataclass
class PriorityQueue:
    size: int
    front: Union[None, node.Node]
    back: Union[None, node.Node]


def make_priority_queue():
    return PriorityQueue(0, None, None)


def is_empty(queue):
    return queue.front == None


def front(queue):
    if is_empty(queue):
        raise IndexError('no front in empty queue')
    print(queue.front)
    return queue.front.value


def back(queue):
    if is_empty(queue):
        raise IndexError('back of empty queue')
    return queue.back.value


def enqueue(queue, element):
    if is_empty(queue):
        return insert(queue, element)
    priority = element.priority
    if back(queue).priority > priority:
        insert(queue, element)
        return None
    count = 0

    size = queue.size
    while queue.back != None:

        if priority > front(queue).priority:

            insert(queue, element)
            break

        else:

            trans_el = dequeue(queue)

            insert(queue, trans_el)
            count += 1

    size = size - count

    while size > 0:
        trans_el = dequeue(queue)

        insert(queue, trans_el)

        size -= 1


def insert(queue, element):
    newnode = node.Node(element, None)
    if queue.front == None:
        queue.front = newnode
    else:
        queue.back.rest = newnode
    queue.back = newnode
    queue.size = queue.size + 1


def dequeue(queue):
    if is_empty(queue):
        raise IndexError("dequeue on empty queue")
    removed = queue.front.value
    queue.front = queue.front.rest
    if is_empty(queue):
        queue.back = None
    queue.size = queue.size - 1
    return removed




