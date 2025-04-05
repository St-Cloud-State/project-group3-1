from flask import Flask, jsonify, render_template, request
import sqlite3

from flask_cors import CORS
app = Flask(__name__)

CORS(app)

from db.db_operations import * 
from db.db_queries import *

app = Flask(__name__)

# Path to our SQLite database file
DATABASE = 'db/registrar.db'


# API to get all students
@app.route('/api/students', methods=['GET'])
def get_all_students_api():
    try:
        students = get_all_students()
        return jsonify(students)
    except Exception as e:
        return jsonify({'error': str(e)})

# API to add a student to the database
@app.route('/api/add_student', methods=['POST'])
def add_student_api():
    try:

        # Get student details from the request
        data = request.get_json()
        student_id = data.get('student_id')
        name = data.get('name')
        address = data.get('address')

        # Insert the student into the database
        success = create_student(student_id, name, address)

        if success: 
            return jsonify({'message': 'Student added successfully'})
        else:
            return jsonify({'error': 'Failed to add student'})
    except Exception as e:
        return jsonify({'error': str(e)})


# API to get all courses
@app.route('/api/courses', methods=['GET'])
def get_all_courses_api():
    try:
        courses = get_all_courses()
        return jsonify(courses)
    except Exception as e:
        return jsonify({'error': str(e)})

# API to get courses by rubric
@app.route('/api/courses/<rubric>', methods=['GET'])
def get_courses_by_rubric_api(rubric):
    try:
        courses = get_courses_by_rubric(rubric)
        return jsonify(courses)
    except Exception as e:
        return jsonify({'error': str(e)})

# API to add a course to the database
@app.route('/api/add_course', methods=['POST'])
def add_course_api():
    try:

        # Get course details from the request
        data = request.get_json()
        course_id = data.get('course_id')
        course_name = data.get('course_name')
        rubric = data.get('rubric')
        course_number = data.get('course_number')
        credits = data.get('credits')

        # Insert the course into the database
        success = create_course(course_id, course_name, rubric, course_number, credits)

        if success: 
            return jsonify({'message': 'Course added successfully'})
        else:
            return jsonify({'error': 'Failed to add course'})
    except Exception as e:
        return jsonify({'error': str(e)})


# API to get all sections
@app.route('/api/sections', methods=['GET'])
def get_all_sections_api():
    try:
        sections = get_all_sections()
        return jsonify(sections)
    except Exception as e:
        return jsonify({'error': str(e)})

# API to get sections by course
@app.route('/api/sections/<course_id>', methods=['GET'])
def get_sections_by_course_api(course_id):
    try:
        sections = get_sections_by_course_id(course_id)
        return jsonify(sections)
    except Exception as e:
        return jsonify({'error': str(e)})

# API to add a section to the database
@app.route('/api/add_section', methods=['POST'])
def add_section_api():
    try:

        # Get section details from the request
        data = request.get_json()
        section_id = data.get('section_id')
        course_id = data.get('course_id')
        semester = data.get('semester')
        year = data.get('year')

        # Insert the section into the database
        success = create_section(section_id, course_id, semester, year)

        if success: 
            return jsonify({'message': 'Section added successfully'})
        else:
            return jsonify({'error': 'Failed to add section'})
    except Exception as e:
        return jsonify({'error': str(e)})

# API to get all registrations
@app.route('/api/registrations', methods=['GET'])
def get_all_registrations_api():
    try:
        registrations = get_all_registrations()
        return jsonify([{'registration_id': r[0], 'student_id': r[1], 'section_id': r[2], 'grade': r[3]} for r in registrations])
    except Exception as e:
        return jsonify({'error': str(e)})



# Route to render the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Route to render the students.html page
@app.route('/students')
def students():
    return render_template('students.html')

# Route to render the courses.html page
@app.route('/courses')
def courses():
    return render_template('courses.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

# Route to render the sections.html page
@app.route('/sections')
def sections():
    return render_template('sections.html')

# Route to render the registration.html page
@app.route('/registration')
def registration():
    return render_template('registration.html')
