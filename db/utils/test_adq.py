import sqlite3
import sys, os
from pprint import pprint

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the functions from advanced_queries.py
from db_advanced_queries import get_students_in_section, get_courses_for_student

def test_get_students_in_section():
    """Test the get_students_in_section function with a predefined section ID."""
    section_id = 1  # CSCI101, Fall 2023 - based on your data
    print(f"\n=== Testing get_students_in_section({section_id}) ===")
    
    try:
        students = get_students_in_section(section_id)
        print(f"Found {len(students)} students in section {section_id} (CSCI101, Fall 2023):")
        for i, student in enumerate(students, 1):
            print(f"{i}. ID: {student['StudentID']}, Name: {student['Name']}, Grade: {student['Grade']}")
    except Exception as e:
        print(f"Error testing get_students_in_section: {e}")

def test_get_courses_for_student():
    """Test the get_courses_for_student function with a predefined student ID."""
    student_id = 1001  # Alice Smith - based on your data
    print(f"\n=== Testing get_courses_for_student({student_id}) ===")
    
    try:
        courses = get_courses_for_student(student_id)
        print(f"Found {len(courses)} courses for student {student_id} (Alice Smith):")
        for i, course in enumerate(courses, 1):
            print(f"{i}. {course['Rubric']} {course['CourseNumber']}: {course['CourseName']} "
                  f"({course['Semester']} {course['Year']}) - Grade: {course['Grade']}")
    except Exception as e:
        print(f"Error testing get_courses_for_student: {e}")

def test_specific_cases():
    """Test additional specific cases to validate functionality."""
    print("\n=== Testing Additional Specific Cases ===")
    
    # Test a section with multiple students (Section 13 - PHYS101, Fall 2023)
    section_id = 13
    students = get_students_in_section(section_id)
    print(f"Students in PHYS101, Fall 2023 (Section {section_id}): {len(students)}")
    
    # Test a student with multiple courses across semesters (Student 1010 - Julia Roberts)
    student_id = 1010
    courses = get_courses_for_student(student_id)
    print(f"Courses for Julia Roberts (Student {student_id}): {len(courses)}")
    
    # Check if ordering by year, semester works correctly
    if courses:
        print("Checking if courses are ordered by year and semester (most recent first):")
        for i, course in enumerate(courses, 1):
            print(f"{i}. {course['Semester']} {course['Year']} - {course['CourseName']}")

if __name__ == "__main__":
    print("Starting advanced queries test...")
        
    # Run the tests
    test_get_students_in_section()
    test_get_courses_for_student()
    test_specific_cases()
    
    print("\nTesting complete!")