class Rectangle(object):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def size(self):
    return self.width * self.width

  def ifSquare(self):
    return self.width == self.height

class Square(Rectangle):
  def __init__(self, side):
    self.side = side
    Rectangle.__init__(self, side, side)

r1 = Rectangle(4,3)
print r1.size()
print r1.ifSquare()

s1 = Square(4)
print s1.ifSquare()
print s1.size()
# cannot write it as pring s1.width()
print s1.width
