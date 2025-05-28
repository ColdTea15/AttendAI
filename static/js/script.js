// Merged JavaScript Code
$(document).ready(function () {
    // Fetch and display attendance overview
    $.getJSON("/api/attendance_overview", function (data) {
        $("#total-records").text(data.total_records || 0);
        $("#total-attendance").text(data.total_attendance || 0);
        $("#attendance-count").text(data.attendance_count || 0);
        $("#absent-count").text(data.absent_count || 0);
        $("#attendance-percentage").text((data.attendance_percentage || 0).toFixed(2) + "%");
    }).fail(function () {
        console.error("Failed to fetch attendance overview data.");
        $("#total-records").text("Error");
        $("#total-attendance").text("Error");
        $("#attendance-count").text("Error");
        $("#absent-count").text("Error");
        $("#attendance-percentage").text("Error");
    });

    // Fetch and display student details
    $.getJSON("/api/student_details", function (data) {
        let html = '';
        $.each(data, function (key, student) {
            html += `<tr>
                        <td>${key}</td>
                        <td>${student.name || 'N/A'}</td>
                        <td>${student.major || 'N/A'}</td>
                        <td>${student.total_attendance || 0}</td>
                        <td>${(student.enrolled_courses || []).join(', ') || 'N/A'}</td>
                        <td>
                            <button class="btn btn-info btn-sm" onclick="showHistory('${key}')">View History</button>
                        </td>
                    </tr>`;
        });
        $("#student-details").html(html);

        createStudentCharts(data);
    });

    // Fetch and display course-wise attendance
    $.getJSON("/api/course_attendance", function (data) {
        const ctxCourse = document.getElementById('courseAttendanceChart').getContext('2d');
        const chartData = {
            labels: Object.values(data).map(course => course.name),
            datasets: [{
                label: 'Attendance Count',
                data: Object.values(data).map(course => course.attendance_count),
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        };
        new Chart(ctxCourse, {
            type: 'bar',
            data: chartData,
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    });

    // Fetch and display attendance trends
    $.getJSON("/api/attendance_trends", function (trendData) {
        const ctxTrends = document.getElementById('attendanceTrendsChart').getContext('2d');
        new Chart(ctxTrends, {
            type: 'line',
            data: {
                labels: trendData.dates,
                datasets: [{
                    label: 'Daily Attendance',
                    data: trendData.attendance_counts,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    });

    // Search and filter student details
    $("#search-bar").on("input", function () {
        const value = $(this).val().toLowerCase();
        $("#student-details tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().includes(value));
        });
    });

    // Show attendance history for a student
    window.showHistory = function (studentId) {
        $.getJSON(`/api/attendance_history/${studentId}`, function (data) {
            let html = '';
            data.forEach(record => {
                html += `<tr>
                            <td>${record.date || 'N/A'}</td>
                            <td>${record.time || 'N/A'}</td>
                            <td>${record.subject || 'N/A'}</td>
                            <td>${record.status || 'N/A'}</td>
                        </tr>`;
            });
            $("#attendance-history").html(html);
            $("#attendanceHistoryModal").modal('show');
        });
    };

    // Unified sendMessage function
    async function sendMessage() {
        const userMessage = document.getElementById('userMessage').value;
        if (!userMessage) return;

        // Display the user's message
        const messagesDiv = document.getElementById('messages');
        const userMsg = document.createElement('div');
        userMsg.className = 'message user-msg';
        userMsg.innerHTML = `
            <div class="text user">${userMessage}</div>
            <img src="/static/user.png" alt="User">
        `;
        messagesDiv.appendChild(userMsg);

        // Scroll to the bottom
        messagesDiv.scrollTop = messagesDiv.scrollHeight;

        // Clear input field
        document.getElementById('userMessage').value = '';

        try {
            const response = await fetch('/chatbot', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userMessage }),
            });

            const data = await response.json();
            const botMsg = document.createElement('div');
            botMsg.className = 'message bot-msg';

            if (data.response) {
                if (data.response.includes('<br>')) {
                    const listItems = data.response.split('<br>').filter(item => item.trim() !== "");
                    const ul = document.createElement('ul');
                    listItems.forEach(item => {
                        const li = document.createElement('li');
                        li.textContent = item.trim();
                        ul.appendChild(li);
                    });
                    botMsg.innerHTML = `
                        <img src="/static/bot.png" alt="Bot">
                        <div class="text bot"></div>
                    `;
                    botMsg.querySelector('.text.bot').appendChild(ul);
                } else {
                    botMsg.innerHTML = `
                        <img src="/static/bot.png" alt="Bot">
                        <div class="text bot">${data.response}</div>
                    `;
                }
            } else {
                botMsg.innerHTML = `
                    <img src="/static/bot.png" alt="Bot">
                    <div class="text bot">Bot: I'm sorry, something went wrong.</div>
                `;
            }
            messagesDiv.appendChild(botMsg);

            // Scroll to the bottom
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        } catch (error) {
            console.error('Error:', error);
            const errorMsg = document.createElement('div');
            errorMsg.className = 'message bot-msg';
            errorMsg.innerHTML = `
                <img src="/static/bot.png" alt="Bot">
                <div class="text bot">Bot: I'm sorry, there was an error connecting to the server.</div>
            `;
            messagesDiv.appendChild(errorMsg);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }
    }
});

// Helper function to create charts for student data
function createStudentCharts(data) {
    // Code for creating Total Attendance and Year-wise charts
}
// Helper function to create charts for student data
function createStudentCharts(data) {
    // Create Total Attendance by Student Chart
    const studentNames = Object.values(data).map(student => student.name || 'N/A');
    const totalAttendance = Object.values(data).map(student => student.total_attendance || 0);
    const attendanceCtx = document.getElementById('attendanceChart').getContext('2d');
    new Chart(attendanceCtx, {
        type: 'bar',
        data: {
            labels: studentNames,
            datasets: [{
                label: 'Total Attendance',
                data: totalAttendance,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: true },
                title: { display: true, text: 'Attendance by Student' }
            },
            scales: {
                y: { beginAtZero: true }
            }
        }
    });

    // Create Year-Wise Attendance Chart
    const years = [...new Set(Object.values(data).map(student => student.year || 'N/A'))];
    const yearAttendance = years.map(year => {
        return Object.values(data)
            .filter(student => student.year === year)
            .reduce((sum, student) => sum + (student.total_attendance || 0), 0);
    });
    const yearCtx = document.getElementById('yearChart').getContext('2d');
    new Chart(yearCtx, {
        type: 'pie',
        data: {
            labels: years.map(year => `Year ${year}`),
            datasets: [{
                label: 'Attendance by Year',
                data: yearAttendance,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: true },
                title: { display: true, text: 'Attendance by Year' }
            }
        }
    });
}

// Unified event handlers and functionalities
$(document).ready(function () {
    // Fetch and display attendance overview
    $.getJSON("/api/attendance_overview", function (data) {
        $("#total-records").text(data.total_records || 0);
        $("#attendance-count").text(data.attendance_count || 0);
        $("#absent-count").text(data.absent_count || 0);
        $("#attendance-percentage").text((data.attendance_percentage || 0).toFixed(2) + "%");
    });

    // Fetch and display student details with charts
    $.getJSON("/api/student_details", function (data) {
        let html = '';
        $.each(data, function (key, student) {
            html += `<tr>
                        <td>${key}</td>
                        <td>${student.name || 'N/A'}</td>
                        <td>${student.major || 'N/A'}</td>
                        <td>${student.total_attendance || 0}</td>
                        <td>${(student.enrolled_courses || []).join(', ') || 'N/A'}</td>
                        <td>
                            <button class="btn btn-info btn-sm" onclick="showHistory('${key}')">View History</button>
                        </td>
                    </tr>`;
        });
        $("#student-details").html(html);

        // Create attendance charts
        createStudentCharts(data);
    });

    // Fetch and display course attendance
    $.getJSON("/api/course_attendance", function (data) {
        const ctxCourse = document.getElementById('courseAttendanceChart').getContext('2d');
        new Chart(ctxCourse, {
            type: 'bar',
            data: {
                labels: Object.values(data).map(course => course.name),
                datasets: [{
                    label: 'Attendance Count',
                    data: Object.values(data).map(course => course.attendance_count),
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    });

    // Fetch and display attendance trends
    $.getJSON("/api/attendance_trends", function (trendData) {
        const ctxTrends = document.getElementById('attendanceTrendsChart').getContext('2d');
        new Chart(ctxTrends, {
            type: 'line',
            data: {
                labels: trendData.dates,
                datasets: [{
                    label: 'Daily Attendance',
                    data: trendData.attendance_counts,
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    });

    // Unified search filter for student details
    $("#search-bar").on("input", function () {
        const value = $(this).val().toLowerCase();
        $("#student-details tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().includes(value));
        });
    });

    // Define and implement `sendMessage` for chatbot communication
    async function sendMessage() {
        const userMessage = document.getElementById('userMessage').value;
        if (!userMessage) return;

        const messagesDiv = document.getElementById('messages');
        const userMsg = document.createElement('div');
        userMsg.className = 'message user-msg';
        userMsg.innerHTML = `
            <div class="text user">${userMessage}</div>
            <img src="/static/user.png" alt="User">
        `;
        messagesDiv.appendChild(userMsg);

        // Scroll and clear input
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
        document.getElementById('userMessage').value = '';

        try {
            const response = await fetch('/chatbot', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userMessage }),
            });

            const data = await response.json();
            const botMsg = document.createElement('div');
            botMsg.className = 'message bot-msg';
            botMsg.innerHTML = `
                <img src="/static/bot.png" alt="Bot">
                <div class="text bot">${data.response || "I'm sorry, something went wrong."}</div>
            `;
            messagesDiv.appendChild(botMsg);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        } catch (error) {
            console.error('Error:', error);
            const errorMsg = document.createElement('div');
            errorMsg.className = 'message bot-msg';
            errorMsg.innerHTML = `
                <img src="/static/bot.png" alt="Bot">
                <div class="text bot">Bot: Error connecting to the server.</div>
            `;
            messagesDiv.appendChild(errorMsg);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }
    }
});
