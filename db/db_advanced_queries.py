import sqlite3

DB_PATH = 'db/registrar.db'

def get_db_connection():
    """Get database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_students_in_section(section_id):
    conn = get_db_connection()
    students = conn.execute('''
        SELECT s.StudentID, s.Name, s.Address, r.Grade
        FROM Student s
        JOIN Registration r ON s.StudentID = r.StudentID
        WHERE r.SectionID = ?
        ORDER BY s.Name
    ''', (section_id,)).fetchall()
    
    # Convert from Row objects to dictionaries
    result = [dict(student) for student in students]
    conn.close()
    return result

def get_courses_for_student(student_id):
    conn = get_db_connection()
    courses = conn.execute('''
        SELECT c.CourseID, c.CourseName, c.Rubric, c.CourseNumber, c.Credits,
               sec.Semester, sec.Year, r.Grade, sec.SectionID
        FROM Course c
        JOIN Section sec ON c.CourseID = sec.CourseID
        JOIN Registration r ON sec.SectionID = r.SectionID
        WHERE r.StudentID = ?
        ORDER BY sec.Year DESC, sec.Semester DESC
    ''', (student_id,)).fetchall()
    
    # Convert from Row objects to dictionaries
    result = [dict(course) for course in courses]
    conn.close()
    return result