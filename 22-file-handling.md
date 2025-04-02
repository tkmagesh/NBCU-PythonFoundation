# File Handling

## 🔹 1. Opening a File

Python uses the built-in `open()` function:

```python
file = open('example.txt', 'r')  # Opens file for reading
```

**Modes:**
- `'r'` – read (default)
- `'w'` – write (creates a new file or overwrites existing)
- `'a'` – append
- `'r+'` – read and write

Always remember to close the file after working with it:

```python
file.close()
```

---

## 🔹 2. Reading from a File

### ➤ Read entire content
```python
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()
```

### ➤ Read line by line
```python
file = open('example.txt', 'r')
for line in file:
    print(line.strip())  # strip removes extra newlines
file.close()
```

---

## 🔹 3. Writing into a File

### ➤ Write (overwrites the file)
```python
file = open('example.txt', 'w')
file.write("Hello, World!\n")
file.write("This is a new line.\n")
file.close()
```

### ➤ Append (adds content at the end)
```python
file = open('example.txt', 'a')
file.write("Adding a line without removing old content.\n")
file.close()
```

---

## 🔹 4. Best Practice: `with` Statement

Using `with` automatically closes the file for you.

### ➤ Reading
```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### ➤ Writing
```python
with open('example.txt', 'w') as file:
    file.write("Clean and safe file handling!\n")
```

