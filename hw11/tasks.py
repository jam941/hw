from dataclasses import dataclass
from priority_queue import *
'''
Author: Jarred Moyer <jam4936@rit.edu>
Title: tasks.py
Language: python3
Description: Tests priority queue functions
Assignment: HW 11
'''

@dataclass()
class Task:
    name: str
    priority: int



q = make_priority_queue()
enqueue(q, Task('Task1', 5))
enqueue(q, Task('Task2', 7))
t = front(q)
#print(t)
print("Highest priority task is", t.name, "with priority", t.priority)
t = back(q)
print("Lowest priority task is", t.name, "with priority", t.priority )
print('Now printing entire que')
while not is_empty(q):
    t = front(q)
    dequeue(q)
    print('Task', t.name, 'With priority ', t.priority)


q = make_priority_queue()
enqueue(q, Task('Task1', 5))
enqueue(q, Task('Task2', 7))
enqueue(q,Task('Task3',1))
t = front(q)
#print(t)
print("Highest priority task is", t.name, "with priority", t.priority)
t = back(q)
print("Lowest priority task is", t.name, "with priority", t.priority )
print('Now printing entire que')
while not is_empty(q):
    t = front(q)
    dequeue(q)
    print('Task', t.name, 'With priority ', t.priority)



q = make_priority_queue()


t = front(q)
#print(t)
print("Highest priority task is", t.name, "with priority", t.priority)
t = back(q)
print("Lowest priority task is", t.name, "with priority", t.priority )
print('Now printing entire que')
while not is_empty(q):
    t = front(q)
    dequeue(q)
    print('Task', t.name, 'With priority ', t.priority)

q = make_priority_queue()
enqueue(q,Task('Task3',1))
t = front(q)
#print(t)
print("Highest priority task is", t.name, "with priority", t.priority)
t = back(q)
print("Lowest priority task is", t.name, "with priority", t.priority )
print('Now printing entire que')
while not is_empty(q):
    t = front(q)
    dequeue(q)
    print('Task', t.name, 'With priority ', t.priority)


