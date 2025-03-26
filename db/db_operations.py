import sqlite3

DB_PATH = 'db/registrar.db'

# CREATE OPERATIONS

def create_student(student_id, name, address=None, db_path=DB_PATH):
    """Add a new student to the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Student (StudentID, Name, Address) VALUES (?, ?, ?)",
            (student_id, name, address)
        )
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error creating student: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def create_course(course_id, course_name, rubric=None, course_number=None, credits=None, db_path=DB_PATH):
    """Add a new course to the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Course (CourseID, CourseName, Rubric, CourseNumber, Credits) VALUES (?, ?, ?, ?, ?)",
            (course_id, course_name, rubric, course_number, credits)
        )
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error creating course: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def create_section(section_id, course_id, semester=None, year=None, db_path=DB_PATH):
    """Add a new section to the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Section (SectionID, CourseID, Semester, Year) VALUES (?, ?, ?, ?)",
            (section_id, course_id, semester, year)
        )
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error creating section: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def create_registration(registration_id, student_id, section_id, grade=None, db_path=DB_PATH):
    """Register a student for a section."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Registration (RegistrationID, StudentID, SectionID, Grade) VALUES (?, ?, ?, ?)",
            (registration_id, student_id, section_id, grade)
        )
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error creating registration: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# UPDATE OPERATIONS

def update_student(student_id, name=None, address=None, db_path=DB_PATH):
    """Update a student's information."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        # Build the SET clause dynamically based on non-None parameters
        set_clause = []
        params = []
        
        if name is not None:
            set_clause.append("Name = ?")
            params.append(name)
        
        if address is not None:
            set_clause.append("Address = ?")
            params.append(address)
        
        if not set_clause:
            return False  # No updates to make
        
        # Add the student_id to params
        params.append(student_id)
        
        cursor.execute(
            f"UPDATE Student SET {', '.join(set_clause)} WHERE StudentID = ?",
            params
        )
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error updating student: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def update_course(course_id, course_name=None, rubric=None, course_number=None, credits=None, db_path=DB_PATH):
    """Update a course's information."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        set_clause = []
        params = []
        
        if course_name is not None:
            set_clause.append("CourseName = ?")
            params.append(course_name)
        
        if rubric is not None:
            set_clause.append("Rubric = ?")
            params.append(rubric)
        
        if course_number is not None:
            set_clause.append("CourseNumber = ?")
            params.append(course_number)
        
        if credits is not None:
            set_clause.append("Credits = ?")
            params.append(credits)
        
        if not set_clause:
            return False
        
        params.append(course_id)
        
        cursor.execute(
            f"UPDATE Course SET {', '.join(set_clause)} WHERE CourseID = ?",
            params
        )
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error updating course: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def update_section(section_id, semester=None, year=None, db_path=DB_PATH):
    """Update a section's information."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        set_clause = []
        params = []
        
        if semester is not None:
            set_clause.append("Semester = ?")
            params.append(semester)
        
        if year is not None:
            set_clause.append("Year = ?")
            params.append(year)
        
        if not set_clause:
            return False
        
        params.append(section_id)
        
        cursor.execute(
            f"UPDATE Section SET {', '.join(set_clause)} WHERE SectionID = ?",
            params
        )
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error updating section: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def update_registration(registration_id, grade=None, db_path=DB_PATH):
    """Update a student's grade in a registration."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        if grade is None:
            return False
        
        cursor.execute(
            "UPDATE Registration SET Grade = ? WHERE RegistrationID = ?",
            (grade, registration_id)
        )
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error updating registration: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# DELETE OPERATIONS

def delete_student(student_id, db_path=DB_PATH):
    """Delete a student from the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        # First, delete all registrations for this student
        cursor.execute("DELETE FROM Registration WHERE StudentID = ?", (student_id,))
        
        # Then, delete the student
        cursor.execute("DELETE FROM Student WHERE StudentID = ?", (student_id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error deleting student: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_course(course_id, db_path=DB_PATH):
    """Delete a course from the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        # First, get all sections for this course
        cursor.execute("SELECT SectionID FROM Section WHERE CourseID = ?", (course_id,))
        sections = cursor.fetchall()
        
        # Delete all registrations for these sections
        for section in sections:
            section_id = section[0]  # Tuple access instead of dictionary
            cursor.execute("DELETE FROM Registration WHERE SectionID = ?", (section_id,))
        
        # Delete all sections for this course
        cursor.execute("DELETE FROM Section WHERE CourseID = ?", (course_id,))
        
        # Finally, delete the course
        cursor.execute("DELETE FROM Course WHERE CourseID = ?", (course_id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error deleting course: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_section(section_id, db_path=DB_PATH):
    """Delete a section from the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        # First, delete all registrations for this section
        cursor.execute("DELETE FROM Registration WHERE SectionID = ?", (section_id,))
        
        # Then, delete the section
        cursor.execute("DELETE FROM Section WHERE SectionID = ?", (section_id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error deleting section: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def delete_registration(registration_id, db_path=DB_PATH):
    """Delete a registration from the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Registration WHERE RegistrationID = ?", (registration_id,))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error deleting registration: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()