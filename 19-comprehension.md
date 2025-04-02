# Comprehension
---

## ✅ 1. **List Comprehension**

### 🔹 Basic Syntax:
```python
[expression for item in iterable if condition]
```

### 🧪 Examples:

#### Example 1: Square of numbers
```python
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]
```

#### Example 2: Even numbers from a list
```python
nums = [1, 2, 3, 4, 5]
evens = [x for x in nums if x % 2 == 0]
# [2, 4]
```

#### Example 3: Convert to uppercase
```python
fruits = ["apple", "banana", "cherry"]
upper = [fruit.upper() for fruit in fruits]
# ['APPLE', 'BANANA', 'CHERRY']
```

---

## ✅ 2. **Tuple Comprehension (via Generator Expression)**

🔹 Python **doesn't have tuple comprehensions** directly. Use **generator expressions** with `tuple()` to get a tuple.

### 🧪 Example:

```python
gen = (x**2 for x in range(3))   # Generator
tup = tuple(gen)
# (0, 1, 4)
```

---

## ✅ 3. **Dictionary Comprehension**

### 🔹 Basic Syntax:
```python
{key_expression: value_expression for item in iterable if condition}
```

### 🧪 Examples:

#### Example 1: Number to square mapping
```python
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

#### Example 2: Uppercase keys from a list
```python
names = ['alice', 'bob', 'carol']
d = {name: name.upper() for name in names}
# {'alice': 'ALICE', 'bob': 'BOB', 'carol': 'CAROL'}
```

#### Example 3: Filtering items
```python
ages = {'alice': 25, 'bob': 17, 'carol': 30}
adults = {k: v for k, v in ages.items() if v >= 18}
# {'alice': 25, 'carol': 30}
```

---
