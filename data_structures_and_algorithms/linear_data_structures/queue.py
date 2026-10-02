class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)


# Test
if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.display()

    q.enqueue(7)
    q.enqueue(77)
    q.display()

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.display()

    print(f"Peek: {q.peek()}")