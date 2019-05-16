# Run time analysis
## Task0
The run time for this task is constant **O(1)** because we already know the address for the given element

## Task1
The run time for this senario is:
```
n*2 + n*2
```
Resulting in:
```
4n -> O(n)
```

## Task2
The run time for this task is **O(n)** because we are doing one iteration over the calls array

## Task3
For both scenarios, A and B, the run time is **O(n)** because we are iterating the calls array one time

## Task4
The run time is **O(n^2 + n)** because in the method discardNumbers() we are iterating one time over the
calls array and one time over the texts array, resulting in:
```
n + n = 2n
```

For the second method identifyTelemarketPhone() we are iterating one time over the calls array
and one time over the set we populated in the previous method. The worst case for iterating a
set is O(n) resulting in:
```
n * n -> o(n^2)
```

Finally
```
2n + n^2 -> O(n^2 + 2)
```

