class Node(object):
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None


class MyDict(object):
  def __init__(self, capacity):
    self.capacity = capacity
    self._hash_table = [None for _ in range(capacity)]

  def put(self, key, value):
    hashcode = hash(key)
    index = hashcode%len(self._hash_table)
    if self._hash_table[index] == None:
      self._hash_table[index] = Node(key, value)
    else:
      current_node = self._hash_table[index]
      key_found = False
      while current_node != None: 
        if current_node.key != key:
          previous = current_node
          current_node = current_node.next
        else:
          current_node.key = key
          key_found = True
          break
      if key_found == False:
        previous.next = Node(key, value)

  def get(self, key):
    hashcode = hash(key)
    index = hashcode%len(self._hash_table)
    current_node = self._hash_table[index]
    while current_node.key != key:
      current_node= current_node.next
    return current_node.value

  def visualize(self):
    """
    2  4  N  6  N  N
    8        7
    10
    """
    vis = [None for _ in range(self.capacity)]
    for i in range(self.capacity):
      current_node = self._hash_table[i]
      if current_node:
        vis[i] = [current_node.key]
        while current_node.next != None:
          current_node = current_node.next
          vis[i].append(current_node.key)
      else:
        vis[i] = ["N"]              

    res = ""
    max_length = 1
    for i in vis:
      if len(i) > max_length:
        max_length = len(i)
        print max_length
    for i in range(max_length):
      res += (2 * (len(vis) - 1) + len(vis)) * "x"+"\n"
    print res
    for i in range(len(vis)):
      print i 
      for n in range(len(vis[i])):
      print n
        res.replace(res[i * len(vis) + n], str(vis[i][n]))
    return res 
       

d = MyDict(10)
d.put(1,1)
d.put(3,2)
d.put(3,3)
d.put(5,5)
d.put(10,10)
d.put(15,15)
d.put(20,20)
d.put(50,50)
print d.visualize()
