document.addEventListener('DOMContentLoaded', () => {
    console.log("Welcome to the University Registration System");
});

document.addEventListener('DOMContentLoaded', () => {
    fetch(window.location.origin + '/api/students')
        .then(response => response.json())
        .then(data => {
            const studentsList = document.getElementById('students-list');
            if (data.error) {
                studentsList.innerHTML = `<p>Error: ${data.error}</p>`;
                return;
            }
            let html = '<ul>';
            data.forEach(student => {
                html += `<li>${student.name} (ID: ${student.student_id})</li>`;
            });
            html += '</ul>';
            studentsList.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching students:', error);
        });
});

document.addEventListener('DOMContentLoaded', () => {
    fetch(window.location.origin + '/api/courses')
        .then(response => response.json())
        .then(data => {
            const coursesList = document.getElementById('courses-list');
            if (data.error) {
                coursesList.innerHTML = `<p>Error: ${data.error}</p>`;
                return;
            }
            let html = '<ul>';
            data.forEach(course => {
                html += `<li>${course.course_name} (ID: ${course.course_id})</li>`;
            });
            html += '</ul>';
            coursesList.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching courses:', error);
        });
});

document.addEventListener('DOMContentLoaded', () => {
    fetch(window.location.origin + '/api/sections')
        .then(response => response.json())
        .then(data => {
            const sectionsList = document.getElementById('sections-list');
            if (data.error) {
                sectionsList.innerHTML = `<p>Error: ${data.error}</p>`;
                return;
            }
            let html = '<ul>';
            data.forEach(section => {
                html += `<li>Section ID: ${section.section_id}, Course ID: ${section.course_id}, Semester: ${section.semester}, Year: ${section.year}</li>`;
            });
            html += '</ul>';
            sectionsList.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching sections:', error);
        });
});

document.addEventListener('DOMContentLoaded', () => {
    fetch(window.location.origin + '/api/registrations')
        .then(response => response.json())
        .then(data => {
            const registrationList = document.getElementById('registration-list');
            if (data.error) {
                registrationList.innerHTML = `<p>Error: ${data.error}</p>`;
                return;
            }
            let html = '<ul>';
            data.forEach(registration => {
                html += `<li>Student ID: ${registration.student_id}, Section ID: ${registration.section_id}, Grade: ${registration.grade}</li>`;
            });
            html += '</ul>';
            registrationList.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching registrations:', error);
        });
});
