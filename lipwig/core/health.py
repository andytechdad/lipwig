import json
from collections import OrderedDict

def health_data():
    """ Returns a JSON object consisting of a small number of key/value pairs
    including application name, and status. These values are static for the
    moment, but could become dynamic in the future"""
    health_data = OrderedDict()
    health_data['application'] = 'lipwig'
    health_data['status'] = 'up'
    output = json.dumps(health_data)
    return output
