from flask import Flask
from markupsafe import escape
from random import randint
from flask import request

app = Flask(__name__)

@app.route('/user/<name>')
def index(name):
    return \
f'''
<html>
    <head>
        <title>0000</title>
    </head>
    
    <body>
        <h1>jjjjj</h1>

        <h2>RANDOM int is :{randint(1,100)}</h2>
        <h2>Hello,{name}</h2>
    </body>
</html>
'''

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()