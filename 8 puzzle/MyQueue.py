class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class MyQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.N = 0

    def clear(self):
        self.first = None
        self.last = None
        self.N = 0

    def is_empty(self):
        return self.first is None

    def size(self):
        return self.N

    def peek(self):
        if self.is_empty():
            raise NoSuchElementException("Queue underflow")
        return self.first.item

    def enqueue(self, item):
        old_last = self.last
        self.last = Node(item)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last
        self.N += 1

    def dequeue(self):
        if self.is_empty():
            raise NoSuchElementException("Queue underflow")
        item = self.first.item
        self.first = self.first.next
        self.N -= 1
        if self.is_empty():
            self.last = None
        return item

    def __iter__(self):
        return self.ListIterator(self.first)

    class ListIterator:
        def __init__(self, first):
            self.current = first

        def __iter__(self):
            return self

        def __next__(self):
            if not self.has_next():
                raise StopIteration
            item = self.current.item
            self.current = self.current.next
            return item

        def has_next(self):
            return self.current is not None

    def add_queue(self, queue):
        if not queue.is_empty():
            old_first = self.first

            if self.is_empty():
                self.first = queue.first
                self.last = queue.last
            else:
                self.first = queue.first
                queue.last.next = old_first

            self.N += queue.size()

class NoSuchElementException(Exception):
    pass
