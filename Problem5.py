

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')

def index1():
    return render_template('index.html')


mydict={'002':["aaa",20,"M"]}

@app.route('/insert',method=['POST'])
def insert():
    if request.method=="POST":
        name= request.form['name']
        rollno = request.form['rollno']
        age = request.form['age']
        gender = request.form['gender']

        mydict.append('rollno':[name, age, gender])


def update(request.form["rollno"]):
    if request.method == "UPDATE":
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']

        mydict.update('rollno': [name, age, gender])


def delete(request.form['rollno']):
    if request.method == "DELETE":
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        del mydict["rollno"]

def search()

app.debug= True


if __name__ == '__main__':
    app.run(debug=True)
