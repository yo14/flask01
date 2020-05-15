from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from models import db, Page, Menu
from views import PageModelView

app = Flask(__name__)
app.config.from_pyfile('settings.py')

db.init_app(app)

admin = Admin(app, name='Flask01', template_mode='bootstrap3')
admin.add_view(PageModelView(Page, db.session))
admin.add_view(ModelView(Menu, db.session))

@app.route('/')
@app.route('/<url>')
def index(url=None):
    page = Page.query.first()
    if url is not None:
        page = Page.query.filter_by(url=url).first()

    contents = 'empty'
    if page is not None:
        contents = page.contents

    menu = Menu.query.order_by('order')

    return render_template('index.html', TITLE='Flask-01', CONTENT=contents, menu=menu)


# @app.route('/testdb')
# def testdeb():
#     import psycopg2
#
#     con = psycopg2.connect('dbname=flask01 user=postgres password=bebasroot host=localhost')
#     cur = con.cursor()
#
#     cur.execute('select * from page;')
#     id,title = cur.fetchone()
#     con.close()
#
#     return 'Output table page: {} - {}'.format(id, title)


app.run('0.0.0.0', debug=True)