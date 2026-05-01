#单链表模板：实现单链表的增删改查
class ListNode:  #创建节点
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.len=0
    
    def get_size(self):
        return self.len
    
    def insert(self,pos,val):
        if pos<0 or pos>self.get_size():
            raise ValueError('Invalid position')
        NewList=ListNode(val)
        if pos==0:
            NewList.next=self.head
            self.head=NewList
        else:
            prev=self.head
            for _ in range(pos-1):
                prev=prev.next
            NewList.next=prev.next
            prev.next=NewList
        self.len+=1
    
    def delete(self,pos):
        if pos<0 or pos>self.len:
            raise ValueError('Invalid position')
        if pos==0:
            self.head=self.head.next
        else:
            prev=self.head
            for _ in range(pos-1):
                prev=prev.next
            prev.next=prev.next.next
        self.len-=1

    def update(self,pos,newval):
        if pos<0 or pos>self.len:
            raise ValueError('Invalid position')
        current=self.head
        for _ in range(pos):
            current=current.next
        current.val=newval
    
    def search(self,val):
        current=self.head
        pos=0
        while current.val!=val and pos<self.len:
            current=current.next
            pos+=1
        if current.val==val:
            return current
        return None
    
    def index(self,val):
        current=self.head
        pos=0
        while current.val!=val and pos<self.len:
            pos+=1
            current=current.next
        if current.val==val:
            return pos
        return -1
    
    def display(self):
        current=self.head
        while current:
            print(current.val,end='->')
            current=current.next
        print('None')

def test():
    c=LinkedList()
    for i in range(10):
        c.insert(i,i*i)
    c.delete(3)
    c.update(4,666)
    c.display()
test()