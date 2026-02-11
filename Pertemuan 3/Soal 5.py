class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # Membalik linked list tanpa membuat list baru
    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next_node = temp.next 
            temp.next = prev       
            prev = temp            
            temp = next_node     

        self.head = prev        

# ------------------
# Contoh Penggunaan 
# ------------------

print("Contoh 1:")
ll = LinkedList()
for x in [1, 2, 3, 4, 5]:
    ll.insert_at_end(x)

print("Linked List sebelum dibalik:")
ll.display()

ll.reverse()

print("Linked List setelah dibalik:")
ll.display()


print("\nContoh 2:")
ll2 = LinkedList()
for x in [10, 20, 30, 40]:
    ll2.insert_at_end(x)

print("Linked List sebelum dibalik:")
ll2.display()

ll2.reverse()

print("Linked List setelah dibalik:")
ll2.display()


print("\nContoh 3:")
ll3 = LinkedList()
ll3.insert_at_end(7)

print("Linked List sebelum dibalik:")
ll3.display()

ll3.reverse()

print("Linked List setelah dibalik:")
ll3.display()
