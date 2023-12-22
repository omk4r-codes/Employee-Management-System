from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import MappedAsDataclass

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/employee_management_system'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/employee_management_system'

db = SQLAlchemy(app)


# class Employee(db.Model):

#     # id = db.Column(db.Integer, primary_key=True)
#     # username = db.Column(db.String(80), unique=True, nullable=False)
#     # email = db.Column(db.String(120), unique=True, nullable=False)

#     emp_id: db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
#     name: db.Column(db.String(80), unique=False, nullable=False)
#     emp_role: db.Column(db.String(50), unique=False, nullable=True)
#     dept_id: db.Column(db.Integer, unique=False, nullable=True)
#     email: db.Column(db.String(120), unique=True, nullable=False)
#     phone: db.Column(db.String(14), unique=True, nullable=False)
#     age: db.Column(db.Integer, unique=False, nullable=False)


class Employee(db.Model):
    emp_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    emp_role: Mapped[str] = mapped_column(String, nullable=True)
    dept_id: Mapped[int] = mapped_column(Integer, nullable=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer)


class Manager(db.Model):
    dept_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    manager_id: Mapped[int] = mapped_column(Integer, nullable=True)


class Department(db.Model):
    dept_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    dept_name: Mapped[str] = mapped_column(String, unique=True, nullable=False)


class Salary(db.Model):
    '''
    emp_id
    acc_no
    sal
    '''
    emp_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    acc_no: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    sal: Mapped[int] = mapped_column(Integer, nullable=False)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/add_emp", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        '''add entry to the database'''
        empid = request.form.get('empid')
        name = request.form.get('name')
        role = request.form.get('role')
        deptid = request.form.get('deptid')
        email = request.form.get('email')
        phNum = request.form.get('phNum')
        age = request.form.get('age')

        entry = Employee(emp_id=empid, name=name, emp_role=role, dept_id=deptid, email=email, phone=phNum, age=age)

        db.session.add(entry)
        db.session.commit()
    return render_template('add_emp.html')


@app.route("/delete", methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        empiddelete = request.form.get('empiddelete')
        employee = Employee.query.get(empiddelete)
        if employee:
            db.session.delete(employee)
            db.session.commit()

    return render_template('delete.html')


@app.route("/show")
def show():
    employees = Employee.query.all()
    return render_template('show.html', employees=employees)


@app.route("/manager", methods=['GET', 'POST'])
def manager():
    if request.method == 'POST':
        dept = request.form.get('dept')
        managerid = request.form.get('managerid')

        entry = Manager(dept_id=dept, manager_id=managerid)
        db.session.add(entry)
        db.session.commit()

    return render_template('manager.html')


@app.route("/show_managers")
def show_manager():
    managers = (db.session.query(Employee, Manager).join(
        Manager, Employee.dept_id == Manager.dept_id, isouter=True)).distinct(Employee.dept_id)

    manager_list = []
    for employee, manager in managers:
        if manager:
            manager_name = Employee.query.get(manager.manager_id).name
        else:
            manager_name = "null"

        department = Department.query.get(employee.dept_id)
        department_name = department.dept_name

        manager_dict = {"dept_name": department_name, "manager_name": manager_name}
        manager_list.append(manager_dict)

    return render_template('show_managers.html', manager_list=manager_list)


@app.route("/salary", methods=['GET', 'POST'])
def salary():
    if request.method == 'POST':
        empid = request.form.get('empid')
        accno = request.form.get('accno')
        sal = request.form.get('sal')
        entry = Salary(emp_id=empid, acc_no=accno, sal=sal)
        db.session.add(entry)
        db.session.commit()

    return render_template('salary.html')


app.run(debug=True)
