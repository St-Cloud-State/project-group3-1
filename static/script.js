
// Function to add a student
function addStudent() {
    const studentID = document.getElementById('studentID').value;
    const name = document.getElementById('studentName').value;
    const address = document.getElementById('studentAddress').value;

    // Create a JSON object with student data
    const studentData = {
        student_id: studentID,
        name: name,
        address: address
    };

    // Send the student data to the server via POST request
    fetch('/api/add_student', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(studentData)
    })
        .then(response => response.json())
        .then(data => {
            // Display a success message or handle errors if needed
            console.log(data.message);

            // Refresh the students
            showAllStudents();
            
        })
        .catch(error => {
            console.error('Error adding student:', error);
        });
}


// Function to display all students
function showAllStudents() {
    fetch('/api/students')
    .then(response => response.json())
    .then(data => {
        const studentList = document.getElementById('studentList');
        studentList.innerHTML = '';

        data.forEach(student => {
            const studentElement = document.createElement('div');
            studentElement.innerHTML = `
                <h3>${student[1]}</h3>
                <p>ID: ${student[0]}</p>
                <p>Address: ${student[2] || ''}</p>
            `;
            studentList.appendChild(studentElement);
        });
    })
    .catch(error => {
        console.error('Error fetching students', error);
    });
}


// Function to add a course 
function addCourse() {
    const courseId = document.getElementById('courseId').value;
    const courseName = document.getElementById('courseName').value;
    const rubric = document.getElementById('rubric').value;
    const courseNumber = document.getElementById('courseNumber').value;
    const credits = document.getElementById('credits').value;

    // Create a JSON object with course data
    const courseData = {
        course_id: courseId,
        course_name: courseName,
        rubric: rubric,
        course_number: Number(courseNumber),
        credits: Number(credits)
    };

    // Send the course data to the server via POST request
    fetch('/api/add_course', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(courseData)
    })
        .then(response => response.json())
        .then(data => {
            // Display a success message or handle errors if needed
            console.log(data.message);

            // Refresh the courses
            showAllCourses();
            
        })
    .catch(error => {
        console.error('Error adding course:', error);
    });
}


// Function to display all courses
function showAllCourses() {
    fetch('/api/courses')
    .then(response => response.json())
    .then(data => {
        const courseList = document.getElementById('courseList');
        courseList.innerHTML = '';

        data.forEach(course => {
            const courseElement = document.createElement('div');
            courseElement.innerHTML = `
                <h3>${course[1]}</h3>
                <p>ID: ${course[0]}</p>
                <p>Rubric: ${course[2] || ''}</p>
                <p>Number: ${course[3] || ''}</p>
                <p>Credits: ${course[4] || ''}</p>
            `;
            courseList.appendChild(courseElement);
        });
    })
    .catch(error => {
        console.error('Error fetching courses:', error);
    });
}



// Function to display all courses by rubric
function showCoursesByRubric() {
    const rubric = document.getElementById('rubricFilter').value;
    
    fetch(`/api/courses/${rubric}`)
    .then(response => response.json())
    .then(data => {
        const coursesByRubric = document.getElementById('coursesByRubric');
        coursesByRubric.innerHTML = '';
        
        data.forEach(course => {
            const courseElement = document.createElement('div');
            courseElement.innerHTML = `
                <h3>${course[1]}</h3>
                <p>ID: ${course[0]}</p>
                <p>Rubric: ${course[2] || ''}</p>
                <p>Number: ${course[3] || ''}</p>
                <p>Credits: ${course[4] || ''}</p>
            `;
            coursesByRubric.appendChild(courseElement);
        });
    })
    .catch(error => {
        console.error('Error fetching courses by rubric:', error);
    });
}


// Function to add a section
function addSection() {
    const sectionId = document.getElementById('sectionId').value;
    const courseId = document.getElementById('sectionCourseId').value;
    const semester = document.getElementById('semester').value;
    const year = document.getElementById('year').value;

    // Create a JSON object with section data
    const sectionData = {
        section_id: Number(sectionId),
        course_id: courseId,
        semester: semester,
        year: Number(year)
    };

    // Send the section data to the server
    fetch('/api/add_section', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(sectionData)
    })
    .then(response => response.json())
    .then(data => {
        // Display a success message or handle errors if needed
        console.log(data.message);
        
        // Refresh section list
        showAllSections();
    })
    .catch(error => {
        console.error('Error adding section:', error);
    });
}


// Function to display all sections
function showAllSections() {
    fetch('/api/sections')
    .then(response => response.json())
    .then(data => {
        const sectionList = document.getElementById('sectionList');
        sectionList.innerHTML = '';
        
        data.forEach(section => {
            const sectionElement = document.createElement('div');
            sectionElement.innerHTML = `
                <h3>Section ${section[0]}</h3>
                <p>Course ID: ${section[1]}</p>
                <p>Semester: ${section[2] || ''}</p>
                <p>Year: ${section[3] || ''}</p>
            `;
            sectionList.appendChild(sectionElement);
        });
    })
    .catch(error => {
        console.error('Error fetching sections:', error);
    });
}


// Function to dispaly sections by course
function showSectionsByCourse() {
    const courseId = document.getElementById('courseIdFilter').value;
    
    fetch(`/api/sections/${courseId}`)
    .then(response => response.json())
    .then(data => {
        const sectionsByCourse = document.getElementById('sectionsByCourse');
        sectionsByCourse.innerHTML = '';
        
        data.forEach(section => {
            const sectionElement = document.createElement('div');
            sectionElement.innerHTML = `
                <h3>Section ${section[0]}</h3>
                <p>Course ID: ${section[1]}</p>
                <p>Semester: ${section[2] || ''}</p>
                <p>Year: ${section[3] || ''}</p>
            `;
            sectionsByCourse.appendChild(sectionElement);
        });
    })
    .catch(error => {
        console.error('Error fetching sections by course:', error);
    });
}