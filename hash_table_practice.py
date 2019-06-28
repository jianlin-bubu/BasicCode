class Node(object):
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

class MyDict(object):
  def __init__(self, capacity):
    self.capacity = capacity
    self.hash_table = [None for _ in range(capacity)]

  def put(self, key, value):
    hash_code = hash(key)
    index = hash_code%self.capacity
    if self.hash_table[index] == None:
      self.hash_table[index] = Node(key, value)
    else:
      current_node = self.hash_table[index]
      key_found = False
      while current_node != None:
        if current_node.key == key:
          current_node.value = value
          key_found = True
          break
        else:
          previous_node = current_node
          current_node = current_node.next
      if not key_found:
          previous_node.next = Node(key, value)

  def get(self, key):
      hashcode = hash(key)
      index = hashcode%self.capacity
      current_node = self.hash_table[index]
      while current_node != None:
        if current_node.key != key:
          current_node = current_node.next
        else:
          return current_node.value

dic = MyDict(10)
dic.put(2,2)
dic.put(3,3)
dic.put(3,4)

print dic.get(2)

