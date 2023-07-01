# Create, Insert and Print Linkedlist


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # def reverseListUsingTwoPointers(self, head):
    #     prev, curr = None, head
    #     while curr:
    #         nxt = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = nxt
    #     return prev

    # def reverseListUsingRecursive(self, head):
    #     if not head:
    #         return None
    #     newHead = head
    #     if head.next:
    #         newHead = self.reverseListUsingRecursive(head.next)
    #         head.next.next = head
    #     head.next = None
    #     return newHead


LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.print()
