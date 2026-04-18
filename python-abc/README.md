# Python OOP & Advanced Object-Oriented Programming (Abstraction, Inheritance, Mixins)

This project is a deep exploration of Object-Oriented Programming (OOP) in Python, focusing on abstraction, inheritance, polymorphism, duck typing, iterators, multiple inheritance, and mixins. The goal is to understand how Python handles class hierarchies, behavior composition, and design principles used in real-world software architecture.

## Learning Objectives

By the end of this project, you should be able to clearly explain and apply the following concepts:

### General OOP Concepts
- What is a superclass, base class, or parent class
- What is a subclass
- How to list all attributes and methods of a class or instance
- When an instance can have new attributes dynamically
- How inheritance works in Python
- How multiple inheritance works
- What the default base class of all Python classes is (`object`)
- How to override inherited methods or attributes
- What is the purpose of inheritance in software design
- How Python resolves method calls in inheritance (MRO)

### Introspection & Built-ins
- `isinstance`, `issubclass`, `type`, `super`
- How to use `getattr`
- How Python finds attributes in an object or class
- What is `__dict__` for classes and instances

### OOP Design Principles
- What is abstraction
- What is encapsulation and information hiding
- What is polymorphism
- What is duck typing
- What is a mixin and when to use it

### Advanced OOP Features
- Abstract Base Classes (ABC)
- Interfaces in Python (via ABC)
- Method overriding
- Multiple inheritance
- Mixins and behavior composition
- Iterators and custom iteration logic

## Requirements

### Python Environment
- Ubuntu 20.04 LTS
- Python 3.8.5
- Allowed editors: vi, vim, emacs
- Files must end with a new line
- First line of all files must be:
  #!/usr/bin/python3
- Code must follow `pycodestyle (2.7.*)`
- All files must be executable
- File length checked with `wc`
- No external imports unless explicitly allowed

## Project Structure

All implementations are grouped in the following directory:

python-abc/

Each task introduces a concept progressively.

## Tasks Overview

### 0. Abstract Animal Class and Subclasses
- Create an abstract class `Animal`
- Define abstract method `sound()`
- Implement:
  - `Dog.sound()` → "Bark"
  - `Cat.sound()` → "Meow"

Concepts:
- Abstract classes
- Enforcing method implementation

---

### 1. Shapes, Interfaces, and Duck Typing
- Create abstract class `Shape`
- Define:
  - `area()`
  - `perimeter()`
- Implement:
  - `Circle`
  - `Rectangle`
- Function `shape_info()` uses duck typing (no type checks)

Concepts:
- Interfaces
- Duck typing
- Polymorphism

---

### 2. VerboseList (Subclassing Built-in Types)
- Inherit from Python `list`
- Override:
  - `append`
  - `extend`
  - `remove`
  - `pop`
- Print messages on modifications

Concepts:
- Inheriting built-in classes
- Method overriding
- Using `super()`

---

### 3. CountedIterator
- Wrap a Python iterator
- Count number of `__next__` calls
- Provide `get_count()`

Concepts:
- Iterators
- `__iter__`, `__next__`
- StopIteration handling

---

### 4. FlyingFish (Multiple Inheritance)
- Class `Fish`
- Class `Bird`
- Class `FlyingFish` inherits both
- Override shared behaviors

Concepts:
- Multiple inheritance
- Method Resolution Order (MRO)

---

### 5. Dragon (Mixins)
- `SwimMixin`
- `FlyMixin`
- `Dragon` combines both behaviors

Concepts:
- Mixins
- Behavior composition
- Modular design

---

## Key Concepts Summary

### Abstraction
Hide implementation details and expose only essential behavior.

### Duck Typing
"If it behaves like the expected object, it is valid."

### Inheritance
Reuse and extend existing behavior.

### Multiple Inheritance
Combine behaviors from multiple parents.

### Mixins
Small reusable behavior components.

### Iterators
Objects that implement:
- `__iter__`
- `__next__`

### MRO (Method Resolution Order)
Defines how Python resolves method calls in multiple inheritance.

## Important Notes

- Do not rely on type checking in functional design (prefer duck typing)
- Always respect encapsulation (use private attributes when required)
- Use `super()` properly in inheritance chains
- Understand behavior before implementation, not the opposite

## Final Goal

You should be able to design Python systems where:
- Classes are reusable
- Behaviors are composable
- Code is flexible and extensible
- Inheritance is used intentionally, not accidentally
