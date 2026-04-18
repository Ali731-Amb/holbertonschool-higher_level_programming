# RESTful API Project

## Introduction
In the evolving world of software development, understanding how to communicate and transfer data efficiently between systems is essential. This project delves into the domain of RESTful APIs, a cornerstone in the realm of web services. The Representational State Transfer (REST) architecture is a set of constraints that ensure a scalable, stateless, and cacheable communication system. This approach allows for the easy integration of web services, making them accessible to a wide range of applications.

## Learning Objectives:
HTTP/HTTPS Basics: Grasp the foundational principles of the web's primary protocol, understanding how data transfer occurs, methods involved, and the difference between the secure and non-secure versions.

API Consumption with Command Line: Hands-on experience in interacting with APIs using basic command-line tools, laying the groundwork for more advanced interactions.

API Consumption with Python: Elevate your data fetching skills by leveraging Python's capabilities, allowing for more advanced processing and data manipulation.

API Development with http.server: Understand the basics of crafting an API from scratch using Python's built-in modules, setting a solid foundation.

API Development with Flask: Dive deeper into API development using the lightweight Flask framework, focusing on routing, data management, and scalability.

API Security & Authentication: Address the crucial aspect of security, understanding how to protect data transfer and ensure only authorized access to resources.

API Standards & Documentation with OpenAPI: Conclude with the importance of maintaining standardized documentation, ensuring that APIs are usable, understandable, and maintainable.

## Importance:
In our interconnected digital age, RESTful APIs play a pivotal role in the integration of different systems. They serve as the middlemen, translating requests into understandable actions, fetching data, or triggering procedures. From social media platforms sharing data with advertisement agencies to complex industrial systems communicating with each other for automation, APIs are ubiquitous.

Developing a solid understanding of how to consume, develop, secure, and document these APIs equips you with a critical skill set. It's a blend of understanding both the technical intricacies and the larger design picture, ensuring seamless and efficient communication in the digital world.

## REST API Conceptual Diagram:
+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database

## Components:
Client: The requester of the service, often a web browser or application.
Web Server: Handles the incoming request, acts as a middleman before passing it to the API server.
API Server: The actual logic layer that processes the request, determining what data or action is required.
Database: Stores the data which the API might fetch or modify.

## Flow:
The client sends an HTTP/HTTPS request to the Web Server.
The Web Server, after potential routing and load balancing, forwards the request to the API Server.
The API Server processes the request, interacts with the database if needed.
The API Server returns the processed response to the Web Server.
The Web Server sends back the final HTTP/HTTPS response to the client.

This diagram provides a high-level view of how RESTful API communication typically works. In simpler setups, the Web Server and API Server might be combined into one. The separation here illustrates potential layers in a more complex or scaled environment.

## Requirements
IMPORTANT: Your scripts will be tested with Python 3.9.

## Tasks

### 0. Basics of HTTP/HTTPS
#### Background:
The Hypertext Transfer Protocol (HTTP) is the foundation of data communication on the web. It allows web clients (like browsers) to communicate with web servers. HTTP has evolved over time and has a secure counterpart called HTTPS (HTTP Secure). HTTPS is just like HTTP but with an added layer of security using SSL/TLS encryption. This layer protects the data from eavesdroppers and tampering.

#### Objective:
At the end of this exercise, students should be able to:
Differentiate between HTTP and HTTPS.
Understand the basic working and structure of HTTP requests and responses.
Recognize and explain the common HTTP methods and status codes.

#### Resources:
Mozilla Developer Network (MDN) - An Overview of HTTP
Difference between HTTP and HTTPS
List of HTTP status codes

#### Instructions:
Differentiating HTTP and HTTPS:
Read the provided resources to understand the basic differences between HTTP and HTTPS.
Jot down the main differences, focusing on security aspects.
Optional: Use a packet sniffer tool like Wireshark to observe the traffic of an HTTP and an HTTPS request (Make sure you have the appropriate permissions).

Understanding HTTP Structure:
Visit a simple website, right-click, and choose "Inspect" or "Inspect Element". Navigate to the "Network" tab. This shows all network requests made by the page.
Reload the page and observe the first request. Click on it. Explore the "Headers" section to understand the structure of HTTP requests and responses. You'll see methods, paths, status codes, headers, and more.

Exploring HTTP Methods and Status Codes:
Based on the resources provided, make a list of at least four common HTTP methods and explain when each would be used.
Make another list of five common HTTP status codes. For each status code, provide a brief description and a scenario where it might be encountered.

#### Hints:
HTTP does not encrypt its data, which means that anyone eavesdropping on the communication can see the content. HTTPS adds a layer of encryption, making the content unintelligible to eavesdroppers.
The "s" in "https" stands for "secure".
Each HTTP status code has a specific purpose. They are grouped by their first digit.

#### Expected Output:
A brief summary explaining the differences between HTTP and HTTPS.
A depiction of HTTP request/response structure.
Lists of HTTP methods and status codes with use cases.

---

### 1. Consume data from an API using curl

#### Background:
curl is a command-line tool used to transfer data using HTTP, HTTPS, and more.

#### Objective:
- Install and use curl
- Construct API requests
- Interpret responses

#### Instructions:
Install curl and run:
curl --version

Fetch a webpage:
curl http://example.com

Fetch API data:
curl https://jsonplaceholder.typicode.com/posts

Fetch headers:
curl -I https://jsonplaceholder.typicode.com/posts

POST request:
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts

---

### 2. Consuming and processing data from an API using Python

#### Background:
Python uses the requests library for HTTP communication.

#### Objective:
- Send requests
- Parse JSON
- Convert to CSV

#### Instructions:
Install requests:
pip install requests

Fetch posts using requests.get()
Print status code
Parse JSON with .json()
Print titles
Save posts to CSV file

---

### 3. Develop a simple API using Python with http.server

#### Background:
http.server provides basic HTTP server functionality.

#### Objective:
- Build server
- Handle GET requests
- Return JSON

#### Instructions:
- Create server on port 8000
- Handle routes:
  / → message
  /data → JSON
  /status → OK
  other → 404

---

### 4. Develop a Simple API using Python with Flask

#### Background:
Flask is a lightweight web framework.

#### Objective:
- Create API
- Handle routes
- Process data

#### Instructions:
- Install Flask
- Create routes:
  / → welcome
  /data → list users
  /status → OK
  /users/<username> → user info
  /add_user → POST

Handle errors:
- 400 invalid JSON
- 404 user not found
- 409 duplicate

---

### 5. API Security and Authentication Techniques

#### Background:
API security prevents unauthorized access.

#### Objective:
- Implement authentication
- Use JWT
- Handle roles

#### Instructions:
- Basic Auth with Flask-HTTPAuth
- JWT with Flask-JWT-Extended
- Protected routes:
  /basic-protected
  /login
  /jwt-protected
  /admin-only

#### Expected Output:
401 Unauthorized for invalid access
403 Forbidden for wrong role
Successful access returns confirmation messages

#### Important Note:
Always return 401 for authentication errors.
