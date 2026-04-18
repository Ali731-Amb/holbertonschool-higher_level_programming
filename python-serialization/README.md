# Python - Serialization

## Introduction

Welcome to our exploration of marshaling and serialization, two fundamental concepts in computer science that enable the efficient storage and transmission of data. In this programming project, you will delve deep into how data can be transformed and communicated between different parts of a system, or even across different systems. This project is designed to enhance your understanding and practical skills in handling data in real-world applications.

## What is Marshaling?

Marshaling is the process of transforming memory objects into a format that can be stored or transmitted over a network. It involves packaging complex objects and their attributes into a simpler, often binary, format. This is crucial in scenarios such as remote procedure calls, where objects need to be represented in a standard format across different computing platforms.

## What is Serialization?

Serialization, closely related to marshaling, specifically involves converting data structures or object states into a format that can be easily saved to a file or sent over a network. The main goal of serialization is to preserve the state of an object, so it can be recreated in an identical state elsewhere. This becomes essential in developing applications that require data persistence, distributed computing, and data sharing between different software components.

## Learning Objectives

- Articulate the differences and similarities between marshaling and serialization.
- Implement serialization in a practical programming task.
- Understand how serialized data can be used in web applications, databases, and network communications.
- Evaluate the performance implications of different serialization formats, like JSON, XML, and binary formats.

## Resources

- Real Python Serialization
- Real Python: Working With JSON Data in Python
- Python's pickle documentation
- Corey Schafer on Pickle
- CSV to JSON in Python
- Python XML ElementTree Guide
- Socket Programming Guide

## Tasks

### 0. Basic Serialization

Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

Write a Python module named `task_00_basic_serialization.py` with the following functions:

- `serialize_and_save_to_file(data, filename)`
- `load_and_deserialize(filename)`

The function `serialize_and_save_to_file` takes:
- data: A Python Dictionary with data
- filename: The filename of the output JSON file. If the output file already exists it should be replaced.

The function `load_and_deserialize` takes:
- filename: The filename of the input JSON file

This function returns a Python Dictionary with the deserialized JSON data from the file.

### 1. Pickling Custom Classes

Learn how to serialize and deserialize custom Python objects using the pickle module.

Create a class named `CustomObject` with:
- name (a string)
- age (an integer)
- is_student (a boolean)

Add a method `display` that prints:

Name: John  
Age: 25  
Is Student: True  

Implement:
- `serialize(self, filename)`
- `deserialize(cls, filename)` (as a class method)

Handle errors properly. If a file is missing or invalid, return None.

### 2. Converting CSV Data to JSON Format

The objective is to read data from CSV and convert it into JSON.

Import:
- csv
- json

Create a function `convert_csv_to_json(csv_filename)` that:

- Reads the CSV using `DictReader`
- Converts rows into dictionaries
- Serializes them into JSON
- Writes into `data.json`

Return:
- True if successful
- False if an error occurs

Example CSV:

name,age,city  
John,28,New York  
Alice,24,Los Angeles  
Bob,22,Chicago  
Eve,30,San Francisco  

Expected JSON:

[
    {"name": "John", "age": "28", "city": "New York"},
    {"name": "Alice", "age": "24", "city": "Los Angeles"},
    {"name": "Bob", "age": "22", "city": "Chicago"},
    {"name": "Eve", "age": "30", "city": "San Francisco"}
]

### 3. Serializing and Deserializing with XML

Use `xml.etree.ElementTree` module.

Create two functions:

- `serialize_to_xml(dictionary, filename)`
- `deserialize_from_xml(filename)`

Serialization:
- Create root `<data>`
- Add dictionary keys as child elements
- Save XML file

Deserialization:
- Parse XML file
- Rebuild dictionary
- Return dictionary

Example XML:

<data>
    <name>John</name>
    <age>28</age>
    <city>New York</city>
</data>

Example Output:

Dictionary serialized to data.xml

Deserialized Data:
{'name': 'John', 'age': '28', 'city': 'New York'}

## Important Notes

- XML does not preserve data types (everything becomes string)
- Always handle exceptions (file not found, invalid data)
- Pickle should not be used with untrusted data

## Key Takeaways

- Serialization is essential for saving and transmitting data
- JSON is lightweight and widely used
- XML is more verbose but structured
- Pickle is Python-specific and useful for objects

## Reflection Questions

- What is the difference between marshaling and serialization?
- Why is JSON more popular than XML?
- When would you use pickle instead of JSON?
- Why does XML not preserve data types?
- What happens if you deserialize a corrupted file?
