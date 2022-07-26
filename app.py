from markupsafe import escape
from flask import Flask
PORT = 5000
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    return 'Why Hello %s!\n' % username
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)