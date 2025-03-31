# Loops in Python
---

## 🔁 1. **`for` loop**

Used to **loop over a sequence** like a list, string, or `range()`.

```python
for i in range(5):
    print(i)
```

🔹 Loops from 0 to 4 (5 is not included).

```python
for no in range(2,10):
    print(no)
```
🔹 Loops from 2 to 10 (10 is not included).

```python
for no in range(2,10,2):
    print(no)
```
🔹 Loops from 2 to 10 (incremented by 2 and 10 is not included).

---

### 🧵 Loop over string

```python
for letter in "hello":
    print(letter)
```

---

### 📋 Loop over list

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

---

## 🔄 2. **`while` loop**

Repeats **while a condition is True**.

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

Be careful with `while` loops — they can run forever if the condition never becomes `False`.

---

## 🛑 Loop Control Statements

- `break` → Stop the loop early  
- `continue` → Skip the rest of the loop and go to the next round  
- `pass` → Do nothing (placeholder)

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

## ✨ Optional: `else` with loops

Python allows `else` **after a loop**, runs only if the loop **was not broken**.

```python
for i in range(3):
    print(i)
else:
    print("Loop completed")
```

---

