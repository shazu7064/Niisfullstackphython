class Node:
	def __init__(self,ele):
	    self.prev=None
	    self.data=ele
	    self.next=None
f=Node(10)
s=Node(20)
t=Node(30)
f.pray=None
f.next=s
s.prev=f
s.next=t
t.prev=s
t.next=None
print("element forward")
ptr=f
while ptr.next!=None:
	print(ptr.data)
	ptr=ptr.next
print(ptr.data)
print("element in backward")
while ptr!=None:
	print(ptr.data)
	ptr=ptr.prev

	
