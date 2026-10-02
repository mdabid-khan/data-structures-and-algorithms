class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)


# Test
if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.display()

    s.push(7)
    s.push(77)
    s.display()

    s.pop()
    s.display()