# 🗄️ SQL - More Queries Project

## 🎯 Learning Objectives

At the end of this project, you will be able to explain:

- 🔐 How to create a new MySQL user  
- 🛂 How to manage user privileges on a database or table  
- 🧩 What is a PRIMARY KEY  
- 🔗 What is a FOREIGN KEY  
- 🚫 How to use NOT NULL and UNIQUE constraints  
- 🔍 How to retrieve data from multiple tables in a single query  
- 🧠 What are subqueries  
- 🔗 What are JOIN and UNION  

---

## ⚙️ Requirements

- 🧑‍💻 Allowed editors: `vi`, `vim`, `emacs`  
- 🐧 Executed on Ubuntu 20.04 LTS using MySQL 8.0 (v8.0.25)  
- 📄 All files must end with a new line  
- 💬 SQL queries must include a comment above each query  
- 🧾 Each file must start with a descriptive comment of the task  
- 🔠 SQL keywords must be uppercase (SELECT, WHERE, etc.)  
- 📌 README.md is mandatory at the root of the project  
- 📏 File length will be checked using `wc`  

---

## 🛠️ MySQL Setup (Ubuntu 20.04)

Install MySQL:
- Update system packages  
- Install `mysql-server`  
- Check version to confirm installation  

Connect to MySQL:
- Use root access via `sudo mysql`  
- Exit with `quit`  

---

## 🧪 Using the Sandbox

- Default credentials: `root / root`  
- Start MySQL service before usage: `service mysql start`  
- Execute SQL scripts using pipe into MySQL client  

---

## 📦 Importing a SQL Dump

Typical flow:
- Create database  
- Download dump file  
- Import into MySQL database  
- Query tables to verify data  

---

## 📚 Project Tasks Overview

### 🔐 0. My privileges
Display privileges of specific users on localhost.

### 👤 1. Root user
Create user `user_0d_1` with full privileges.

### 👀 2. Read user
Create database + user `user_0d_2` with SELECT-only access.

### 🧱 3. Force name table
Create table with required NOT NULL constraints.

### 🚫 4. ID can't be null
Create table with default values and constraints.

### 🔑 5. Unique ID
Create table with UNIQUE constraint on id.

### 🏙️ 6. States table
Create database + table with primary key.

### 🌆 7. Cities table
Add foreign key referencing states table.

### 🌴 8. Cities of California
Use subquery to filter specific state cities.

### 🔗 9. Cities by States
Join tables to display combined information.

### 📺 10–16. TV Shows database queries
Work with:
- genres linked to shows  
- shows without genres  
- counting shows per genre  
- filtering by specific genre (Comedy, Drama, etc.)  
- listing all relationships between shows and genres  

---

## 🧠 Key Concepts Covered

- Database design & normalization  
- Data integrity constraints  
- Relational model (PK / FK)  
- Advanced querying (JOIN, subqueries, aggregation)  
- Permission management in SQL  

---

## 🚀 Goal of the Project

Build strong SQL fundamentals by mastering:
- database structure design  
- secure user management  
- complex data retrieval across multiple tables  
