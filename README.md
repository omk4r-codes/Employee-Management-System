# Employee Management System

This Employee Management System is a web-based application developed using Python Flask, HTML, Bootstrap, and MySQL via phpMyAdmin in Object-Oriented Programming. The system allows for the management of employees, including adding new employees, removing them by their employee IDs, assigning salaries, promoting employees to managers, and displaying a list of employees and managers within the website.

## Features

- **Add Employee:** Users can add new employees to the system by providing necessary details such as name, ID, department, etc.
- **Remove Employee:** Employees can be removed from the system using their unique employee IDs.
- **Salary Assignment:** Ability to assign salaries to employees based on their positions or other criteria.
- **Promotion to Manager:** Option to promote an employee to a manager role within the system.
- **Display Employees and Managers:** Display a comprehensive list of employees and managers on the website for easy reference.


## Prerequisites

- Python Flask: Used as the backend framework to handle server-side logic.
- HTML: Used for structuring the web pages and user interface.
- Bootstrap: Utilized for designing a responsive and visually appealing frontend.
- phpMyAdmin & MySQL: Database management system to store and retrieve employee-related information.


## Installation & Set-up

The web-based application requires python v8+ to run properly. To download python, head over to the [python official website](https://www.python.org/).
Then, install flask module as:
```sh
pip install flask
```

Install SQLAlchemy module:
```
pip install SQLAlchemy
```
*for python v3.11, SQLAlchemy doesn't work sometimes. Please try downgrading or upgradinng your python in that case!

Download XAMPP from its [official website](https://www.apachefriends.org/download.html) and set up. Open XAMPP Control Panel and start Apache & MySQL Modules.

Then go to your browser, type "localhost" and hit enter to open the XAMPP Dashboard.
Go to phpMyAdmin and create a new database named 'employee_management_system'.
Create different tables as given in the code.

Now you are good to go. Just run the code in `main.py` and click on the link in the terminal!

###### Feel free to customize and expand upon this code to match your requirements!

