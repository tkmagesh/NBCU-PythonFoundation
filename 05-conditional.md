# Conditional Statements
---

## ✅ 1. **`if` Statement**

Runs a block of code **only if** a condition is `True`.

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

---

## 🔁 2. **`if-else` Statement**

Runs one block if condition is `True`, another if `False`.

```python
age = 18

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
```

---

## 🔀 3. **`if-elif-else` Chain**

Use **`elif`** (else-if) to check multiple conditions.

```python
score = 75

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D or Fail")
```

Python checks top to bottom. It **runs the first match** and **skips the rest**.

---

## 🔄 4. **Nested `if`**

You can put one `if` inside another.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Too young")
```

---

## 🤏 Short-hand (One-liners)

**Single-line `if`:**
```python
x = 10
if x > 5: print("Big number")
```

**Ternary operator (short if-else):**
```python
age = 17
result = "Adult" if age >= 18 else "Minor"
print(result)
```

---

## 🔗 Logical Operators with Conditions

Use `and`, `or`, `not` to combine conditions:

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Welcome!")
```

---

## ⚠️ Important Notes:

- Always use **indentation** (usually 4 spaces) under `if`, `else`, etc.
- Conditions must result in `True` or `False`.
- Strings, numbers, lists, etc., can also be tested directly:
  ```python
  name = "Alice"
  if name:  # True if not empty
      print("Name is provided")
  ```

- The following values are considered `False`
    - `0`
    - `0.0`
    - `""` OR `''` (empty string)
    - `[]` (empty list)
    - `{}` (empty dictionary)
    - `()` (empty tuple)

- Hint: Use "bool()" to get the boolean equivalent of a value
---

