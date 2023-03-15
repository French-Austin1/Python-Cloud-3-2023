
# Python Day 3

Today we focus on flask, SQLAlchemy and jinja2 in an effort to create a simple website.

## What is flask?

Flask is a popular Python web framework used for building web applications. It provides developers with the necessary tools and libraries to create web applications quickly and efficiently.  

At its core, Flask is a micro-framework, which means it has a small and flexible core that can be extended with various third-party libraries and plugins. Flask follows the Model-View-Controller (MVC) architecture pattern and is compatible with most common databases and web servers.  

Flask is used to create web applications by defining routes, which determine the URLs that the application responds to, and views, which handle the logic of the application. Flask also supports the use of templates, which are used to generate dynamic HTML pages.

## What is SQLAlchemy?

SQLAlchemy is a popular Python library used for working with databases. It provides a set of tools and abstractions that simplify the process of working with relational databases, including the ability to map Python classes to database tables and execute SQL queries in a Pythonic way.  

At its core, SQLAlchemy provides an Object Relational Mapper (ORM) that allows you to interact with databases using Python objects. The ORM provides a high-level interface for interacting with databases, allowing you to focus on the business logic of your application rather than the low-level details of working with SQL.  

SQLAlchemy supports a wide range of database systems, including MySQL, PostgreSQL, Oracle, SQLite, and Microsoft SQL Server. It also supports both raw SQL queries and an Object-Relational Query (OQR) language called SQLAlchemy Expression Language, which provides a Pythonic way to construct complex queries.

## What is jinja2?

Jinja2 is a popular templating engine for Python web frameworks, including Flask. It provides a powerful and flexible way to generate dynamic HTML pages by combining HTML templates with dynamic data from the application.  

Jinja2 templates are essentially text files that contain HTML markup with special syntax for injecting dynamic content. The syntax uses double curly braces `{{}}` to indicate that a placeholder should be replaced with a value at runtime. For example, if you wanted to display the value of a variable called name in your HTML template, you could use the following syntax:  

`<p>Hello, {{ name }}!</p>`

When you render this template, the `{{ name }}` placeholder will be replaced with the value of the `name` variable. 

## Test your knowledge!

Design and develop a simple Flask website with a database and an about page that allows users to create, read, update, and delete (CRUD) records. The website should have a homepage that displays a list of all records in the database and a form to add new records. Each record should contain at least a title and a description. The website should also have an about page that provides information about the website and its creators. The database should be configured using SQLAlchemy and should support multiple database systems, including SQLite, MySQL, and PostgreSQL. The website should be built using Flask's built-in templating engine, Jinja2, and should be styled using Bootstrap or another CSS framework. The website should be tested for functionality and usability. *(pytest, coverage, pylint)*