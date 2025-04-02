# Dictionary
---

## 🧾 **What is a Dictionary?**

- A **dictionary** is a **collection of key-value pairs**.
- It is **unordered** (before Python 3.7), **mutable**, and **indexed by keys** (not positions).
- Defined using **curly braces `{}`**.

---

## 🛠️ **Creating a Dictionary**

```python
# Basic dictionary
person = {"name": "Alice", "age": 30, "job": "Engineer"}

# Empty dictionary
empty = {}

# Using dict()
person2 = dict(name="Bob", age=25)
```

---

## 🔍 **Accessing Values**

```python
person["name"]       # 'Alice'
person.get("age")    # 30
person.get("salary", 0)  # Returns default 0 if not found
```

---

## 🧱 **Dictionary Structure**

```python
# Key-value pairs
{
    key1: value1,
    key2: value2,
}
```

- **Keys** must be **immutable** (strings, numbers, tuples).
- **Values** can be any type.

---

## ✏️ **Modifying a Dictionary**

```python
# Update value
person["age"] = 31

# Add new key-value
person["city"] = "New York"
```

---

## ❌ **Removing Items**

```python
person.pop("age")         # Removes 'age'
del person["job"]         # Removes 'job'
person.clear()            # Empties the dictionary
```

---

## ✅ **Useful Dictionary Methods**

| Method                | Description                             | Example                                 |
|-----------------------|-----------------------------------------|-----------------------------------------|
| `dict.keys()`         | Returns all keys                        | `person.keys()`                         |
| `dict.values()`       | Returns all values                      | `person.values()`                       |
| `dict.items()`        | Returns (key, value) pairs              | `person.items()`                        |
| `dict.get(k, default)`| Safe way to get a value                 | `person.get("age", 0)`                  |
| `dict.update(d2)`     | Merges another dict into it             | `person.update({"age": 35})`            |
| `dict.pop(k)`         | Removes and returns the value of key k | `person.pop("name")`                    |
| `dict.copy()`         | Creates a shallow copy                  | `new_dict = person.copy()`              |
| `dict.setdefault(k,v)`| Returns value if key exists, else sets | `d.setdefault("a", 100)`                |

---

## 🔁 **Looping through a Dictionary**

```python
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)
```

---

## 🔄 **Dictionary Comprehension**

```python
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---


## Check for the existence of a key

```python
my_dict = {'name': 'Alice', 'age': 25}
if 'name' in my_dict:
    print("Key exists")

# Output: Key exists
```
---


## 🧠 **Common Use Cases**

- Counting items:  
  ```python
  counts = {}
  for item in ['a', 'b', 'a']:
      counts[item] = counts.get(item, 0) + 1
  ```

- Nested dictionaries:
  ```python
  student = {
      "name": "John",
      "grades": {"math": 90, "science": 85}
  }
  ```

---

## 🆚 **Dictionary vs List**

| Feature      | Dictionary               | List                  |
|--------------|--------------------------|------------------------|
| Access by    | Key                      | Index                 |
| Ordered?     | ✅ (Python 3.7+)         | ✅                    |
| Mutable?     | ✅                        | ✅                    |
| Use Case     | Lookup by key            | Ordered sequence      |

---

