from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:1234@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

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


class Entry(db.Model):
    '''
    Stores stories
    '''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180))
    body = db.Column(db.String(1000))
    #created = db.Column(db.datetime)

    def __init__(self, title, body):
        self.title = title
        self.body = body
        #self.created = datetime.datetime.utcnow()

    def is_valid(self):
        if self.title and self.body:
            return True
        else:
            return False
        #

@app.route("/")  
def index():
    return redirect("/blog")
    
@app.route("/blog")

def display_blog_entries():
    # TODO refractor to use routes with variable instead of get parameters
    entry_id = request.args.get('id')
    if (entry_id):
        entry = Entry.query.get(entry_id)
        return render_template('single_entry.html', title="Blog Entry", entry=entry)
# if we're here, we need to display all the entries
# TODO store sort direction in session() so we remember users perference
    sort = request.args.get('sort')
    if sort=="newest":
        all_entries = Entry.query.order_by(Entry.created.desc().all())
    else:
        all_entries = Entry.query.all()
    return render_template('all_entries.html', title="All entries", all_entries = all_entries)

@app.route('/new_entry', methods=['GET','POST'])
def new_entry():
    '''
    GET: Display form for new blog entry
    POST: create new entry or redisplay form if entries are invalid
    '''
    if request.method =='POST':
        new_entry_title = request.form['title']
        new_entry_body = request.form['body']
        new_entry = Entry(new_entry_title, new_entry_body)

        if new_entry.is_valid():
            db.session.add(new_entry)
            db.session.commit()

            # display just this most recent blog entry
            url = "/blog?id=" + str(new_entry.id)
            return redirect(url)
        else:
            flash("Please check your entry for errors, both a title and body must be present")
            return render_template('new_entry_form.html',
        title="Create new blog entry",
        new_entry_title=new_entry_title,
        new_entry_body=new_entry_body)

    else:
        return render_template('new_entry_form.html', title="Create new story entry")

    #
if __name__ == '__main__':
    app.run()

#extra stuff
#class User():
#   id = (db.Integer, primary_key=True)
#    username = db.Column(db.String(32))
#    password = db.Column(db.String(32))
#blogs signifies the user to the posts they write
#   blogs = db.Column()