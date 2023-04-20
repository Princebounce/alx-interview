# Pascal's Triangle Generator
##This function generates the Pascal's triangle of a given number.

Usage
**To use this function, call it with an integer argument:**
```
result = pascal_triangle(5)
print(result)
```

**The output will be a list of lists representing the Pascal's triangle of 5:**
```
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
```
If the argument is less than or equal to 0, an empty list will be returned.

Example
**Here's an example of how to use this function:**
```
from pascal_triangle import pascal_triangle

result = pascal_triangle(7)
print(result)
```

**The output will be:**
```
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1]
]
```
