from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route("/login")
def login():
    return "<button>login</button>"


@auth.route("/logout")
def logout():
    return "<button>logout</button>"

@auth.route('sign-up')
def sign_up():
    return "<button>sign up</button>"