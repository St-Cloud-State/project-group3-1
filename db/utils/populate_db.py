import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import db_operations as operations

# Function to populate all tables
def populate_database():
    # Add students
    populate_students()
    
    # Add courses
    populate_courses()
    
    # Add sections
    populate_sections()
    
    # Add registrations
    populate_registrations()
    
    print("Database population complete!")

# Function to populate Student table
def populate_students():
    print("Adding students...")
    for student in student_data:
        student_id, name, address = student
        success = operations.create_student(student_id, name, address)
        if success:
            print(f"Added student: {name}")
        else:
            print(f"Failed to add student: {name}")

# Function to populate Course table
def populate_courses():
    print("Adding courses...")
    for course in course_data:
        course_id, course_name, rubric, course_number, credits = course
        success = operations.create_course(course_id, course_name, rubric, course_number, credits)
        if success:
            print(f"Added course: {course_name}")
        else:
            print(f"Failed to add course: {course_name}")

# Function to populate Section table
def populate_sections():
    print("Adding sections...")
    for section in section_data:
        section_id, course_id, semester, year = section
        success = operations.create_section(section_id, course_id, semester, year)
        if success:
            print(f"Added section: {section_id} for course {course_id}")
        else:
            print(f"Failed to add section: {section_id} for course {course_id}")

# Function to populate Registration table
def populate_registrations():
    print("Adding registrations...")
    for registration in registration_data:
        registration_id, student_id, section_id, grade = registration
        success = operations.create_registration(registration_id, student_id, section_id, grade)
        if success:
            print(f"Added registration: {registration_id}")
        else:
            print(f"Failed to add registration: {registration_id}")

student_data = [
    (1001, "Alice Smith", "123 Main St"),
    (1002, "Bob Johnson", "456 Elm St"),
    (1003, "Charlie Brown", "789 Oak St"),
    (1004, "Diana Ross", "101 Pine Ave"),
    (1005, "Edward Norton", "202 Maple Dr"),
    (1006, "Fiona Apple", "303 Cedar Ln"),
    (1007, "George Clooney", "404 Birch Rd"),
    (1008, "Hannah Montana", "505 Walnut Blvd"),
    (1009, "Ian McKellen", "606 Spruce Way"),
    (1010, "Julia Roberts", "707 Redwood Ct")
]
    
course_data = [
    ("CSCI101", "Introduction to Programming", "CSCI", 101, 3),
    ("CSCI201", "Data Structures", "CSCI", 201, 4),
    ("MATH150", "Calculus I", "MATH", 150, 4),
    ("MATH250", "Linear Algebra", "MATH", 250, 3),
    ("ENG120", "College Writing", "ENG", 120, 3),
    ("PHYS101", "Physics I", "PHYS", 101, 4),
    ("CHEM110", "Chemistry I", "CHEM", 110, 4),
    ("HIST105", "World History", "HIST", 105, 3),
    ("BIO120", "Biology I", "BIO", 120, 4),
    ("PSY101", "Introduction to Psychology", "PSY", 101, 3)
]

section_data = [
    (1, "CSCI101", "Fall", 2023),
    (2, "CSCI101", "Spring", 2024),
    (3, "CSCI201", "Fall", 2023),
    (4, "CSCI201", "Spring", 2024),
    (5, "CSCI201", "Summer", 2024),  # Summer 2024 for even course
    (6, "MATH150", "Fall", 2023),
    (7, "MATH150", "Spring", 2024),
    (8, "MATH250", "Fall", 2023),
    (9, "MATH250", "Spring", 2024),
    (10, "MATH250", "Summer", 2024),  # Summer 2024 for even course
    (11, "ENG120", "Fall", 2023),
    (12, "ENG120", "Spring", 2024),
    (13, "PHYS101", "Fall", 2023),
    (14, "PHYS101", "Spring", 2024),
    (15, "CHEM110", "Fall", 2023),
    (16, "CHEM110", "Spring", 2024),
    (17, "CHEM110", "Summer", 2024),  # Summer 2024 for even course
    (18, "HIST105", "Fall", 2023),
    (19, "HIST105", "Spring", 2024),
    (20, "HIST105", "Summer", 2024),  # Summer 2024 for even course
    (21, "BIO120", "Fall", 2023),
    (22, "BIO120", "Spring", 2024),
    (23, "PSY101", "Fall", 2023),
    (24, "PSY101", "Spring", 2024),
]
   
registration_data = [
    # Fall 2023 courses
    (1, 1001, 1, 3.0),   # Alice Smith - CSCI101, Fall 2023 - Grade B
    (2, 1001, 6, 4.0),   # Alice Smith - MATH150, Fall 2023 - Grade A
    (3, 1001, 11, 2.0),  # Alice Smith - ENG120, Fall 2023 - Grade C
    (4, 1002, 3, 4.0),   # Bob Johnson - CSCI201, Fall 2023 - Grade A
    (5, 1002, 13, 3.0),  # Bob Johnson - PHYS101, Fall 2023 - Grade B
    (6, 1002, 18, 1.0),  # Bob Johnson - HIST105, Fall 2023 - Grade D
    (7, 1003, 21, 2.0),  # Charlie Brown - BIO120, Fall 2023 - Grade C
    (8, 1003, 7, 4.0),   # Charlie Brown - MATH150, Fall 2023 - Grade A
    (9, 1003, 23, 3.0),  # Charlie Brown - PSY101, Fall 2023 - Grade B
    (10, 1004, 13, 4.0), # Diana Ross - PHYS101, Fall 2023 - Grade A
    (11, 1004, 8, 3.0),  # Diana Ross - MATH250, Fall 2023 - Grade B
    (12, 1005, 1, 2.0),  # Edward Norton - CSCI101, Fall 2023 - Grade C
    (13, 1005, 18, 1.0), # Edward Norton - HIST105, Fall 2023 - Grade D
    (14, 1006, 21, 4.0), # Fiona Apple - BIO120, Fall 2023 - Grade A
    (15, 1006, 5, 3.0),  # Fiona Apple - CSCI201, Fall 2023 - Grade B
    (16, 1007, 23, 1.0), # George Clooney - PSY101, Fall 2023 - Grade D
    (17, 1007, 6, 4.0),  # George Clooney - MATH150, Fall 2023 - Grade A
    (18, 1008, 11, 2.0), # Hannah Montana - ENG120, Fall 2023 - Grade C
    (19, 1008, 13, 3.0), # Hannah Montana - PHYS101, Fall 2023 - Grade B
    (20, 1009, 21, 4.0), # Ian McKellen - BIO120, Fall 2023 - Grade A
    (21, 1009, 7, 3.0),  # Ian McKellen - MATH150, Fall 2023 - Grade B
    (22, 1010, 13, 2.0), # Julia Roberts - PHYS101, Fall 2023 - Grade C
    (23, 1010, 1, 4.0),  # Julia Roberts - CSCI101, Fall 2023 - Grade A
    (24, 1010, 11, 3.0), # Julia Roberts - ENG120, Fall 2023 - Grade B
    (25, 1004, 6, 2.0),  # Diana Ross - MATH150, Fall 2023 - Grade C
    (26, 1006, 18, 4.0), # Fiona Apple - HIST105, Fall 2023 - Grade A
    (27, 1009, 23, 1.0), # Ian McKellen - PSY101, Fall 2023 - Grade D
    (28, 1010, 21, 3.0), # Julia Roberts - BIO120, Fall 2023 - Grade B
    (29, 1001, 8, 4.0),  # Alice Smith - MATH250, Fall 2023 - Grade A
    (30, 1008, 18, 3.0), # Hannah Montana - HIST105, Fall 2023 - Grade B

    # Spring 2024 courses
    (31, 1001, 2, 4.0),   # Alice Smith - CSCI101, Spring 2024 - Grade A
    (32, 1001, 7, 3.0),   # Alice Smith - MATH150, Spring 2024 - Grade B
    (33, 1002, 4, 2.0),   # Bob Johnson - CSCI201, Spring 2024 - Grade C
    (34, 1002, 13, 1.0),  # Bob Johnson - PHYS101, Spring 2024 - Grade D
    (35, 1002, 19, 4.0),  # Bob Johnson - HIST105, Spring 2024 - Grade A
    (36, 1003, 22, 3.0),  # Charlie Brown - BIO120, Spring 2024 - Grade B
    (37, 1003, 24, 4.0),  # Charlie Brown - PSY101, Spring 2024 - Grade A
    (38, 1003, 12, 2.0),  # Charlie Brown - ENG120, Spring 2024 - Grade C
    (39, 1004, 19, 1.0),  # Diana Ross - HIST105, Spring 2024 - Grade D
    (40, 1004, 7, 4.0),   # Diana Ross - MATH150, Spring 2024 - Grade A
    (41, 1005, 12, 3.0),  # Edward Norton - ENG120, Spring 2024 - Grade B
    (42, 1005, 4, 2.0),   # Edward Norton - CSCI201, Spring 2024 - Grade C
    (43, 1006, 22, 1.0),  # Fiona Apple - BIO120, Spring 2024 - Grade D
    (44, 1006, 19, 3.0),  # Fiona Apple - HIST105, Spring 2024 - Grade B
    (45, 1007, 24, 4.0),  # George Clooney - PSY101, Spring 2024 - Grade A
    (46, 1007, 7, 3.0),   # George Clooney - MATH150, Spring 2024 - Grade B
    (47, 1008, 12, 2.0),  # Hannah Montana - ENG120, Spring 2024 - Grade C
    (48, 1008, 13, 1.0),  # Hannah Montana - PHYS101, Spring 2024 - Grade D
    (49, 1009, 22, 4.0),  # Ian McKellen - BIO120, Spring 2024 - Grade A
    (50, 1009, 7, 3.0),   # Ian McKellen - MATH150, Spring 2024 - Grade B
    (51, 1010, 13, 2.0),  # Julia Roberts - PHYS101, Spring 2024 - Grade C
    (52, 1010, 19, 1.0),  # Julia Roberts - HIST105, Spring 2024 - Grade D
    (53, 1010, 12, 4.0),  # Julia Roberts - ENG120, Spring 2024 - Grade A
    (54, 1001, 24, 3.0),  # Alice Smith - PSY101, Spring 2024 - Grade B
    (55, 1004, 19, 2.0),  # Diana Ross - HIST105, Spring 2024 - Grade C
    (56, 1006, 22, 1.0),  # Fiona Apple - BIO120, Spring 2024 - Grade D
    (57, 1009, 24, 3.0),  # Ian McKellen - PSY101, Spring 2024 - Grade B
    (58, 1010, 7, 4.0),   # Julia Roberts - MATH150, Spring 2024 - Grade A
    (59, 1008, 2, 2.0),   # Hannah Montana - CSCI101, Spring 2024 - Grade C
    (60, 1005, 4, 1.0),   # Edward Norton - CSCI201, Spring 2024 - Grade D

    # Summer 2024 courses (unchanged)
    (61, 1002, 5, None),  # Bob Johnson - CSCI201, Summer 2024
    (62, 1003, 10, None), # Charlie Brown - MATH250, Summer 2024
    (63, 1007, 20, None), # George Clooney - HIST105, Summer 2024
]

if __name__ == "__main__":
    populate_database()