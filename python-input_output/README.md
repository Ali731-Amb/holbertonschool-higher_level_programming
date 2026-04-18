# Python Input/Output Project

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
Why Python programming is awesome  
How to open a file  
How to write text in a file  
How to read the full content of a file  
How to read a file line by line  
How to move the cursor in a file  
How to make sure a file is closed after using it  
What is and how to use the `with` statement  
What is JSON  
What is serialization  
What is deserialization  
How to convert a Python data structure to a JSON string  
How to convert a JSON string to a Python data structure  
How to access command line parameters in a Python script  

---

## Requirements

### Python Scripts
Allowed editors: vi, vim, emacs  
All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)  
All files should end with a new line  
First line of all files should be exactly `#!/usr/bin/python3`  
A README.md file, at the root of the folder of the project, is mandatory  
Your code should use the pycodestyle (version 2.7.*)  
All files must be executable  
File length will be tested using wc  

### Python Test Cases
Allowed editors: vi, vim, emacs  
All files should end with a new line  
All test files should be inside a folder tests  
All test files should be text files (extension: .txt)  
All tests should be executed using: `python3 -m doctest ./tests/*`  
All modules must have documentation  
All classes must have documentation  
All functions must have documentation  
A documentation is a full sentence explaining purpose  
Edge cases must be considered  

---

## Tasks

### 0. Read file
Write a function that reads a text file (UTF8) and prints it to stdout.

Prototype: `def read_file(filename=""):`  
Must use `with` statement  
No imports  
No exception handling required  

---

### 1. Write to a file
Write a function that writes a string to a text file (UTF8) and returns number of characters written.

Prototype: `def write_file(filename="", text=""):`  
Creates file if it does not exist  
Overwrites file if it exists  
Must use `with` statement  
No imports  

---

### 2. Append to a file
Write a function that appends a string at the end of a text file (UTF8) and returns number of characters added.

Prototype: `def append_write(filename="", text=""):`  
Creates file if it does not exist  
Must use `with` statement  
No imports  

---

### 3. To JSON string
Write a function that returns the JSON representation of an object (string).

Prototype: `def to_json_string(my_obj):`  
No exception handling required  

---

### 4. From JSON string to object
Write a function that returns an object represented by a JSON string.

Prototype: `def from_json_string(my_str):`  

---

### 5. Save Object to file
Write a function that writes an Object to a text file using JSON representation.

Prototype: `def save_to_json_file(my_obj, filename):`  
Must use `with` statement  
No exception handling required  

---

### 6. Create object from JSON file
Write a function that creates an Object from a JSON file.

Prototype: `def load_from_json_file(filename):`  
Must use `with` statement  

---

### 7. Load, add, save
Write a script that:
- adds all arguments to a Python list
- saves them to `add_item.json`
- uses `save_to_json_file`
- uses `load_from_json_file`

---

### 8. Class to JSON
Write a function that returns dictionary description of an object for JSON serialization.

Prototype: `def class_to_json(obj):`  
Only simple data structures (list, dict, str, int, bool)  

---

### 9. Student to JSON
Create class `Student` with:
- first_name
- last_name
- age

Method:
`def to_json(self):`  

---

### 10. Student to JSON with filter
Same class but:

`def to_json(self, attrs=None):`  
If attrs is a list of strings, only return those attributes  
Else return all attributes  

---

### 11. Student to disk and reload
Add method:

`def reload_from_json(self, json):`  
Replace all attributes using dictionary  

---

### 12. Pascal's Triangle
Write function:

`def pascal_triangle(n):`  
Returns list of lists representing Pascal triangle  
Return empty list if n <= 0  

---

## Repository

GitHub repository: holbertonschool-higher_level_programming  
Directory: python-input_output
