"""
Python Iterators
An iterable is an object that can be iterated over, 
meaning that you can traverse through all the values.


An iterator is an object that contains a countable number of values.


An iterator is an object that can be iterated upon, 
meaning that you can traverse through all the values.


Technically, in Python, an iterator is an object which implements the iterator protocol, 
which consist of the methods __iter__() and __next__().
An object is called iterable if we can get an iterator from it.
All these objects are iterable, meaning you can get an iterator from them:
- lists
- tuples
- dictionaries
- sets
- strings
- etc.

Iterator vs Iterable
Iterables are objects that you can iterate over, 
meaning that you can traverse through all the values.

An iterator is the object that does the actual iterating.
Iterables have the __iter__() method which is used to get an iterator.
All these objects are iterable, meaning you can get an iterator from them:
- lists
- tuples
- dictionaries
- sets
- strings
- etc.  

"""


my_tupple = ("joe", "john", "doe", "ice")

print(hasattr(my_tupple, "__iter__"))




class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)




class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)