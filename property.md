# @Property
#### Definition
* JAVA can hide variables from outside using __private__ variables
* like this, python can hide variables using __property__ decorator

```python
class C(object):
            @property
            def x(self):
                "I am the 'x' property."
                return self._x
            @x.setter
            def x(self, value):
                self._x = value
            @x.deleter
            def x(self):
                del self._x

# How to Use
myclass = C()
myclass.x = 3 # setter called
print x       # property called
```
