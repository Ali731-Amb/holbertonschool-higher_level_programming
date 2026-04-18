# Python - Classes and Objects

![Project Badge](https://img.shields.io/badge/Progress-100%25-brightgreen)

**Level:** Novice
**Project:** Holberton School - Higher Level Programming

---

## 📌 Description

This project introduces **Object-Oriented Programming (OOP)** in Python.

You will learn how to structure code using:

* Classes
* Objects
* Attributes and methods
* Encapsulation and abstraction

The goal is to move from procedural thinking to **modeling real-world concepts with code**.

---

## 🎯 Learning Objectives

At the end of this project, you should be able to explain:

### General

* What OOP is
* What “first-class everything” means in Python
* What a class is
* What an object (instance) is
* The difference between a class and an object
* What an attribute is
* Public, protected, and private attributes
* What `self` represents
* What a method is
* What `__init__` does
* Data abstraction, encapsulation, and information hiding
* What a property is
* Difference between attribute and property
* Pythonic getters and setters
* How to dynamically create attributes
* How attributes are bound to objects and classes
* What `__dict__` contains
* How Python searches for attributes
* How to use `getattr`

---

## ⚙️ Requirements

### General

* Allowed editors: `vi`, `vim`, `emacs`
* Python version: **3.8.5** (Ubuntu 20.04 LTS)
* All files must end with a new line
* First line must be:

  ```
  #!/usr/bin/python3
  ```
* A `README.md` file is mandatory
* Code must follow **pycodestyle (2.7.*)**
* All files must be executable
* File length will be checked (`wc`)

### Documentation

* Every module must have a docstring
* Every class must have a docstring
* Every function must have a docstring
* Docstrings must be **real sentences**, not keywords

---

## ℹ️ More Info

Documentation is mandatory and must follow a clear descriptive style (e.g., Google-style docstrings).

---

## 📁 Repository Structure

```id="z7t1qs"
holbertonschool-higher_level_programming/
└── python-classes/
    ├── 0-square.py
    ├── 1-square.py
    ├── 2-square.py
    ├── 3-square.py
    ├── 4-square.py
    ├── 5-square.py
    └── 6-square.py
```

---

## 🧩 Tasks

### 0. My first square

Create an empty class `Square`.

👉 Focus: minimal class definition.

---

### 1. Square with size

Add a **private attribute** `size`.

👉 Question: why protect it?

---

### 2. Size validation

Validate:

* Type → must be `int`
* Value → must be ≥ 0

Raise:

* `TypeError`
* `ValueError`

👉 Focus: input validation inside constructor.

---

### 3. Area of a square

Add method:

* `area()` → returns size²

👉 Think: behavior depends on state.

---

### 4. Access and update private attribute

Add:

* Getter (`@property`)
* Setter with validation

👉 Centralize validation logic.

---

### 5. Printing a square

Add method:

* `my_print()` → prints square using `#`

Special case:

* size = 0 → print empty line

👉 Nested loops reappear here.

---

### 6. Coordinates of a square

Add:

* Private attribute `position` (tuple of 2 positive ints)

Modify `my_print()`:

* Apply horizontal and vertical offset

👉 Think: rendering + positioning.

---

## 🧠 Key Concepts

Focus on understanding deeply:

* A class is a **blueprint**, an object is an **instance**
* `self` is the instance itself
* Private attributes (`__attr`) enforce control
* Properties allow controlled access without exposing internals
* Methods operate on instance state
* Python resolves attributes using a lookup chain (`__dict__`, class, inheritance)
* Encapsulation prevents invalid states
* Difference between:

  * storing data
  * controlling access to data

---

## 🚀 Execution Example

```id="h4x9wl"
./0-main.py
./1-main.py
```

---

## ❓ Questions to Guide Your Thinking

* Why hide `size` instead of making it public?
* What breaks if you don’t validate input?
* What is the difference between:

  * `self.size`
  * `self.__size`
* Why use `@property` instead of direct access?
* How does Python transform `__size` internally?
* What happens if you assign a new attribute dynamically?
* Where does Python look first when accessing an attribute?

---

## 🏁 Goal

The objective is to understand how to design clean, controlled, and extensible code using classes, while respecting encapsulation and Pythonic practices.
