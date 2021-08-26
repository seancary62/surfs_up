from flask import Flask

# New Instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

