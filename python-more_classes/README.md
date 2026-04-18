# Python - More Classes

## Learning Objectives

At the end of this project, you should be able to explain:

- Why Python programming is considered powerful and flexible  
- What Object-Oriented Programming (OOP) is  
- The concept of “first-class everything” in Python  
- What a class is  
- What an object and an instance are  
- The difference between a class and an object/instance  
- What an attribute is  
- How public, protected, and private attributes work and how to use them  
- What `self` represents in a class  
- What a method is  
- The purpose of the special method `__init__`  
- Data Abstraction, Data Encapsulation, and Information Hiding  
- What a property is  
- The difference between attributes and properties  
- The Pythonic way of implementing getters and setters  
- The special methods `__str__` and `__repr__` and their usage  
- The difference between `__str__` and `__repr__`  
- What a class attribute is  
- The difference between instance attributes and class attributes  
- What a class method is  
- What a static method is  
- How to dynamically create attributes for instances  
- How attributes are bound to objects and classes  
- What `__dict__` contains for classes and instances  
- How Python resolves attributes on objects and classes  
- How to use the `getattr` function  

---

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`  
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5  
- All files must end with a new line  
- First line of all files: `#!/usr/bin/python3`  
- Mandatory `README.md` at the root of the project  
- Code must follow `pycodestyle` (version 2.7.*)  
- All files must be executable  
- File length will be checked using `wc`  
- Every module must have documentation  
- Every class must have documentation  
- Every function (inside and outside classes) must have documentation  
- Documentation must be real sentences explaining purpose (not just words)  

---

## Tasks

### 0. Simple rectangle
Create an empty class `Rectangle`.

---

### 1. Real definition of a rectangle
Create a class `Rectangle` with:

- Private attribute `width`
- Private attribute `height`
- Properties and setters for both attributes
- Initialization with optional width and height
- Validation:
  - Must be integers
  - Must be >= 0

---

### 2. Area and perimeter
Extend `Rectangle`:

- Add method `area()` returning width × height  
- Add method `perimeter()` returning 2 × (width + height)  
- If width or height is 0 → perimeter is 0  

---

### 3. String representation
Extend `Rectangle`:

- `__str__` and `print()` display rectangle using `#`
- `__repr__` returns a string that recreates the object
- If width or height is 0 → return empty string  

---

### 4. Eval is magic
Extend `Rectangle`:

- `__repr__` must allow `eval()` to recreate object exactly  

---

### 5. Detect instance deletion
Extend `Rectangle`:

- Print `"Bye rectangle..."` when an instance is deleted  

---

### 6. How many instances
Extend `Rectangle`:

- Add class attribute `number_of_instances`
- Increment on creation
- Decrement on deletion  

---

### 7. Change representation
Extend `Rectangle`:

- Add class attribute `print_symbol`
- Used for string representation instead of `#`
- Can be any type  

---

### 8. Compare rectangles
Extend `Rectangle`:

- Add static method `bigger_or_equal(rect_1, rect_2)`
- Compare rectangles by area  
- Return `rect_1` if equal  

---

### 9. A square is a rectangle
Extend `Rectangle`:

- Add class method `square(size=0)`
- Returns a square (width == height == size)  

---

## Notes

- No external imports allowed  
- Focus on OOP principles and encapsulation  
- Practice properties, class methods, and static methods  
- Understand object lifecycle (`__init__`, `__del__`)  
