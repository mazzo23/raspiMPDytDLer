## toggle state:

https://stackoverflow.com/questions/8381735/how-to-toggle-a-value-in-python

### Solution using NOT

```
>>> x = True
>>> x = not x        # toggle
>>> x
False
>>> x = not x        # toggle
>>> x
True
>>> x = not x        # toggle
>>> x
False
```

### Solution using itertools  

```
>>> import itertools
>>> toggle = itertools.cycle(['red', 'green', 'blue']).next
>>> toggle()
'red'
>>> toggle()
'green'
>>> toggle()
'blue'
>>> toggle()
'red'
>>> toggle()
'green'
>>> toggle()
'blue'
```
