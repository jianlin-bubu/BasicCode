class Rectangle(object):
  def __init__(self, height, width):
    self.height = height
    self.width = width

  def size(self):
    return self.height * self.width

r1 = Rectangle(3,5)
r2 = Rectangle(2,4)

print r1.size()
print r2.size()
