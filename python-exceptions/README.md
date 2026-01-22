![Python Exceptions Banner](assets/banner.png)

# Python - Exceptions

## Description
This project is an introduction to **exception handling in Python**.
It focuses on understanding the difference between errors and exceptions, learning how to handle runtime errors properly using `try`, `except`, `else`, and `finally`, and knowing when and how to raise exceptions intentionally.

Exception handling is a key concept in Python that allows programs to **fail gracefully**, avoid crashes, and manage unexpected situations such as invalid user input, division by zero, or accessing elements out of range.

---

## Learning Objectives

During this project, I learned why Python is so enjoyable to work with: its syntax is clear, readable, and it knows how to handle problems without panicking.
I understood the difference between errors and exceptions, and why exceptions exist to prevent a program from crashing at the first unexpected issue.

I learned how to use exceptions properly, when to catch them, when to raise them, and how to handle them cleanly using `try` and `except`.
I also understood why catching exceptions is important: to keep the program under control, display useful error messages, and avoid dramatic exits.

Finally, I learned the importance of cleaning up after an exception (because leaving a mess is never a good idea), such as closing files or freeing resources, to keep the program stable and well-behaved.

---

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- OS: Ubuntu 20.04 LTS
- Python version: `python3` (3.8.5)
- All files must end with a new line
- The first line of all files must be exactly: `#!/usr/bin/python3`
- A README.md file at the root of the project is mandatory
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable
- File length will be tested using wc
- No module imports allowed unless explicitly stated
- Use of try / except is mandatory where required
- Use of len() and type() is forbidden where specified

---

## Tasks

### 0. Safe list printing
**File:** `0-safe_print_list.py`

- Prints `x` elements of a list
- Uses `try / except`
- Does not use `len()`
- Returns the real number of elements printed
- Handles cases where `x` is greater than the list size

---

### 1. Safe printing of an integers list
**File:** `1-safe_print_integer.py`

- Prints an integer using `"{:d}".format()`
- Returns `True` if the value is an integer, otherwise `False`
- Uses `try / except`
- Does not use `type()`

---

### 2. Print and count integers
**File:** `2-safe_print_list_integers.py`

- Prints the first `x` elements of a list
- Only integers are printed; other types are silently ignored
- Uses `try / except`
- Does not use `len()`
- Returns the number of integers printed
- Raises an exception if the list is too short

---

### 3. Integers division with debug
**File:** `3-safe_print_division.py`

- Divides two integers
- Uses `try / except / finally`
- Prints the result in the `finally` block
- Returns the division result or `None` if an error occurs

---

### 4. Divide a list
**File:** `4-list_division.py`

- Divides elements of two lists index by index
- Returns a new list of size `list_length`
- Handles the following cases:
  - Wrong type → prints `wrong type`
  - Division by zero → prints `division by 0`
  - Index out of range → prints `out of range`
- Uses `try / except / finally`
- If a division fails, the result is `0`

---

### 5. Raise exception
**File:** `5-raise_exception.py`

- Raises a `TypeError`
- No module imports allowed

---

### 6. Raise a message
**File:** `6-raise_exception_msg.py`

- Raises a `NameError` with a custom message
- No module imports allowed

---

## Advanced Tasks – Python Exceptions

### 7. Safe integer print with error message

**File:** `100-safe_print_integer_err.py`
**Prototype:** `def safe_print_integer_err(value):`

This function safely prints an integer value.

- The value is printed followed by a new line **only if it is an integer**
- Uses `try / except` to handle errors
- Uses `"{:d}".format()` to format the integer
- Does **not** use `type()`
- If the value is **not** an integer:
  - Returns `False`
  - Prints the error message to **stderr**, preceded by `Exception:`
- Returns `True` if the integer is printed correctly

This task focuses on exception handling, output formatting, and stderr usage.

---

### 8. Safe function

**File:** `101-safe_function.py`
**Prototype:** `def safe_function(fct, *args):`

This function executes another function safely.

- `fct` is always a valid function reference
- Executes the function with its arguments
- Returns the function result if execution succeeds
- If an exception occurs:
  - Prints the error message to **stderr**, preceded by `Exception:`
  - Returns `None`
- Uses `try / except`

This task reinforces safe execution patterns and generic exception handling.

---

### 9. ByteCode → Python #4

**File:** `102-magic_calculation.py`
**Prototype:** `def magic_calculation(a, b):`

This function reproduces **exactly** the behavior of a given Python bytecode.

Key characteristics:
- Initializes a result variable
- Iterates over a range
- Uses a `try / except` block inside a loop
- Raises a custom exception when a condition is met
- Performs arithmetic operations involving:
  - Power
  - Division
  - In-place addition
- Handles exceptions by updating the result and breaking the loop
- Returns the final computed result

This task emphasizes understanding Python bytecode and translating low-level operations into valid Python logic.

---

## Author

**Alison AMBLARD**
Student at Holberton School
Track: Higher Level Programming
Project: Python - Exceptions


