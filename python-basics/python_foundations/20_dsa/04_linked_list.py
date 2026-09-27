class Node:
    def __init__(self, value, nxt=None):
        self.value, self.next = value, nxt

head = Node(1, Node(2, Node(3)))
cur = head
while cur:
    print(cur.value)
    cur = cur.next
