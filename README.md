# Factorial Program

This Python program calculates the factorial of a given number using a loop-based approach.

## 📌 Description
The program initializes a number `n` and computes its factorial by multiplying all integers from 1 up to `n`.  
It then prints the result in a formatted string.

## 🔧 Changes Made
- Updated the value of `n` from **5** to **55** to calculate a larger factorial.

## 🖥️ Code Example
```python
n = 55
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial of {n} = {fact}")
