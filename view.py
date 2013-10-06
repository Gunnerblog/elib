from flask import Flask, session

app = Flask(__name__)
from flask import render_template
from flask import abort, redirect, url_for,request

from flask.ext import admin
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqlamodel import ModelView

from forms import RegistrationForm, AuthForm
from database import db_session, init_db
from models import User, Book, Author, Search


#admin enable 
class MyAdminIndexView(admin.AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('adminindex.html')

    def is_accessible(self):
        if 'username' in session:    
            user = User().get(session['username'])
            if user and user.is_staff:
                return True
            else:
                return False
        else:
            return False

admin = Admin(app,'App', index_view=MyAdminIndexView())
admin.add_view(ModelView(User, db_session))
admin.add_view(ModelView(Book, db_session))
admin.add_view(ModelView(Author, db_session))



SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
app.config.update(SECRET_KEY = SECRET_KEY)

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/home',  methods=['GET','POST'])
def home(name = None):
    if 'username' in session:
        user = User().get(session['username'])
        if request.method == "POST":
            search = Search(request.form['search'])
            result_dict = search.get_result()
            return render_template('home.html', books=result_dict, user=user)
        else:
            return render_template('home.html', books={}, user=user)
    else:
        return "You must login"


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if 'username' not in session:
        form = RegistrationForm(request.form)
        user = None
        if request.method == "POST" and form.validate():
            user = User().create(form.username.data, form.email.data, form.password.data)
            session['username'] = user.name
            return redirect(url_for('home'))
        else:
            return render_template('registration.html', form=form, user=user)
    else:
        return redirect(url_for('index'))

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route("/", methods=['GET', 'POST'])
def index():

    user = None
    if 'username' in session:
        user = User().get(session['username'])

    authform = AuthForm(request.form)
    if request.method == "POST" and authform.validate():
        user = User().authentication(authform.email.data, authform.password.data)
        session['username'] = user.name
        if user.is_staff:
            return redirect(url_for('admin'))
        else:         
            return redirect(url_for('home'))
    else:
        return render_template('index.html', authform=authform, user=user)

@app.route("/admin")
def admin():
    pass

if __name__ == "__main__":
    init_db()   
    app.run(debug=True)