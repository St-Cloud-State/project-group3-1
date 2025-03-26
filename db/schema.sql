-- Drop tables if they exist (in reverse order of creation to respect foreign key constraints)
-- DROP TABLE IF EXISTS Registration;
-- DROP TABLE IF EXISTS Section;
-- DROP TABLE IF EXISTS Course;
-- DROP TABLE IF EXISTS Student;

-- Create Student table
CREATE TABLE Student (
    StudentID INTEGER PRIMARY KEY,
    Name VARCHAR NOT NULL,
    Address VARCHAR
);

-- Create Course table
CREATE TABLE Course (
    CourseID VARCHAR PRIMARY KEY,
    CourseName VARCHAR NOT NULL,
    Rubric VARCHAR,
    CourseNumber INTEGER,
    Credits INTEGER
);

-- Create Section table
CREATE TABLE Section (
    SectionID INTEGER PRIMARY KEY,
    CourseID VARCHAR NOT NULL,
    Semester VARCHAR,
    Year INTEGER,
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);

-- Create Registration table (junction table)
CREATE TABLE Registration (
    RegistrationID INTEGER PRIMARY KEY,
    StudentID INTEGER NOT NULL,
    SectionID INTEGER NOT NULL,
    Grade DECIMAL,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (SectionID) REFERENCES Section(SectionID)
);