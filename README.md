# Run time analysis
## Task0
The run time for this task is constant **O(1)** because we already know the address for the given element

## Task1
The run time for this senario is:
```
n + n
```
Because we are doing two iterations, using two for loops
Resulting in:
```
2n -> O(n)
```

## Task2
The run time for this task is **O(n)** because first we iterate one time over the calls array
to track the seconds spent on a call and populate the timeRecord dictionary. Then we iterate one more time over the timeRecord dictionary to compare which phone spent the longest time.
```
n + n = 2n
```
Leading to **O(n)**

## Task3
Because we are iterating the calls array one time and then making a second iteration when sorting,
the run time is:
```
n + n log n
```
resulting in **O(n)** 

## Task4
The run time is **O(n^2 + n)** because in the method discardNumbers() we are iterating one time over the
calls array and one time over the texts array, resulting in:
```
n + n = 2n
```

For the second method identifyTelemarketPhone() we are iterating one time over the calls array
and one time for the sorting function. Although we iterate over the set we populated in the previous method, the average case scenario is o(1) when iterating a set. Resulting in:
```
n + n log n + 1 -> O(n + n log n)
```

Finally
```
2n + n + n log n = 3n + n log n  -> O(n + n log n)
```


>Dictionaries and sets in python are implemented using hashmaps. The worst-case scenario for item lookup or adding an item or removing one, is technically O(n).
>However, that worst-case scenario rarely ever happens ( https://stackoverflow.com/questions/1963507/time-complexity-of-accessing-a-python-dict ). So for all purposes, it's more accurate to consider the average case scenario which is O(1).