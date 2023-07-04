# 0x09. Python - Everything is object

## Tasks

### 0. Who am I?


What function would you use to get the type of an object?

### 1. Where are you?



How do you get the variable identifier (which is the memory address in the CPython implementation)?


### 2. Right count



```
>>> a = 89
>>> b = 100

```



### 3. Right count =


```
>>> a = 89
>>> b = 89

```



### 4. Right count =


```
>>> a = 89
>>> b = a

```


### 5. Right count =+



```
>>> a = 89
>>> b = a + 1

```



### 6. Is equal



```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

```



### 7. Is the same


```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

```



### 8. Is really equal


```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

```



### 9. Is really the same


```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)

```



### 10. And with a list, is it equal



```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)

```



### 11. And with a list, is it the same



```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)

```


### 12. And with a list, is it really equal

```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)

```



### 13. And with a list, is it really the same


```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

```



### 14. List append




```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

```


### 15. List add




```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

```



### 16. Integer incrementation


```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)

```


### 17. List incrementation


```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

```


### 18. List assignation




```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

```



### 19. Copy a list object


Write a function `def copy_list(l):` that returns a **copy** of a list.




### 20. Tuple or not?



```
a = ()

```



### 21. Tuple or not?



```
a = (1, 2)

```


### 22. Tuple or not?



```
a = (1)

```


### 23. Tuple or not?



```
a = (1, )

```





### 24. Who I am?





```
a = (1)
b = (1)
a is b

```


### 25. Tuple or not


What does this script print?

```
a = (1, 2)
b = (1, 2)
a is b

```

### 26. Empty is not empty



What does this script print?

```
a = ()
b = ()
a is b

```


### 27. Still the same?


```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)

```




### 28. Same or not?



```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)

```





