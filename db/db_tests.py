import sqlite3
#import os
from db_operations import *
from db_queries import *

def test_create_operations():
    """Populate database with test data - 10 records in each table."""
    # Add 10 students
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
    
    for student in student_data:
        create_student(student[0], student[1], student[2])
    print("Added 10 students")
    
    # Add 10 courses
    course_data = [
        ("CS101", "Introduction to Programming", "CS", 101, 3),
        ("CS201", "Data Structures", "CS", 201, 4),
        ("MATH150", "Calculus I", "MATH", 150, 4),
        ("MATH250", "Linear Algebra", "MATH", 250, 3),
        ("ENG120", "College Writing", "ENG", 120, 3),
        ("PHYS101", "Physics I", "PHYS", 101, 4),
        ("CHEM110", "Chemistry I", "CHEM", 110, 4),
        ("HIST105", "World History", "HIST", 105, 3),
        ("BIO120", "Biology I", "BIO", 120, 4),
        ("PSY101", "Introduction to Psychology", "PSY", 101, 3)
    ]
    
    for course in course_data:
        create_course(course[0], course[1], course[2], course[3], course[4])
    print("Added 10 courses")
    
    # Add 10 sections
    section_data = [
        (1, "CS101", "Fall", 2023),
        (2, "CS201", "Spring", 2024),
        (3, "MATH150", "Fall", 2023),
        (4, "MATH250", "Spring", 2024),
        (5, "ENG120", "Fall", 2023),
        (6, "PHYS101", "Fall", 2023),
        (7, "CHEM110", "Spring", 2024),
        (8, "HIST105", "Spring", 2024),
        (9, "BIO120", "Fall", 2023),
        (10, "PSY101", "Spring", 2024)
    ]
    
    for section in section_data:
        create_section(section[0], section[1], section[2], section[3])
    print("Added 10 sections")
    
    # Add 10 registrations
    registration_data = [
        (1, 1001, 1, 3.7),
        (2, 1002, 2, 3.5),
        (3, 1003, 3, 4.0),
        (4, 1004, 4, 3.8),
        (5, 1005, 5, 3.3),
        (6, 1006, 6, 3.6),
        (7, 1007, 7, 3.9),
        (8, 1008, 8, 3.4),
        (9, 1009, 9, 3.7),
        (10, 1010, 10, 3.5)
    ]
    
    for reg in registration_data:
        create_registration(reg[0], reg[1], reg[2], reg[3])
    print("Added 10 registrations")

def test_read_operations():
    """Test all read operations."""
    print("\n--- Testing Read Operations ---")
    
    # Test student reads
    print("\nStudent Reads:")
    all_students = get_all_students()
    print(f"All students count: {len(all_students)}")
    
    student = get_student_by_id(1001)
    print(f"Student 1001: {student}")
    
    students_by_name = get_students_by_name("Smith")
    print(f"Students with 'Smith' in name: {len(students_by_name)}")
    
    # Test course reads
    print("\nCourse Reads:")
    all_courses = get_all_courses()
    print(f"All courses count: {len(all_courses)}")
    
    course = get_course_by_id("CS101")
    print(f"Course CS101: {course}")
    
    cs_courses = get_courses_by_rubric("CS")
    print(f"CS Courses: {len(cs_courses)}")
    
    math_courses = get_courses_by_rubric("MATH")
    print(f"MATH Courses: {len(math_courses)}")
    
    level_101_courses = get_courses_by_number(101)
    print(f"101 level courses: {len(level_101_courses)}")
    
    four_credit_courses = get_courses_by_credits(4)
    print(f"4-credit courses: {len(four_credit_courses)}")
    
    # Test section reads
    print("\nSection Reads:")
    all_sections = get_all_sections()
    print(f"All sections count: {len(all_sections)}")
    
    section = get_section_by_id(1)
    print(f"Section 1: {section}")
    
    cs101_sections = get_sections_by_course_id("CS101")
    print(f"CS101 sections: {len(cs101_sections)}")
    
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
    
    registration = get_registration_by_id(1)
    print(f"Registration 1: {registration}")
    
    student_regs = get_registrations_by_student_id(1001)
    print(f"Student 1001 registrations: {len(student_regs)}")
    
    section_regs = get_registrations_by_section_id(1)
    print(f"Section 1 registrations: {len(section_regs)}")
    
    a_grades = get_registrations_by_grade(4.0)
    print(f"Registrations with 4.0 grade: {len(a_grades)}")

def test_update_operations():
    """Test update operations."""
    print("\n--- Testing Update Operations ---")
    
    # Update students
    update_student(1001, "Alice Johnson", "999 New Address")
    update_student(1005, address="205 Updated Drive")
    print("Updated students 1001 and 1005")
    
    # Update courses
    update_course("CS101", "Intro to Computer Science", credits=4)
    update_course("MATH150", course_name="Calculus 1")
    print("Updated courses CS101 and MATH150")
    
    # Update sections
    update_section(1, "Spring", 2024)
    update_section(6, year=2024)
    print("Updated sections 1 and 6")
    
    # Update registrations
    update_registration(1, 4.0)
    update_registration(5, 3.7)
    print("Updated registrations 1 and 5")

def test_delete_operations():
    """Test delete operations."""
    print("\n--- Testing Delete Operations ---")
    
    # Delete all registrations first
    for i in range(1, 11):
        delete_registration(i)
    print("Deleted all registrations")
    
    # Delete all sections
    for i in range(1, 11):
        delete_section(i)
    print("Deleted all sections")
    
    # Delete all courses
    courses = ["CS101", "CS201", "MATH150", "MATH250", "ENG120", 
               "PHYS101", "CHEM110", "HIST105", "BIO120", "PSY101"]
    for course_id in courses:
        delete_course(course_id)
    print("Deleted all courses")
    
    # Delete all students
    for i in range(1001, 1011):
        delete_student(i)
    print("Deleted all students")

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
