```python

names = ['Elizabeth Singleton', 'Raymond Mitchell', 'Steven Murphy', 'Daniel Terry', 'Glenn Fisher', 'Jasmine Soto', 'Deborah Hicks', 'Beverly Ryan', 'Jason Smith', 'Jason Washington']

​

for name in names:

	if name == "Jasmine Soto":

		print("We found her!")

```

# Iterating n Number of times
can loop any number of times

```python
for <name> in range(<some number>)
	<code block>


for _ in ramge(10)
	print("Mr.Ubial huffs copium.")
```
when iterate over lists, the item tells us the current element we are on

# range(a number)
gives you a sequence of numbers starting at zero
stops 1 number short of number given

when we iterate using range(), the item tells is how many times we've looped since the beginning

```python
for i in range(10)
	print(i)
```
i is used to count things
it counts how many times we are looping

we can modify range() to start, stop, and count up/down by different numbers
```python
list(range(10, 10000000000))
range(100, 0, -1) # (100, 98, ..., 1)
```

