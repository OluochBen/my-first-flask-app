from flask import Flask

#Create a Flask application instance
app = Flask(__name__)

#Added app routes
@app.route('/')
def index():
    return "<p>Hello World<p>"

#Configure how app is run
if __name__ == "__main__":
    app.run(port=5000, debug=True)

#web service gateway interface