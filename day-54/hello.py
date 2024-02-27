from flask import Flask

app = Flask(__name__)
print(__name__)


@app.route('/')
def hello():
    return '<h1  style="text-align: center"> Hello, World!</h1>'


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


@app.route('/bye')
def bye():
    return 'Bye!'


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f'Hello there {name}, you are {number} years!'


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function()

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f'This is {user.name} new blog post ')


if __name__ == '__main__':
    app.run(debug=True)
