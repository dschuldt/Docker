import bottle, pyclamd, os
from bottle import route, run, request, HTTPResponse

app = bottle.default_app()
na_error = "ClamAV daemon is not ready to accept requests"

@route('/info')
def info():
    try:
        return "ClamAV version {0}".format(pyclamd.ClamdUnixSocket().version())
    except:
        return bottle.HTTPResponse(status=503, body=na_error)

@route('/scan', method='POST')
def scan():
    try:
        cd = pyclamd.ClamdUnixSocket()
        upload = request.files.get('data')
        upload.save('/tmp/',True)
        scan = cd.scan_file('/tmp/{0}'.format(upload.filename))
        result = str(scan)
        os.remove('/tmp/{0}'.format(upload.filename))
        if scan is None:
            return bottle.HTTPResponse(status=204)
        else:
            return result[result.find(':')+2:-1]
    except:
        return bottle.HTTPResponse(status=503, body=na_error)
        
if __name__ == "__main__":
    run(host='localhost', port=8080)
