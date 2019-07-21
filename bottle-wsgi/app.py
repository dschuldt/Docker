from bottle import Bottle, route, run, view, static_file
from static_routes import static_routes

application = Bottle()
application.mount("/static", static_routes)

@application.route('/')
@view('index')
def main():
    return dict(greeting="Hello World, this is Bottle")

if __name__ == '__main__':
    application.run(reloader=True)
