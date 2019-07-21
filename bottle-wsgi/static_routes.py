from bottle import Bottle, static_file

static_routes = Bottle()

@static_routes.route("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

@static_routes.route("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="static/js")  