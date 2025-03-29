import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_queries import get_all_students, get_all_sections, get_all_courses, get_all_registrations

# Print all students
print("\n=== Students ===")
students = get_all_students()
for student in students:
    print(student)

# Print all courses
print("\n=== Courses ===")
courses = get_all_courses()
for course in courses:
    print(course)

# Print all sections
print("\n=== Sections ===")
sections = get_all_sections()
for section in sections:
    print(section)

# Print all registrations
print("\n=== Registrations ===")
registrations = get_all_registrations()
for registration in registrations:
    print(registration)