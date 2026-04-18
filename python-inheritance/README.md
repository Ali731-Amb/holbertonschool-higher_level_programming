# Python - Inheritance

## Learning Objectives

At the end of this project, you should be able to explain:

- What a superclass, base class, or parent class is  
- What a subclass is  
- How to list all attributes and methods of a class or instance  
- When an instance can have new attributes  
- How to inherit a class from another  
- How to define a class with multiple base classes  
- What the default base class in Python is  
- How to override inherited methods or attributes  
- Which attributes/methods are inherited by subclasses  
- Why inheritance is used  
- How and when to use `isinstance`, `issubclass`, `type`, and `super`

## Requirements

### Python scripts
- Allowed editors: vi, vim, emacs  
- Ubuntu 20.04 LTS using Python 3.8.5  
- All files must end with a new line  
- First line: `#!/usr/bin/python3`  
- A README.md is mandatory at the root of the project  
- Code must follow pycodestyle (2.7.*)  
- All files must be executable  
- File length checked using wc  

### Test files
- All tests inside `tests/` folder  
- Must be `.txt` files  
- Run with: `python3 -m doctest ./tests/*`  
- All modules/classes/functions must be documented  
- Documentation must be real sentences explaining purpose  
- Avoid using words like import or from in comments  

## Tasks

0. Lookup  
Write a function that returns the list of attributes and methods of an object.

1. My list  
Create a class MyList that inherits from list:
- Method print_sorted() prints list in ascending order  
- Assume all elements are integers  

2. Exact same object  
Function is_same_class(obj, a_class):
- Returns True if object is exactly instance of class  

3. Same class or inherit from  
Function is_kind_of_class(obj, a_class):
- True if object is instance or inherited from class  

4. Only sub class of  
Function inherits_from(obj, a_class):
- True if object is instance of subclass (not same class)  

5. Geometry module  
Class BaseGeometry:
- Empty class  

6. Improve Geometry  
BaseGeometry:
- area() raises Exception: area() is not implemented  

7. Integer validator  
BaseGeometry:
- integer_validator(name, value):
  - value must be int  
  - value must be > 0  
  - otherwise raise correct exception  

8. Rectangle  
Inherits BaseGeometry:
- Private attributes width and height  
- Validated using integer_validator  
- No getters/setters  

9. Full rectangle  
- Implements area()  
- __str__ returns [Rectangle] <width>/<height>  

10. Square #1  
Inherits Rectangle:
- Private attribute size  
- Validated with integer_validator  
- Implements area()  

11. Square #2  
- __str__ returns [Square] <size>/<size>  

## Key idea

Inheritance is about structuring code to:
- reuse logic  
- avoid duplication  
- centralize validation  
- build hierarchy (BaseGeometry → Rectangle → Square)  
- enable polymorphism  
