import json
from collections import OrderedDict

def return_help(version):
    help_data = OrderedDict()
    help_data['Lipwig Version'] = str(version)
    endpoints = OrderedDict()
    endpoints["/"] = "This Help Page"
    endpoints["/healthcheck"] = "Healthchecker"
    help_data['endpoints'] = endpoints
    output = json.dumps(help_data)
    return output
