# Tuple

## 🧾 **What is a Tuple?**

- A **tuple** is an **ordered**, **immutable** (unchangeable) collection.
- It can contain elements of **different data types**.
- Defined using **parentheses `()`** or without them (just commas).

---

## 🛠️ **Creating Tuples**

```python
empty = ()
one_item = (5,)          # Note the comma!
nums = (1, 2, 3)
mixed = (1, "hi", 3.14)
nested = (1, (2, 3), [4, 5])
```

---

## 🔍 **Accessing Elements**

```python
t = (10, 20, 30)

t[0]      # 10
t[-1]     # 30
t[1:3]    # (20, 30) – slicing works like lists
```

---

## ✅ **Tuple Characteristics**

| Feature        | Supported |
|----------------|-----------|
| Indexing       | ✅         |
| Slicing        | ✅         |
| Mutability     | ❌ (immutable) |
| Nested Items   | ✅         |
| Duplicate Items| ✅         |

---

## ♻️ **Common Tuple Functions**

| Function/Method   | Description                        | Example                          |
|------------------|------------------------------------|----------------------------------|
| `len(t)`          | Number of items                    | `len((1, 2, 3)) → 3`             |
| `min(t)`          | Smallest item (numbers/strings)    | `min((4, 2, 9)) → 2`             |
| `max(t)`          | Largest item                       | `max((4, 2, 9)) → 9`             |
| `sum(t)`          | Sum of elements (numbers only)     | `sum((1, 2, 3)) → 6`             |
| `t.index(x)`      | Index of first occurrence of x     | `(1, 2, 3).index(2) → 1`         |
| `t.count(x)`      | Count occurrences of x             | `(1, 1, 2).count(1) → 2`         |

---

## 🔁 **Looping through Tuples**

```python
t = ('a', 'b', 'c')
for item in t:
    print(item)
```

With `enumerate()`:
```python
for index, value in enumerate(t):
    print(index, value)
```

---

## 🧠 **Tuple Packing & Unpacking**

```python
# Packing
person = ("Alice", 25, "Engineer")

# Unpacking
name, age, job = person
print(name)  # Alice
```

Use `*` for variable-length unpacking:

```python
a, *b = (1, 2, 3, 4)
# a = 1, b = [2, 3, 4]
```

---

## 🆚 **Tuple vs List**

| Feature      | Tuple            | List           |
|--------------|------------------|----------------|
| Syntax       | `(1, 2, 3)`      | `[1, 2, 3]`     |
| Mutable?     | ❌ Immutable     | ✅ Mutable      |
| Performance  | Faster (read-only)| Slower         |
| Use Case     | Fixed data       | Dynamic data   |

---
