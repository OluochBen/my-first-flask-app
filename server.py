from flask import Flask

#Create a Flask application instance
app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Hello World<p>"

if __name__ == "__main__":
    app.run(port=5000, debug=True)

#Use flask --app server run