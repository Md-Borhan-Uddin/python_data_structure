class Node:
  def __init__(self,val,next=None):
    self.val = val
    self.next = next

class Linklist:
  def __init__(self) -> None:
    self.head = None
    self.size = 0
    self.__last = None

  def _itration(self):
    items = []
    h = self.head
    while h is not None:
      items.append(h.val)
      h  = h.next
    return items
  
  def __repr__(self) -> str:
    return f'Linklist{self._itration()}'

  
  def __str__(self) -> str:
    return self.__repr__()

  def __len__(self):
    return self.size

  def push(self,val):
    node = Node(val)
    if self.size > 0:
      self.__last.next = node
    else:
      self.push_head(val)
    self.size +=1
    self.__last = node
    return self

  
  def __iter__(self):
    h = self.head
    while h is not None:
      yield h.val
      h  = h.next
  
  def push_head(self,val):
    node = Node(val)
    if self.head is None:
      self.head = node
      self.__last = node
    else:
      node.next = self.head
      self.__last = self.head
      self.head = node
    self.size +=1
    
    return self




l = Linklist()


l.push_head(6)
l.push_head(1)
l.push(4)
l.push_head(8)
print(l)

for i in l:
  print(i)