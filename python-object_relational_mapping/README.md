# 🐍 Python ORM & MySQL Project (SQLAlchemy + MySQLdb)

## 🎯 Learning Objectives

At the end of this project, you will be able to explain:

- 🔌 How to connect to a MySQL database from a Python script  
- 📥 How to SELECT rows from a MySQL table using Python  
- 📤 How to INSERT rows into a MySQL table using Python  
- 🧠 What ORM (Object Relational Mapping) means  
- 🏗️ How to map a Python class to a MySQL table  

---

## ⚙️ Requirements

- 🧑‍💻 Allowed editors: `vi`, `vim`, `emacs`  
- 🐧 Ubuntu 20.04 LTS using Python 3.8.5  
- 🐬 MySQLdb version 2.0.x  
- 🧩 SQLAlchemy version 1.4.x  
- 📄 All files must end with a new line  
- 🐍 First line of all files: `#!/usr/bin/python3`  
- 📌 README.md is mandatory  
- 🎨 Code must follow `pycodestyle (2.7.*)`  
- 🔒 All files must be executable  
- 📏 File length checked using `wc`  
- 📚 Mandatory documentation for modules, classes, and functions  
- 🚫 No use of `execute()` in SQLAlchemy ORM tasks  

---

## 🛠️ Environment Setup

### 🐬 MySQL 8.0 Installation
- Install MySQL server on Ubuntu 20.04  
- Verify version using `mysql --version`  
- Access server with `sudo mysql`  

### 🧪 MySQLdb installation
- Install system dependencies (`python3-dev`, `libmysqlclient-dev`, `zlib1g-dev`)  
- Install driver: `mysqlclient==2.0.3`  
- Verify import works in Python  

### 🧩 SQLAlchemy installation
- Install version `1.4.22`  
- Verify import and version in Python  

---

## 🧠 Core Concepts

### 🔗 MySQL + Python
- Connect using MySQLdb or SQLAlchemy engine  
- Execute SQL queries from Python scripts  
- Handle results as tuples or ORM objects  

### ⚠️ SQL Injection
- Dangerous when user input is directly inserted into queries  
- Must be avoided using parameterized queries or ORM filtering  

### 🏗️ ORM (Object Relational Mapping)
- Maps Python classes → database tables  
- Allows working with objects instead of raw SQL  
- Example: `State` class ↔ `states` table  

---

## 📚 Tasks Overview

---

### 📊 0. Get all states
- Connect to database `hbtn_0e_0_usa`  
- List all states ordered by `id`  

---

### 🔎 1. Filter states (N*)
- Display states starting with **N**  
- Order by `id`  

---

### 🧾 2. Filter by user input
- Search states by exact name  
- Input passed as argument  
- Uses string formatting (unsafe version)  

---

### 🛡️ 3. SQL Injection protection
- Same as previous task  
- But now **safe against SQL injection**  
- Uses parameterized queries  

---

### 🏙️ 4. Cities by states
- Join cities and states  
- Display cities with their state  
- Only one execute call allowed  

---

### 🏙️ 5. Filter cities by state
- Input state name  
- Return all cities in that state  
- SQL injection safe  

---

## 🧱 SQLAlchemy ORM Tasks

---

### 🧬 6. First state model
- Create `State` class  
- Link to `states` table  
- Define:
  - `id` (PK, auto-increment)
  - `name` (VARCHAR 128, NOT NULL)

---

### 📋 7. All states (ORM)
- Query all `State` objects  
- Order by `id`  

---

### ⬆️ 8. First state
- Fetch only first state  
- If empty → print `Nothing`  

---

### 🔍 9. Contains letter "a"
- Filter states containing `"a"`  
- Case-sensitive search  

---

### 🎯 10. Get a state by name
- Return state by exact name  
- If not found → `Not found`  

---

### ➕ 11. Add a state
- Insert `"Louisiana"` into database  
- Print new `id`  

---

### ✏️ 12. Update a state
- Update state where `id = 2`  
- New name: `"New Mexico"`  

---

### ❌ 13. Delete states
- Remove states containing letter `"a"`  

---

### 🏙️ 14. Cities in state
- Create `City` model  
- Link with `State` via foreign key  
- Display:
  - `State: (City ID) City Name`  

---

## 🧠 Key Takeaways

- 🔌 Database connection handling in Python  
- 🧾 Difference between raw SQL vs ORM  
- 🛡️ SQL injection prevention techniques  
- 🏗️ Object-relational mapping design  
- 🔗 Relationships (One-to-Many via foreign keys)  
- ⚡ Efficient querying strategies  

---

## 🚀 Final Goal

By completing this project, you should be able to:

- Replace raw SQL with Python ORM  
- Securely interact with databases  
- Design relational models in Python  
- Build scalable database-driven applications  
