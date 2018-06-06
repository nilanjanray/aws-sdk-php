import pdb
class A(object):
  def __init__(self, department, age):
    self.department = department
    self.age = age
  def __call__(self, function):
    #pdb.set_trace()
    sometuple = ('ML', 'aaa', 'LAMP',) if (self.age > 50) else ('rrr', 'ggg', 'yyy',)
    #sometuple = ('ML', 'aaa', 'LAMP',)
    print(type(function))
    return function(*sometuple)
    #pdb.set_trace()
    #return self.func(tehcnology, name, stack) 
    #pdb.set_trace()

"""signatures = ('Statistics', 100,)
@A(*signatures)
def helloworld(technology, name, stack):
  print(technology)
"""
#sometuple = ('ML', 'aaa', 'LAMP',)
#helloworld(*sometuple)

def moreouter(func):
  def oneinner():
    #print(type(func[0]()))
    sig = ('Nilanjan', 100, 'Blue',)
    func[2](*sig)
  return oneinner, oneinner()

def outer(func):
  def inner():
    sig = ('Nilanjan', 100, 'Red',)
    func(*sig)
  return inner, inner(), func


"""@moreouter
@outer
def checkthis(name, age, color):
  print(color)
"""

import itertools
#sig = ('Nilanjan', 100, 'Red',)
#checkthis(*sig)
def section(**kwords):
  #self.kwords = kwords
  print('section')
  print(kwords)

#Foo = type('Foo', (), dict(a=(lambda c: (value for value in c))([2222,4444])))
Foo = type('Foo', (), dict(a=section))
print(type(Foo.a))
"""
All version compatible 2 & 3 when a method is an instance menthod/lambda anoynomus
"""
#Bar = type('Bar', (Foo,), dict(b=lambda self: self.a(name='Python', stack='Lamp')))
"""
Only compatible with version -3 need to check if it's work with 3.4
"""
Bar = type('Bar', (Foo,), dict(b=Foo.a(name='Python', stack='Lamp')))
#print([value for value in itertools.chain(Bar().b())])
Bar().b
