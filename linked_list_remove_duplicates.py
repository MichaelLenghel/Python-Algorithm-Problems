class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next


    # Does not work perfectly when removing multiple duplicates side by side
    def removeDuplicates(self,head):
        previous = None
        current = head
        visited = set()
        
        while current:
            if current.data in visited:
                temp = previous.data
                while temp == current.data:
                    if current.next == None:
                        break
                    current = current.next
                if previous.data != current.data:
                    previous.next = current
                else:
                    previous.next = current.next
            else:
                # Add to set
                visited.add(current.data)
            previous = current
            current = current.next

        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 