class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self, value):
        new_node = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = self.linkedList.tail = new_node
        else:
            self.linkedList.tail.next = new_node
            self.linkedList.tail = new_node

    def isEmpty(self):
        return self.linkedList.head is None

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty."
        removed_node = self.linkedList.head
        if self.linkedList.head == self.linkedList.tail:
            self.linkedList.head = self.linkedList.tail = None
        else:
            self.linkedList.head = self.linkedList.head.next
        return removed_node

    def peek(self):
        if self.isEmpty():
            return "Queue is empty."
        return self.linkedList.head

    def delete(self):
        self.linkedList.head = self.linkedList.tail = None
