from flask import Flask, render_template

from models import db, Page

app = Flask(__name__)
app.config.from_pyfile('settings.py')

db.init_app(app)

@app.route('/')
def index():
    # ini cara pyspg dari latihan sebelumnya
    # import psycopg2
    # con = psycopg2.connect('dbname=flask01 user=postgres password=bebasroot host=localhost')
    # cur = con.cursor()
    # cur.execute('select contents from page where id=1;')
    # contents = cur.fetchone()
    # con.close()

    page = Page.query.filter_by(id=1).first()

    return render_template('index.html', TITLE='Flask-01', CONTENT=page.contents)

@app.route('/about')
def about():
    return render_template('about.html', TITLE='Flask-01')

@app.route('/testdb')
def testdeb():
    import psycopg2

    con = psycopg2.connect('dbname=flask01 user=postgres password=bebasroot host=localhost')
    cur = con.cursor()

    cur.execute('select * from page;')
    id,title = cur.fetchone()
    con.close()

    return 'Output table page: {} - {}'.format(id, title)


app.run('0.0.0.0', debug=True)