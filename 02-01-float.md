# Float

### ✅ **What is a `float`?**

A `float` is a number with a **decimal point**.

```python
x = 3.14       # float
y = -0.5       # float
```

---

### 📌 **Key Points about `float`:**

1. **Created by using a decimal or `float()`**  
   ```python
   a = 5.0
   b = float(10)  # converts int to float → 10.0
   ```

2. **Supports arithmetic operations**  
   Works just like integers:
   ```python
   x = 2.5 + 1.5     # 4.0
   x = 4.2 * 3       # 12.6
   ```

3. **Division always returns float**
   ```python
   print(10 / 2)   # 5.0 (even though 5 is an int)
   ```

4. **Can be used in comparisons**
   ```python
   print(3.5 > 2.1)  # True
   ```

5. **Precision issues (⚠️)**  
   Due to how computers store decimals, some results are **not exact**:
   ```python
   print(0.1 + 0.2)  # 0.30000000000000004
   ```
   This is normal in most programming languages.

6. **Use `round()` to fix precision**
   ```python
   print(round(0.1 + 0.2, 2))  # 0.3
   ```

7. **Scientific notation**
   Floats can also be written in scientific (exponential) format:
   ```python
   x = 3e2   # 3 × 10² = 300.0
   y = 1.5e-3  # 1.5 × 10⁻³ = 0.0015
   ```

8. **Convert string to float**
   ```python
   num = float("3.14")  # 3.14
   ```

---

### 🔄 Common Conversions

- `int → float`  
  ```python
  float(5)  # 5.0
  ```

- `str → float`  
  ```python
  float("2.5")  # 2.5
  ```

- ⚠️ `float("hello")` → Error! (must be a number string)

