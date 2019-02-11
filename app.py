from flask import Flask, render_template, request, redirect, url_for
import pymysql
from os import urandom
import facebook

# Initialize the app and mail server to send mail
app = Flask(__name__)
app.secret_key = urandom(100)

# Try to connect to the DB and handle error
try:
    db = pymysql.connect(host="localhost", user="root", passwd="", db="database")
    cur = db.cursor()

except:
    print("!---- YOUR SERVER IS NOT RUNNING ----!")
    exit(0)


# homepage
@app.route('/')
def home():
    return render_template('index.html')

# facebook login user : https://graph.facebook.com/oauth/access_token?client_id=your-app-id&client_secret=your-app-secret&grant_type=client_credentials"


# submit access token to generate data
@app.route('/submit', methods=['POST'])
def submit():
    token = request.form['token']
    graph = facebook.GraphAPI(access_token=token)
    post = graph.get_object(id='me', fields='id,name,posts,hometown')
    name = post['name']
    ht = post['hometown']['name']
    p = []
    for message in post['posts']['data']:
        try:
            p.append(message['message'])
        except KeyError:
            pass
    posts = ''.join(p)
    cur.execute("INSERT INTO data(name,hometown,posts) VALUES (%s,%s,%s)", (name, ht, posts))
    db.commit()
    return redirect(url_for('search'))


@app.route('/search')
def search():
    cur.execute("SELECT * from data")
    data = cur.fetchall()
    return render_template("search.html", result=data)


# finding interest by specific keyword
@app.route('/find', methods=['POST'])
def find():
    text = request.form['search']
    n = '%'+text+'%'
    cur.execute("SELECT * from data WHERE CONCAT(name,hometown,posts) LIKE %s", n)
    data = cur.fetchall()
    return render_template("search.html", result=data)


# Handeling HTTP errors
@app.errorhandler(400)
def bad_request(error):
    return render_template('errors/400.html', title='Bad Request'), 400


@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', title='Forbidden'), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', title='Page Not Found'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html', title='Server Error'), 500
