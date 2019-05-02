from flask import Flask, render_template, request, session

from src.common.database import Database
from src.models.blog import Blog
from src.models.user import User

app = Flask(__name__)
app.secret_key = "snake"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login_method():
    return render_template("login.html")


@app.route("/register")
def register_method():
    return render_template("register.html")


# @app.before_first_request
# def init_db():
#     Database.initialize()


@app.route("/auth/login", methods=['POST'])
def login_user():
    email = request.form["email"]
    password = request.form["password"]
    if User.login_valid(email,password):
        User.login(email)
    else:
        session["email"] = None

    return render_template("profile.html",email=session["email"])


@app.route("/auth/register", methods=['POST'])
def register_user():
    email = request.form["email"]
    password = request.form["password"]
    User.register(email,password)
    return render_template("profile.html",email=session["email"])


@app.route('/blogs/<string:user_id>')
@app.route('/blogs')
def page_infos(user_id=None):
    if user_id:
        user = User.get_by_id(user_id)
    else:
        user = User.get_by_email(email=session['email'])

    blogs = user.get_blogs()
    return render_template("user_blogs.html",blogs=blogs,email=user.email)



if __name__ == '__main__':
    app.run()