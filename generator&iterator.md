# Iterator
#### Definition
* iterate : 반복하다

#### iterable Object
  * List, Set, Dictionary

#### How to make a 'Class' to be iterable
  * define \__iter\__ , \__next\__ (special method, DUNDER method)

#### For Loop
* Iterable objects can be used at 'for loop' by calling 'next' method.
  * ex) "`for a in ["1", "2", "3"]`"

# Generator
#### Definition
* Generator is a special form of Iterator
* Every generator should stop at __yield__, and __yield__ give result partially whenever __next__ method is called.

#### When to use
* Data is too big to return at once, so need to return partially.

#### Example
* sample code below
```python
def generator():
   yield 1
   yield 2
   yield 3
```
```python
g = generator()
print(type(g)) #class generator
n = next(g)
n = next(g)
n = next(g)
```
```python
for x in generator():
    print(x)
```

### Refer to
* http://pythonstudy.xyz/python/article/23-Iterator%EC%99%80-Generator
