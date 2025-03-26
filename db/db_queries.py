import sqlite3

DB_PATH = 'db/registrar.db'

# STUDENT

def get_all_students(db_path=DB_PATH):
    """Get all students from the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Student")
        students = cursor.fetchall()
        return students
    except sqlite3.Error as e:
        print(f"Error getting students: {e}")
        return []
    finally:
        conn.close()

def get_student_by_id(student_id, db_path=DB_PATH):
    """Get a specific student by ID."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Student WHERE StudentID = ?", (student_id,))
        student = cursor.fetchone()
        return student
    except sqlite3.Error as e:
        print(f"Error getting student: {e}")
        return None
    finally:
        conn.close()

def get_students_by_name(name, db_path=DB_PATH):
    """Get students by name (partial match)."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Student WHERE Name LIKE ?", (f"%{name}%",))
        students = cursor.fetchall()
        return students
    except sqlite3.Error as e:
        print(f"Error getting students by name: {e}")
        return []
    finally:
        conn.close()

# COURSE

def get_all_courses(db_path=DB_PATH):
    """Get all courses from the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Course")
        courses = cursor.fetchall()
        return courses
    except sqlite3.Error as e:
        print(f"Error getting courses: {e}")
        return []
    finally:
        conn.close()

def get_course_by_id(course_id, db_path=DB_PATH):
    """Get a specific course by ID."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Course WHERE CourseID = ?", (course_id,))
        course = cursor.fetchone()
        return course
    except sqlite3.Error as e:
        print(f"Error getting course: {e}")
        return None
    finally:
        conn.close()

def get_courses_by_rubric(rubric, db_path=DB_PATH):
    """Get all courses with a specific rubric."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Course WHERE Rubric = ?", (rubric,))
        courses = cursor.fetchall()
        return courses
    except sqlite3.Error as e:
        print(f"Error getting courses by rubric: {e}")
        return []
    finally:
        conn.close()

def get_courses_by_number(course_number, db_path=DB_PATH):
    """Get all courses with a specific course number."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Course WHERE CourseNumber = ?", (course_number,))
        courses = cursor.fetchall()
        return courses
    except sqlite3.Error as e:
        print(f"Error getting courses by number: {e}")
        return []
    finally:
        conn.close()

def get_courses_by_credits(credits, db_path=DB_PATH):
    """Get all courses with a specific credit value."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Course WHERE Credits = ?", (credits,))
        courses = cursor.fetchall()
        return courses
    except sqlite3.Error as e:
        print(f"Error getting courses by credits: {e}")
        return []
    finally:
        conn.close()

# SECTION

def get_all_sections(db_path=DB_PATH):
    """Get all sections from the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Section")
        sections = cursor.fetchall()
        return sections
    except sqlite3.Error as e:
        print(f"Error getting sections: {e}")
        return []
    finally:
        conn.close()

def get_section_by_id(section_id, db_path=DB_PATH):
    """Get a specific section by ID."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Section WHERE SectionID = ?", (section_id,))
        section = cursor.fetchone()
        return section
    except sqlite3.Error as e:
        print(f"Error getting section: {e}")
        return None
    finally:
        conn.close()

def get_sections_by_course_id(course_id, db_path=DB_PATH):
    """Get all sections for a specific course."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Section WHERE CourseID = ?", (course_id,))
        sections = cursor.fetchall()
        return sections
    except sqlite3.Error as e:
        print(f"Error getting sections by course: {e}")
        return []
    finally:
        conn.close()

def get_sections_by_semester(semester, db_path=DB_PATH):
    """Get all sections for a specific semester."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Section WHERE Semester = ?", (semester,))
        sections = cursor.fetchall()
        return sections
    except sqlite3.Error as e:
        print(f"Error getting sections by semester: {e}")
        return []
    finally:
        conn.close()

def get_sections_by_year(year, db_path=DB_PATH):
    """Get all sections for a specific year."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Section WHERE Year = ?", (year,))
        sections = cursor.fetchall()
        return sections
    except sqlite3.Error as e:
        print(f"Error getting sections by year: {e}")
        return []
    finally:
        conn.close()

def get_sections_by_semester_year(semester, year, db_path=DB_PATH):
    """Get all sections for a specific semester and year."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Section WHERE Semester = ? AND Year = ?", (semester, year))
        sections = cursor.fetchall()
        return sections
    except sqlite3.Error as e:
        print(f"Error getting sections by semester and year: {e}")
        return []
    finally:
        conn.close()

# REGISTRATION

def get_all_registrations(db_path=DB_PATH):
    """Get all registrations from the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Registration")
        registrations = cursor.fetchall()
        return registrations
    except sqlite3.Error as e:
        print(f"Error getting registrations: {e}")
        return []
    finally:
        conn.close()

def get_registration_by_id(registration_id, db_path=DB_PATH):
    """Get a specific registration by ID."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Registration WHERE RegistrationID = ?", (registration_id,))
        registration = cursor.fetchone()
        return registration
    except sqlite3.Error as e:
        print(f"Error getting registration: {e}")
        return None
    finally:
        conn.close()

def get_registrations_by_student_id(student_id, db_path=DB_PATH):
    """Get all registrations for a specific student."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Registration WHERE StudentID = ?", (student_id,))
        registrations = cursor.fetchall()
        return registrations
    except sqlite3.Error as e:
        print(f"Error getting registrations by student: {e}")
        return []
    finally:
        conn.close()

def get_registrations_by_section_id(section_id, db_path=DB_PATH):
    """Get all registrations for a specific section."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Registration WHERE SectionID = ?", (section_id,))
        registrations = cursor.fetchall()
        return registrations
    except sqlite3.Error as e:
        print(f"Error getting registrations by section: {e}")
        return []
    finally:
        conn.close()

def get_registrations_by_grade(grade, db_path=DB_PATH):
    """Get all registrations with a specific grade."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Registration WHERE Grade = ?", (grade,))
        registrations = cursor.fetchall()
        return registrations
    except sqlite3.Error as e:
        print(f"Error getting registrations by grade: {e}")
        return []
    finally:
        conn.close()