from flask import Flask
from core import index
from core import health
from yaml import load

app = Flask(__name__)

config_file = 'config.yaml'

def get_version(config_file):
    with open(config_file, 'rb') as config:
        loader = load(config)
        try:
            version = loader['version']
            print(version)
        except TypeError:
            version = "CONFIG LOAD FAILURE"
            print(version)
        config.close()
    return version

@app.route("/")
def default_index():
    version = get_version(config_file)
    default = index.return_help(version)
    return default

@app.route("/healthcheck")
def healthchecker():
    healthcheck_output = health.health_data()
    return healthcheck_output

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8888)
