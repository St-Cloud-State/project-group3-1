import sqlite3

import sys
import os
# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db_operations import *
from db_queries import *

def test_create_operations():
    student_data = [
        (2001, "Mark Johnson", "800 Pine Street"),
        (2002, "Sarah Williams", "921 Oak Avenue"),
        (2003, "James Anderson", "435 Maple Boulevard")
    ]
    
    for student in student_data:
        create_student(student[0], student[1], student[2])
    print("Added 3 new students")
    
    course_data = [
        ("CSCI301", "Advanced Programming", "CSCI", 301, 4),
        ("ENG220", "Creative Writing", "ENG", 220, 3),
        ("PHYS201", "Physics II", "PHYS", 201, 4)
    ]
    
    for course in course_data:
        create_course(course[0], course[1], course[2], course[3], course[4])
    print("Added 3 new courses")
    
    section_data = [
        (101, "CSCI301", "Fall", 2024),
        (102, "ENG220", "Spring", 2025),
        (103, "PHYS201", "Summer", 2024)
    ]
    
    for section in section_data:
        create_section(section[0], section[1], section[2], section[3])
    print("Added 3 new sections")
    
    registration_data = [
        (101, 2001, 101, 3.0),
        (102, 2002, 102, 4.0),
        (103, 2003, 103, 3.0)
    ]
    
    for reg in registration_data:
        create_registration(reg[0], reg[1], reg[2], reg[3])
    print("Added 3 new registrations")

def test_read_operations():
    """Test all read operations."""
    print("\n--- Testing Read Operations ---")
    
    # Test student reads
    print("\nStudent Reads:")
    all_students = get_all_students()
    print(f"All students count: {len(all_students)}")
    
    student = get_student_by_id(2001)
    print(f"Student 2001: {student}")
    
    students_by_name = get_students_by_name("Johnson")
    print(f"Students with 'Johnson' in name: {len(students_by_name)}")
    
    # Test course reads
    print("\nCourse Reads:")
    all_courses = get_all_courses()
    print(f"All courses count: {len(all_courses)}")
    
    course = get_course_by_id("CSCI301")
    print(f"Course CSCI301: {course}")
    
    cs_courses = get_courses_by_rubric("CSCI")
    print(f"CSCI Courses: {len(cs_courses)}")
    
    math_courses = get_courses_by_rubric("MATH")
    print(f"MATH Courses: {len(math_courses)}")
    
    level_301_courses = get_courses_by_number(301)
    print(f"301 level courses: {len(level_301_courses)}")
    
    four_credit_courses = get_courses_by_credits(4)
    print(f"4-credit courses: {len(four_credit_courses)}")
    
    # Test section reads
    print("\nSection Reads:")
    all_sections = get_all_sections()
    print(f"All sections count: {len(all_sections)}")
    
    section = get_section_by_id(101)
    print(f"Section 101: {section}")
    
    csci301_sections = get_sections_by_course_id("CSCI301")
    print(f"CSCI301 sections: {len(csci301_sections)}")
    
    fall_sections = get_sections_by_semester("Fall")
    print(f"Fall sections: {len(fall_sections)}")
    
    y2023_sections = get_sections_by_year(2023)
    print(f"2023 sections: {len(y2023_sections)}")
    
    fall_2023_sections = get_sections_by_semester_year("Fall", 2023)
    print(f"Fall 2023 sections: {len(fall_2023_sections)}")
    
    # Test registration reads
    print("\nRegistration Reads:")
    all_registrations = get_all_registrations()
    print(f"All registrations count: {len(all_registrations)}")
    
    registration = get_registration_by_id(101)
    print(f"Registration 101: {registration}")
    
    student_regs = get_registrations_by_student_id(1001)
    print(f"Student 1001 registrations: {len(student_regs)}")
    
    section_regs = get_registrations_by_section_id(101)
    print(f"Section 101 registrations: {len(section_regs)}")
    
    a_grades = get_registrations_by_grade(4.0)
    print(f"Registrations with 4.0 grade: {len(a_grades)}")

def test_update_operations():
    """Test update operations."""
    print("\n--- Testing Update Operations ---")
    
    # Update newly created student
    update_student(2001, "Mark Thompson", "820 Cedar Lane")
    print("Updated student 2001: changed name and address")
    
    # Update newly created course
    update_course("CS301", "Advanced Software Engineering", credits=5)
    print("Updated course CS301: changed name and credits")
    
    # Update newly created section
    update_section(101, "Spring", 2025)
    print("Updated section 101: changed semester and year")
    
    # Update newly created registration
    update_registration(101, 4.0)
    print("Updated registration 101: changed grade to 4.0")
   
def test_delete_operations():
    """Test delete operations."""
    print("\n--- Testing Delete Operations ---")
    
    # Delete only newly created registrations
    for i in range(101, 104):
        delete_registration(i)
    print("Deleted newly added registrations (101-103)")
    
    # Delete only newly created sections
    for i in range(101, 104):
        delete_section(i)
    print("Deleted newly added sections (101-103)")
    
    # Delete only newly created courses
    courses = ["CSCI301", "ENG220", "PHYS201"]
    for course_id in courses:
        delete_course(course_id)
    print("Deleted newly added courses")
    
    # Delete only newly created students
    for i in range(2001, 2004):
        delete_student(i)
    print("Deleted newly added students (2001-2003)")    

def main():
    """Main test function."""

    # Add test data
    test_create_operations()
    
    # Test read operations
    test_read_operations()
    
    # Test update operations
    test_update_operations()
    
    # Test reads after updates
    #print("\n--- Testing Read Operations After Updates ---")
    test_read_operations()
    
    # Test delete operations
    test_delete_operations()
    
    # Test reads after deletion
    #print("\n--- Testing Read Operations After Deletion ---")
    test_read_operations()
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    main()
