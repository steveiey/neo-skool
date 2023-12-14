In Python, lists are a collection of items  
We store values inside of lists  
The values of the items can be of different [[Type]]s  
**Order matters** in a list

# Creating a List
To make a list, we use brackets \[\] to surround our list  
We separate the individual items with commas

```python
some_list = ["Jimmy", "Sara", "Frederique"]
```

# Access Elements in the List
We can access the individual things from lists using **bracket notation**  
In the example below, we'll use bracket notation to access "Sara"  

```python
some_list[1]          # "Sara"
some_list[0]          # "Jimmy"
some_list[2]          # "Frederique"
some_list[-1]         # "Frederique"  counts from the end
some_list[-2]         # "Sara"
```

Inside the brackets, we give the *index* of the item we want  
Python uses **0-index** counting, which means we start counting at 0

### 2D lists

all list used before are 1D 

```python
list = ["sus","smogus"]
```

make 2D lists, aka lists in a list

```python
2D_list = [
	["sus","smogus"],
	["uagagagagagagagagagagaga","jhjfdhjfdkjfdkgfdhjgfjkgdfkgfghjgdfkjghdjk"],
	["harahhhhhnm","umami"]
]

2D_list[0][0] = "sus"
2D_list[0][1] = "smogus"
```

### Tuples
tuples are constants and cannot be changed
brackets for a bracket
() for a tuple

### Images
a pixel in stored in a tuple with 3 values

image = (red,green,blue)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)