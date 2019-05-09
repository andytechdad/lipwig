import json

def hello_world(version):
    hello_world = "Welcome to Lipwig. Version:" + str(version)
    output = json.dumps(hello_world)
    return output
