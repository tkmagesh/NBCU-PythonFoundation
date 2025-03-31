# String
---

## 🧵 What is a `string`?

A `string` is a sequence of characters (letters, numbers, symbols) inside **quotes**.

```python
name = "Alice"
greeting = 'Hello'
```

You can use **single** or **double** quotes — both work the same.

---

## ✅ Key Things to Know About Strings

---

### 1. **Creating strings**
```python
s1 = "Hello"
s2 = 'World'
s3 = """Multiline
String"""
```

---

### 2. **Accessing characters (indexing)**
```python
text = "Python"
print(text[0])   # P
print(text[-1])  # n (last character)
```

---

### 3. **Slicing (get part of the string)**
```python
text = "Python"
print(text[1:4])  # yth
print(text[:3])   # Pyt
```

---

### 4. **Strings are immutable**  
You **can't change** characters in a string directly.

```python
text = "Hi"
# text[0] = "h"  ❌ Error
```

---

### 5. **Joining and Repeating**
```python
first = "Hello"
last = "World"
print(first + " " + last)  # Hello World

print("Ha" * 3)  # HaHaHa
```

---

### 6. **Using escape characters**
```python
print("He said \"Hi\"")   # He said "Hi"
print("Line1\nLine2")     # New line
```

---

### 7. **String formatting**
```python
name = "Sam"
age = 25

# f-string (most common)
print(f"My name is {name} and I am {age}")

# older styles:
print("My name is {} and I am {}".format(name, age))
```

---

## 🔧 Common String Functions/Methods

Assume:  
```python
text = "  hello World!  "
```

| Function             | What it does                        | Example                        |
|----------------------|-------------------------------------|--------------------------------|
| `lower()`            | lowercase letters                   | `text.lower()` → `'  hello world!  '` |
| `upper()`            | uppercase letters                   | `text.upper()` → `'  HELLO WORLD!  '` |
| `strip()`            | removes spaces                      | `text.strip()` → `'hello World!'` |
| `replace(old, new)`  | replaces part of string             | `text.replace("hello", "hi")` |
| `split()`            | splits into list of words           | `"a,b,c".split(",")` → `['a', 'b', 'c']` |
| `join()`             | joins list into string              | `" ".join(["a", "b"])` → `"a b"` |
| `find()`             | finds first index of substring      | `text.find("World")` → `8` |
| `count()`            | counts occurrences                  | `text.count("l")` → `3` |
| `startswith()`       | checks beginning                    | `text.startswith("  he")` → `True` |
| `endswith()`         | checks ending                       | `text.endswith("!")` → `False` |

