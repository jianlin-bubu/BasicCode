class Person(object):
    def __init__(self, name):
        self.name = name
        self.d = {}
    def think(self, key):
        print 'I think %s' % self.d[key]

bubu = Person('bubu')
bubu.d['love'] = 'fan'
bubu.think('love')
