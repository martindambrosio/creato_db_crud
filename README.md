# Art School Database & CRUD Application

This repository contains a project for managing the database of "Creato", an art school, and its associated CRUD (Create, Read, Update, Delete) application built with Python and Tkinter. The project allows easy management of data related to employees, students, courses, grades, and more. It is structured in a way that makes it easy to manage, query, and edit information from the database.

# Project Structure

/creato-school-database
│
├── README.md                # This file
│── creato_schema.sql        # SQL file with table creation, INSERT statements, functions, stored procedures, views, and triggers.
│── /images_sql_results      # Folder with screenshots of the results of views.
│
├── /crud_python
│   ├── /controlador             # Folder containing logic for database operations and CRUD functionalities.
│   ├── /ddbb                    # Folder for the database-related files.
│   ├── /images_crud             # Folder with screenshots of the CRUD interface.
│   ├── /img                     # Folder with images used in the user interface.
│   ├── /vistas                  # Folder containing the views for the CRUD application.
│   ├── principal.py             # Main Python script that runs the CRUD application.
│   ├── README.md                # Crud readme.


# Features:

    SQL Database: Uses SQL for data management, with triggers and stored procedures to handle automated operations.
    Python CRUD Application: Built using Tkinter for a user-friendly interface for managing courses, students, and grades.
    Search & Filters: The CRUD application includes functionality for searching and filtering records, making it easy to manage data.

Set up the database:

    Open the creato_schema.sql file and run it to create the tables and insert the sample data.

Run the CRUD application:

    python creato_crud.py

