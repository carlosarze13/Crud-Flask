from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class ProfessorModel(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    city = db.Column(db.String(80))
    address = db.Column(db.String(80))
    salary =  db.Column(db.Integer())
 
    def __init__(self, first_name,last_name,city,address,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.address = address
        self.salary = salary
 
    def __repr__(self):
       return f'''ID:{self.id},
       Firstname: {self.first_name},
       Lastname: {self.last_name},
       City: {self.city},
       Address: {self.address},
       Salary: {self.salary}'''

