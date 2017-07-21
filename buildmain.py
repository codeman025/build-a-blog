from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:1234@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


#single blog entry url = ./blog?id=6

form = """
<!doctype html>
<html>
    <body>
        <form action="/blogpost" method="post">
            <label for="first-name">First Name:</label>
            <input type="text" name="first_name" />
            <input type="submit" />
        </form>
    </body>
</html>
"""
#forms in flask code
# @app.route("/")
#def index():
#   return form

#   app.run()
#form_value = request.args.get("whatevernameforGETmethod")
#http://localhost:5000/blogpost?first_name=userinput
#if 'post' need the specify methods
@app.route("/blogpost", methods=['POST','GET'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '</h1>'




@app.route("/")
class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self, name):
        self.name = name

class Blog(id,title,body):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))

    def __init__(self,title,body):
        self.title = title
        self.body = body

tasks = []

@app.route('/blog', methods= ['GET'])
@app.route('newpost', methods=['GET'])



@app.route('/',methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('todos.html',title="build-a-blog",tasks=tasks)

if __name__ == '__main__':
    app.run()