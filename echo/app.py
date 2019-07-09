from bottle import Bottle, route, run, abort
import requests
import os
from urllib.parse import urlparse

app = Bottle(__name__)

@app.route('/echo/<string>')
def echo(string):
    return '{0}'.format(string)

@app.route('/error/<code:int>')
def error(code, description = None):
    abort(code,description)

@app.route('/servicecall')
def servicecall():
    api_endpoint = urlparse('{0}'.format(os.environ['API_ENDPOINT']))
    if not api_endpoint.geturl() or not api_endpoint.scheme:
        error(400, 'no environment variable API_ENDPOINT set or no scheme provided')
    else:  
        return requests.get(api_endpoint.geturl()).content


if __name__ == '__main__':
    app.run()
