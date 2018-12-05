import node

from dataclasses import dataclass
from typing import Union



@dataclass
class PriorityQueue:
    size: int
    front: Union[None, node.Node]
    back: Union[None, node.Node]


def make_priority_queue():
    '''
    Makes an empty queue
    :return: empty queue
    '''
    return PriorityQueue(0, None, None)


def is_empty(queue):
    '''
    Checks to see if a que is empty
    :param queue: Must be a queue structure
    :return: boolean verdict
    '''
    return queue.front == None


def front(queue):
    '''
    Checks the front value of a queue
    :param queue: a queue
    :return: the value of the first node of a queue
    '''
    if is_empty(queue):
        raise IndexError('no front in empty queue')
    return queue.front.value


def back(queue):
    '''
    Checks the back value of a queue
    :param queue: a queue
    :return: the value of the last node of a queue
    '''
    if is_empty(queue):
        raise IndexError('back of empty queue')
    return queue.back.value


def enqueue(queue, element):
    '''
    enqueues a task into a que based on its priority
    :param queue: a queue
    :param element: a datastructure with an integer attribute priority
    :return: None
    '''
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
    '''
    Inserts a element into the back of a que
    :param queue: A queue
    :param element: Any element with a attribute priority
    :return: None
    '''
    newnode = node.Node(element, None)
    if queue.front == None:
        queue.front = newnode
    else:
        queue.back.rest = newnode
    queue.back = newnode
    queue.size = queue.size + 1


def dequeue(queue):
    '''
    Removes the item from the front of the queue
    :param queue: A queue
    :return: the object at the front of the queue that was removed
    '''
    if is_empty(queue):
        raise IndexError("dequeue on empty queue")
    removed = queue.front.value
    queue.front = queue.front.rest
    if is_empty(queue):
        queue.back = None
    queue.size = queue.size - 1
    return removed





