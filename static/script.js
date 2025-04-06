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
                html += `<li>${student.name} (ID: ${student.student_id})</li>`;
            });
            html += '</ul>';
            studentsList.innerHTML = html;
        })
        .catch(error => {
            console.error('Error fetching students:', error);
        });
});

// Function to add a new student
function addStudent() {
    const name = document.getElementById('studentName').value;
    const student_id = document.getElementById('studentID').value;

    fetch('/api/add_student', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ student_id, name })
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
