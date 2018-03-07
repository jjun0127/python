# Decorators
* Python decorator wrap the method
* Decorators return wrapped method
```Python
def elapsed_time(functor):
    def decorated():
        start = time.time()
        functor()
        end = time.time()
        print "Elapsed time: %f" % (end - start)
    return decorated
```
```Python
@elapsed_time
def hello():
    print 'hello'
```
##### Result
```
/usr/bin/python2.7 /home/junha/Documents/develop/python_test/testt.py
123
hello
Elapsed time: 0.000002
```
