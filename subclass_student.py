class Child(object):
  def __init__(self, name):
    self.name = name
"""
class Student(Child):
  def __init__(self, name, roll):
    self.roll = roll
"""
class Student(Child):
  def __init__(self, name, roll):
    self.roll = roll
    # initialize the superclass 'Child' and pass the name
    Child.__init__(self, name)

a = Child("bubu")
b = Student("fanfan", 12)
print(b.name)
print(b.roll) 
