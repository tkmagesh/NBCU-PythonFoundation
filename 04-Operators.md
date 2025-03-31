# Operators

### 1. **Arithmetic Operators** (Math stuff)  
```python
+   # Addition  
-   # Subtraction  
*   # Multiplication  
/   # Division  
%   # Modulus (remainder)  
**  # Exponent (power)  
//  # Floor division (no decimal)
```

---

### 2. **Assignment Operators** (Assigning values)  
```python
=     # Assign  
+=    # Add and assign → x += 1 (same as x = x + 1)  
-=    # Subtract and assign  
*=, /=, %=, **=, //=  # Same idea
```

---

### 3. **Comparison Operators** (Compare values, returns True/False)  
```python
==   # Equal  
!=   # Not equal  
>    # Greater than  
<    # Less than  
>=   # Greater than or equal  
<=   # Less than or equal
```

---

### 4. **Logical Operators** (Combine conditions)  
```python
and   # True if both are true  
or    # True if at least one is true  
not   # Reverses the result
```

---

### 5. **Identity Operators** (Compare memory location)  
```python
is      # True if both refer to the same object  
is not  # True if they don't
```

---

### 6. **Membership Operators** (Check if a value exists)  
```python
in       # True if value is in the sequence  
not in   # True if not
```

---

### 7. **Bitwise Operators** (Binary operations — advanced)  
```python
&    # AND  
|    # OR  
^    # XOR  
~    # NOT  
<<   # Left shift  
>>   # Right shift
```

## Operators Examples
---

### 1. **Arithmetic Operators**
```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a % b)   # 1
print(a ** b)  # 1000 (10³)
print(a // b)  # 3
```

---

### 2. **Assignment Operators**
```python
x = 5
x += 2   # x = x + 2 → x = 7
x *= 3   # x = 7 * 3 → x = 21
```

---

### 3. **Comparison Operators**
```python
a = 5
b = 7

print(a == b)   # False
print(a != b)   # True
print(a < b)    # True
print(a >= 5)   # True
```

---

### 4. **Logical Operators**
```python
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x > 15)    # False
print(not (x > 5))        # False
```

---

### 5. **Identity Operators**
```python
a = [1, 2]
b = a
c = [1, 2]

print(a is b)       # True (same object)
print(a is c)       # False (same content, different objects)
print(a is not c)   # True
```

---

### 6. **Membership Operators**
```python
colors = ["red", "blue"]
print("red" in colors)      # True
print("green" not in colors)  # True
```

---

### 7. **Bitwise Operators** 
```python
a = 5     # 0101 in binary  
b = 3     # 0011

print(a & b)  # 1 (0001)
print(a | b)  # 7 (0111)
print(a ^ b)  # 6 (0110)
print(~a)     # -6 (inverts bits)
print(a << 1) # 10 (shifts left)
print(a >> 1) # 2  (shifts right)
```

