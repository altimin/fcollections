[<img src="https://travis-ci.org/altimin/fcollections.svg?branch=master"/>](https://travis-ci.org/altimin/fcollections)


# fcollections - functional collections for python

Motivation behind this library is to write long chain of map/filter sequence transformations without pain. To achieve that this library provides wrappers around standard python collections with additional methods defined.

Currently two wrappers are implemented -- `Iterable` and `List`.

### Iterable

`Iterable` wraps any iterable entity and provides methods to work with it.

Of course, .filter(), .map() and .reduce() methods are provided:

```python
>>> Iterable([4, 3, -1, 2, 1]).filter(lambda x: x > 0).map(str).reduce(str.__add__)
'4321'
```

.count method counts objects :) Argumentless .count() returns collections.Counter:
```python
>>> Iterable([1, 1, 1, 5, 5, 3]).count()
Counter({1: 3, 5: 2, 3: 1})
```
and .count(object) method returns number of occurences for this specific value:
```python
>>> Iterable([1, 1, 1, 5, 5, 3]).count(5)
2
```

Also there are many methods inspired by itertools module:

```python
>>> Iterable([4, 3, -1, 2, 1]).groupby(lambda x: x % 2)
{0: [4, 2], 1: [3, -1, 1]}
```

```python
>>> Iterable([4, 3, -1, 2, 1]).drop(1).take(2).list()
[-1, 2]
```

```python
>>> Iterable([4, 3, -1, 2, 1]).dropuntil(lambda x: x < 0).list()
[-1, 2, 1]
```

```python
>>> Iterable([4, 3, 4, 1, 1, 4]).unique().list()
[4, 3, 1]
```

There are also some methods which compute scalar value: `min`, `max`, `len`, `all`, `any`.

### List

List wraps, well, standard python list. Obviously, List is also an Iterable and has all methods Iterable does. All operators are wrapped to, so adding List to a standard list results in a List.

Some methods like `sort`, returning None for standard list, return self for List resulting in more chaining possible:

```python
>>> List([3, 2, 1]).append(-1).sort().map(lambda x: x**3).list()
 [-1, 1, 8, 27]
```

### Plans for future
* Wrappers for the rest of standard python collections (dict, set, Counter).
* DictOfLists class to do cool things with result of .groupby().
* .plot() methods (inspired by .plot() method from pandas)

Any ideas are appreciated!
