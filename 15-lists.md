# Lists
---

## 🧾 What is a List?

A **list** in Python is a **collection** of items that is **ordered**, **mutable** (can be changed), and can hold **elements of different data types**.

### 📌 Creating a List

```python
# A list of numbers
numbers = [1, 2, 3, 4, 5]

# A list of strings
fruits = ['apple', 'banana', 'cherry']

# A mixed list
mixed = [1, 'hello', 3.14, True]
```

You can access elements using **indexing**:

```python
print(fruits[0])  # Output: apple
print(fruits[-1]) # Output: cherry (negative index = from end)
```

---

## 🔧 Built-in Functions for Lists

Here are some common and useful built-in functions and methods:

### 1. `len()`

Returns the number of elements in the list.

```python
len(fruits)  # Output: 3
```

---

### 2. `append()`

Adds an element **at the end** of the list.

```python
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
```

---

### 3. `insert(index, item)`

Inserts an item at a **specific index**.

```python
fruits.insert(1, 'mango')
print(fruits)  # Output: ['apple', 'mango', 'banana', 'cherry', 'orange']
```

---

### 4. `remove(item)`

Removes the **first occurrence** of the item.

```python
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'mango', 'cherry', 'orange']
```

---

### 5. `pop(index)`

Removes and returns the item at the given index. If no index is provided, removes the last item.

```python
last_item = fruits.pop()
print(last_item)  # Output: orange
print(fruits)     # Output: ['apple', 'mango', 'cherry']
```

---

### 6. `sort()`

Sorts the list **in-place** (changes the original list).

```python
numbers = [4, 2, 1, 3]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]
```

---

### 7. `sorted(list)`

Returns a **new sorted list** (original list is unchanged).

```python
nums = [4, 1, 5]
new_nums = sorted(nums)
print(new_nums)  # Output: [1, 4, 5]
print(nums)      # Output: [4, 1, 5]
```

---

### 8. `reverse()` and `reversed()`

- `reverse()` reverses the list in-place.
- `reversed()` returns a reversed iterator.

```python
nums = [1, 2, 3]
nums.reverse()
print(nums)  # Output: [3, 2, 1]

nums = [1, 2, 3]
print(list(reversed(nums)))  # Output: [3, 2, 1]
```

---

### 9. `index(item)`

Returns the index of the **first occurrence** of the item.

```python
fruits = ['apple', 'banana', 'cherry']
print(fruits.index('banana'))  # Output: 1
```

---

### 10. `count(item)`

Counts how many times an item appears in the list.

```python
nums = [1, 2, 2, 3, 2]
print(nums.count(2))  # Output: 3
```

---

### 11. `extend()`

Adds **all elements** from another iterable (like another list).

```python
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)  # Output: [1, 2, 3, 4]
```

---



# List Slicing

## ✂️ **List Slicing Syntax**

```python
my_list[start : stop : step]
```

- `start` → index to begin (inclusive)
- `stop` → index to end (exclusive)
- `step` → how many indices to skip

---

## 🔹 **Basic Slicing Examples**

```python
my_list = [10, 20, 30, 40, 50, 60]
```

| Slice             | Result                 | Description                    |
|------------------|------------------------|--------------------------------|
| `my_list[1:4]`    | `[20, 30, 40]`         | From index 1 to 3              |
| `my_list[:3]`     | `[10, 20, 30]`         | From start to index 2          |
| `my_list[2:]`     | `[30, 40, 50, 60]`     | From index 2 to end            |
| `my_list[:]`      | `[10, 20, 30, 40, 50, 60]` | Copy the whole list       |

---

## 🔁 **Using Step**

| Slice              | Result                 | Description                         |
|-------------------|------------------------|-------------------------------------|
| `my_list[::2]`     | `[10, 30, 50]`         | Every 2nd item                      |
| `my_list[1::2]`    | `[20, 40, 60]`         | Every 2nd item starting from index 1|
| `my_list[::-1]`    | `[60, 50, 40, 30, 20, 10]` | Reverse list                    |
| `my_list[::-2]`    | `[60, 40, 20]`         | Reverse, skipping every other item  |

---

## ⚠️ **Out of Range Handling**

Python slicing won't throw an error for out-of-range indices:

```python
my_list[0:100]  # Works fine
my_list[10:]    # Returns []
```

---

## 📋 **Modifying with Slicing**

You can assign values using slicing too:

```python
my_list[1:3] = [200, 300]
# Now: [10, 200, 300, 40, 50, 60]
```

You can delete slices:

```python
del my_list[1:3]
# Now: [10, 40, 50, 60]
```

---

