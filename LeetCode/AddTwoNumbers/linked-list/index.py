# Constructor to initialize a new node with data
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Create the first node (head of the list)
head = Node(11)

# Link the second node
head.next = Node(22)

# Link the third node
head.next.next = Node(44)

# Link the fourth Node
head.next.next.next = Node(88)

temp = head
while temp is not None:
    print(f"\n{temp.data}\n", end=" ")
    temp = temp.next



