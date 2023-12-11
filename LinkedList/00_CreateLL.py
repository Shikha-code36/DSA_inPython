class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_end(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.display()

    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and index > 1:
                current = current.next
                index -= 1

            temp_next = current.next
            current.next = new_node
            new_node.next = temp_next

        self.display()

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.display()

    def remove_first_node(self):
        if self.head:
            self.head = self.head.next
        self.display()

    def remove_last_node(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        self.display()

    def remove_at_index(self, index):
        if index == 0:
            self.remove_first_node()

        current = self.head
        while current and index > 1:
            current = current.next
            index -= 1

        current.next = current.next.next
        self.display()

    def update_node(self, new_data, index):
        current = self.head
        while current and index > 1:
            current = current.next
            index -= 1
        
        current.data = new_data
        self.display()

    def size(self):
        count = 0
        current = self.head
        while current:
            count+=1
            current=current.next
        
        return count

    def display(self):
        elements = []
        current = self.head

        while current:
            elements.append(current.data)
            current = current.next

        string_elements = [str(element) for element in elements]
        joined_string = " -> ".join(string_elements)
        print(joined_string)


# Create a linked list
my_list = LinkedList()

# Append elements
my_list.insert_at_end(1)
my_list.insert_at_end(2)

# Insert at the end
my_list.insert_at_end(3)

# Insert at an index
my_list.insert_at_index(5, 2)

# Insert at the beginning
my_list.insert_at_beginning(0)

# Remove the first node
my_list.remove_first_node()

# Remove the last node
my_list.remove_last_node()

# Remove at an index
my_list.remove_at_index(1)

# Update a node
my_list.update_node('z', 0)

# Print the size of the linked list
print("\nSize of linked list:", my_list.size())


