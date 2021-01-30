from bottle import Bottle
from login import uri

app = Bottle()

app.run(debug=True, reloader=True)
