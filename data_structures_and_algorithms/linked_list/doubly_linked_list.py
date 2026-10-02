class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Add at end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Add at beginning
    def prepend(self, data):
        new_node = Node(data)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    # Delete a node
    def delete(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                # If node is head
                if temp.prev is None:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
                return
            temp = temp.next

        print("Value not found")

    # Display forward
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Display backward
    def display_backward(self):
        temp = self.head

        if temp is None:
            return

        # Go to last node
        while temp.next:
            temp = temp.next

        # Traverse backward
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


# ==============================
# Test
# ==============================

if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append("A")
    dll.append("B")
    dll.append("C")

    print("Forward:")
    dll.display_forward()

    print("Backward:")
    dll.display_backward()

    print("\nAfter prepend:")
    dll.prepend("Start")
    dll.display_forward()

    print("\nAfter delete 'B':")
    dll.delete("B")
    dll.display_forward()