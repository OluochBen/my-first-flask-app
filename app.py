from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    """Home page route"""
    return "<p>Tembo School</p>"

@app.route('/courses/<int:course_id>')
def course_details(course_id):
    """Dynamic route for course details"""
    return f"Course ID: {course_id}"

@app.route('/courses')
def show_courses():
    """Courses listing page"""
    return "All Courses"

@app.route('/courses/<path:course_file>')
def course_file(course_file):
    """Path parameter example"""
    return f"Serving: {course_file}"

@app.route('/course_details')
def course_query():
    """Query parameters example"""
    name = request.args.get('name', default='Unknown Course')
    date = request.args.get('date', default='Unknown Date')
    return f"Course: {name} | Created: {date}"

@app.route('/about')
def about():
    """About page"""
    return "About Us"

@app.route('/contact')
def contact():
    """Contact page"""
    return "Contact Information"

if __name__ == "__main__":
    app.run(port=5000, debug=True)