from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import sqlite3

# Importing functions from separate modules
from db.db_operations import *
from db.db_queries import *

app = Flask(__name__)
CORS(app)

# Path to our SQLite database file
DATABASE = 'db/registrar.db'

# Helper function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Students Page
@app.route('/students')
def students():
    return render_template('students.html')

# Courses Page
@app.route('/courses')
def courses():
    return render_template('courses.html')

# Sections Page
@app.route('/sections')
def sections():
    return render_template('sections.html')

# Registration Page
@app.route('/registration')
def registration():
    return render_template('registration.html')

# API to get all students
@app.route('/api/students', methods=['GET'])
def get_all_students_api():
    try:
        students = get_all_students()
        return jsonify(students)
    except Exception as e:
        return jsonify({'error': str(e)})

# API to add a student
@app.route('/api/add_student', methods=['POST'])
def add_student_api():
    try:
        data = request.get_json()
        student_id = data.get('student_id')
        name = data.get('name')
        address = data.get('address')
        success = create_student(student_id, name, address)
        if success:
            return jsonify({'message': 'Student added successfully'})
        else:
            return jsonify({'error': 'Failed to add student'})
    except Exception as e:
        return jsonify({'error': str(e)})

# API to remove a student
@app.route('/api/delete_student/<int:student_id>', methods=['DELETE'])
def delete_student_api(student_id):
    try:
        success = delete_student(student_id)
        if success:
            return jsonify({'message': 'Student deleted successfully'})
        else:
            return jsonify({'error': 'Failed to delete student'})
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

# API to add a course
@app.route('/api/add_course', methods=['POST'])
def add_course_api():
    try:
        data = request.get_json()
        course_id = data.get('course_id')
        course_name = data.get('course_name')
        rubric = data.get('rubric')
        course_number = data.get('course_number')
        credits = data.get('credits')
        success = create_course(course_id, course_name, rubric, course_number, credits)
        if success:
            return jsonify({'message': 'Course added successfully'})
        else:
            return jsonify({'error': 'Failed to add course'})
    except Exception as e:
        return jsonify({'error': str(e)})

# API to remove a course
@app.route('/api/delete_course/<course_id>', methods=['DELETE'])
def delete_course_api(course_id):
    try:
        success = delete_course(course_id)
        if success:
            return jsonify({'message': 'Course deleted successfully'})
        else:
            return jsonify({'error': 'Failed to delete course'})
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

# API to add a section
@app.route('/api/add_section', methods=['POST'])
def add_section_api():
    try:
        data = request.get_json()
        section_id = data.get('section_id')
        course_id = data.get('course_id')
        semester = data.get('semester')
        year = data.get('year')
        success = create_section(section_id, course_id, semester, year)
        if success:
            return jsonify({'message': 'Section added successfully'})
        else:
            return jsonify({'error': 'Failed to add section'})
    except Exception as e:
        return jsonify({'error': str(e)})

# API to remove a section
@app.route('/api/delete_section/<int:section_id>', methods=['DELETE'])
def delete_section_api(section_id):
    try:
        success = delete_section(section_id)
        if success:
            return jsonify({'message': 'Section deleted successfully'})
        else:
            return jsonify({'error': 'Failed to delete section'})
    except Exception as e:
        return jsonify({'error': str(e)})


# API to get all registrations
@app.route('/api/registrations', methods=['GET'])
def get_all_registrations_api():
    try:
        registrations = get_all_registrations()
        return jsonify(registrations)
    except Exception as e:
        return jsonify({'error': str(e)})

# API to add a registration
@app.route('/api/add_registration', methods=['POST'])
def add_registration_api():
    try:
        data = request.get_json()
        registration_id = data.get('registration_id')
        student_id = data.get('student_id')
        section_id = data.get('section_id')
        grade = data.get('grade')

        success = create_registration(registration_id, student_id, section_id, grade)
        if success:
            return jsonify({'message': 'Registration added successfully'})
        else:
            return jsonify({'error': 'Failed to add registration'})
    except Exception as e:
        return jsonify({'error': str(e)})

 # API to remove a registration
@app.route('/api/delete_registration/<int:registration_id>', methods=['DELETE'])
def delete_registration_api(registration_id):
    try:
        success = delete_registration(registration_id)
        if success:
            return jsonify({'message': 'Registration deleted successfully'})
        else:
            return jsonify({'error': 'Failed to delete registration'})
    except Exception as e:
        return jsonify({'error': str(e)})     

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
