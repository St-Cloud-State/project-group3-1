// Updated Frontend Script

document.addEventListener('DOMContentLoaded', () => {
    console.log("Welcome to the University Registration System");

    // Fetch and display all students
    fetch('/api/students')
        .then(response => response.json())
        .then(data => {
            const studentsList = document.getElementById('allstudents');
            if (data.error) {
                studentsList.innerHTML = `<p>Error: ${data.error}</p>`;
                return;
            }
            let html = '<ul>';
            data.forEach(student => {
                html += `<li>
                    ${student[1]} (ID: ${student[0]}, Address: ${student[2] || 'N/A'})
                    <button onclick="deleteStudent(${student[0]})" class="btn btn-primary">Delete</button>
                </li>`;
            });
            html += '</ul>';
            studentsList.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching students:', error);
        });

    // Fetch and display all courses
    fetch('/api/courses')
        .then(response => response.json())
        .then(data => {
            const coursesList = document.getElementById('allcourses');
            if (!coursesList) return;

            if (data.error) {
                coursesList.innerHTML = `<p>Error: ${data.error}</p>`;
                return;
            }
            let html = '<ul>';
            data.forEach(course => {
                html += `<li>
                    ${course[1]} (ID: ${course[0]}, Rubric: ${course[2]}, Number: ${course[3]}, Credits: ${course[4]})
                    <button onclick="deleteCourse('${course[0]}')" class="btn btn-primary">Delete</button>
                </li>`;
            });
            html += '</ul>';
            coursesList.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching courses:', error);
        });

    fetch('/api/sections')
        .then(response => response.json())
        .then(data => {
            const sectionList = document.getElementById('allsections');
            if (!sectionList) return;

            if (data.error) {
                sectionList.innerHTML = `<p>Error: ${data.error}</p>`;
                return;
            }
            let html = '<ul>';
            data.forEach(section => {
                html += `<li>
                    Section ${section[0]} - Course: ${section[1]}, ${section[2]} ${section[3]}
                    <button onclick="deleteSection(${section[0]})" class="btn btn-primary">Delete</button>
                </li>`;
            });
            html += '</ul>';
            sectionList.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching sections:', error);
        });
});

// Function to add a new student
function addStudent() {
    const name = document.getElementById('studentName').value;
    const student_id = document.getElementById('studentID').value;
    const address = document.getElementById('studentAddress').value;
    
    if (!name || !student_id) {
        alert('Please fill in all required fields');
        return;
    }

    fetch('/api/add_student', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            student_id, 
            name,
            address
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || data.error);
        location.reload();
    })
    .catch(error => {
        console.error('Error adding student:', error);
    });
}

// Function to add a new student
function addStudent() {
    const name = document.getElementById('studentName').value;
    const student_id = document.getElementById('studentID').value;
    const address = document.getElementById('studentAddress').value;
    
    if (!name || !student_id) {
        alert('Please fill in all required fields');
        return;
    }

    fetch('/api/add_student', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            student_id, 
            name,
            address
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || data.error);
        location.reload();
    })
    .catch(error => {
        console.error('Error adding student:', error);
    });
}

// Function to delete a student
function deleteStudent(studentId) {
    if (confirm("Are you sure you want to delete this student?")) {
        fetch(`/api/delete_student/${studentId}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message || data.error);
            location.reload();
        })
        .catch(error => {
            console.error('Error deleting student:', error);
            alert('Failed to delete student');
        });
    }
}

// Function to add a new course
function addCourse() {
    const course_name = document.getElementById('courseName').value;
    const course_id = document.getElementById('courseID').value;
    const rubric = document.getElementById('rubric').value;
    const course_number = parseInt(document.getElementById('courseNumber').value);
    const credits = parseInt(document.getElementById('credits').value);

    if (!course_name || !course_id || !rubric || isNaN(course_number) || isNaN(credits)) {
        alert('Please fill in all required fields');
        return;
    }

    fetch('/api/add_course', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            course_id, 
            course_name,
            rubric,
            course_number,
            credits
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || data.error);
        location.reload();
    })
    .catch(error => {
        console.error('Error adding course:', error);
    });
}

// Function to delete a course
function deleteCourse(courseId) {
    if (confirm("Are you sure you want to delete this course?")) {
        fetch(`/api/delete_course/${courseId}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message || data.error);
            location.reload();
        })
        .catch(error => {
            console.error('Error deleting course:', error);
            alert('Failed to delete course');
        });
    }
}

// Function to add a new section
function addSection() {
    const section_id = document.getElementById('sectionID').value;
    const course_id = document.getElementById('courseID').value;
    const semester = document.getElementById('semester').value;
    const year = document.getElementById('year').value;
    
    if (!section_id || !course_id) {
        alert('Please fill in all required fields');
        return;
    }

    fetch('/api/add_section', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            section_id, 
            course_id,
            semester: semester || "",
            year: year || 0
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || data.error);
        location.reload();
    })
    .catch(error => {
        console.error('Error adding section:', error);
    });
}

// Function to delete a section
function deleteSection(sectionId) {
    if (confirm("Are you sure you want to delete this section?")) {
        fetch(`/api/delete_section/${sectionId}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message || data.error);
            location.reload();
        })
        .catch(error => {
            console.error('Error deleting section:', error);
            alert('Failed to delete section');
        });
    }
}
