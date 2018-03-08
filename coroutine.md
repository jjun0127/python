# Coroutine
#### Definition
* A special type of Generator Using __yield__ as input
* The same as normal generator, stop when encountering __yield__
* Use __send__ function as input of Coroutine.

#### Sample code

```python
def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr

    return start


# Example use
if __name__ == '__main__':
    @coroutine
    def grep(pattern):
        print "Looking for %s" % pattern
        while True:
            line = (yield)
            if pattern in line:
                print line,

    g = grep("python")
    # Notice how you don't need a next() call here
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
```

#### Refer to
* http://pyengine.blogspot.kr/2011/07/python-coroutine-2.html
