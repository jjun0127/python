# Asterisk(\*)
##### Definition
* Unpacking something.

# \*args
#### Definition
* You can use \*args when arguments are not fixed, but flexible

#### How to use
```Python
def foo(*args):
  print args

mylist = [1, 2, 3]
foo(*mylist)
```

# \*\*kwargs
#### Definition
* Keyword arguments.
* Dictionary must have keys corresponding to arguments of method

#### How to use
```Python
def foo(name, age): ## def foo(**kwargs) , this is possible too
  print name

mylist = {'name' : 'Junha', 'age' : 26}
foo(**mylist)
```
