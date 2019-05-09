from flask import Flask
from core import simple
app = Flask(__name__)

@app.route("/")
def hello():
    hello_world = simple.hello_world()
    return hello_world

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
