from os import abort
from flask import Flask, render_template,request,redirect
from models import db,ProfessorModel
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbprofessor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all() 

@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        city = request.form['city']
        address = request.form['address']
        salary = request.form['salary']
        professor= ProfessorModel(first_name=first_name, last_name=last_name, city=city , address = address,salary=salary)
        db.session.add(professor)
        db.session.commit()
        return redirect('/data')
@app.route('/data')
def RetrieveDataList():
    professors = ProfessorModel.query.all()
    return render_template('datalist.html',professors= professors)
@app.route('/data/<int:id>')
def RetrieveSingleProfessor(id):
    professor = ProfessorModel.query.filter_by(id=id).first()
    if professor:
        return render_template('data.html', professor = professor)
    return f"Professor with id ={id} Doenst exist"
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    professor = ProfessorModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if professor:
            db.session.delete(professor)
            db.session.commit()
 
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            city = request.form['city']
            address = request.form['address']
            salary = request.form['salary']
            professor= ProfessorModel(first_name=first_name, last_name=last_name, city=city , address = address,salary=salary)
 
            db.session.add(professor)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Professor with id ={id} Doenst exist"
    return render_template('update.html', professor = professor)
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    professor = ProfessorModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if professor:
            db.session.delete(professor)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')
@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
