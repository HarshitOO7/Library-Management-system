# Library Management System

This is a Library Management System made using Python and MySQL with voice assistance.

## Features

  * Admin can add new books
  * Admin can delete books
  * Admin can check the borrowers
  * User can request a book
  * User can return a book
  * User can check the borrowers

## Requirements
    
      * Python 3.7
      * MySQL
        * pyttsx3
        * mysql.connector


## Installation
    
The project contains the following files:

1. library.py – This is the main python file that contains the code to manage the library. 

2. db.py – This file contains the code to connect to the database.

3. readme.md – This file contains the documentation of the project.

4. hbedi.sql – This file contains the SQL code to create the database and tables.

In order to run this project, you need to install python, MySQL and the necessary libraries. You also need to create a database and tables using the code in hbedi.sql file. After that, you need to configure the database in the db.py file. Finally, you can run the library.py file to start the application.

## Usage

After running the library.py file, you will see the following menu:

    Welcome To Our Library!
    _________________________________________________________________
    -----------------------------------------------------------------
    	 =========LIBRARY MENU=======
    1. Display all available books
    2. Request a book
    3. To check the borrowers
    4. Exit

You can choose any option from the menu. If you choose option 1, you will see the list of available books:
    
        Available Books:
        1. Python
        2. C++
        3. Java
        4. C
        5. C#
        6. JavaScript
        7. PHP
        8. HTML
        9. CSS
        10. SQL

If you choose option 2, you will be asked to enter the name of the book you want to request:
        
            Enter the name of the book you want to request: Python

If the book is available, you will see the following message:
            
                Book issued successfully. Please return the book within 30 days

If the book is not available, you will see the following message:
                
                    Sorry, the book is not available right now. Please try again later

If you choose option 3, you will see the list of borrowers:
                    
                        Borrowers:
                        1. GameOnSpotYt
                        2. hbedi

If you choose option 4, the application will terminate.


