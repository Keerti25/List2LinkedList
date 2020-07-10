class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
        
    def add(self,data):
        node=Node(data)
        pointer = self.head
        while pointer.next:
            pointer=pointer.next
        node.next=pointer.next
        pointer.next=node

    def delete(self,dat):
        pointer = self.head
        nextv = pointer.next
        
        while pointer:
            print(nextv.data)
            if nextv.data == dat:
                pointer.next=nextv.next
                nextv.next = None
                return "Node Deleted"
            pointer = pointer.next
            nextv = nextv.next

    def addAtbeg(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def display(self):
        pointer = self.head
        while pointer:
            print(pointer.data)
            pointer = pointer.next

    def update(self,dat,val):
        pointer = self.head
        while pointer:
            if pointer.data == dat:
                pointer.data = val
            pointer = pointer.next
            
    def length(self):
        pointer = self.head
        count = 0
        while pointer:
            pointer = pointer.next
            count = count+1
        return count


def isSame(link1,link2):
    pointer1 = link1.head
    pointer2 = link2.head
    if link1.length()==link2.length():
        while pointer1:
            if pointer1.data!=pointer2.data:
                return "It is not palindrome"
            else:
                return "It is Palindrome"
    else:
        return "It is not Palindrome"
    
def palindrome(l):
        point = l.head
        lnk = LinkedList()
        while point:
            lnk.addAtbeg(point.data)
            point = point.next
        lnk.display()
        return isSame(l,lnk)

def convert_list2palindrome(a):
    lk = LinkedList()
    lk.addAtbeg(a[0])
    for i in range(1,len(a)):
        lk.add(a[i])
    return lk

a = int(input("Enter the length of list: "))
lst=[]
for i in range(a):
    s = int(input("Enter %ith element of list: "%(i+1)))
    lst.append(s)
print("List:",lst)
lks=convert_list2palindrome(lst)
print("List converted into linkedlist: ")
lks.display()
print("============LENGTH of LINKEDLIST============")
print(lks.length())
print("======DELETION of NODE====================")
d = int(input("Enter the value of node to be deleted: "))
lks.delete(d)
print("After deletion: ")
lks.display()
print("========UPDATING NODE=====================")
print("Now,update the linked list: ")
u=int(input('Enter value of node to be updated: '))
v = int(input('Enter new value of node: '))
lks.update(u,v)
print("Updated linked list: ")
lks.display()
print("============CHECKING PALINDROME=============")
print(palindrome(lks))
