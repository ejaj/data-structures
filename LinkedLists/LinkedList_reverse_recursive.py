class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        rest = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return rest

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp:
            linkedListStr = (linkedListStr +
                             str(temp.data) + " ")
            temp = temp.next
        return linkedListStr


# Driver code
linkedList = LinkedList()
linkedList.push(20)
linkedList.push(4)
linkedList.push(15)
linkedList.push(85)

print("Given linked list")
print(linkedList)

linkedList.head = linkedList.reverse(linkedList.head)

print("Reversed linked list")
print(linkedList)