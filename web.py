from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, db
import time
from jamaibase import JamAI, protocol as p

# Initialize Flask app
app = Flask(__name__)

# Firebase setup
cred = credentials.Certificate("serviceAccountKey.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': ''
    })

# JamAI API Configuration
PROJECT_ID = ""
PAT = ""

# Initialize JamAI
jamai = JamAI(project_id=PROJECT_ID, token=PAT)

# Global chat session ID
chat_id = None

# Create a new chat session
def create_new_chat():
    timestamp = int(time.time())
    new_table_id = f"Chat_{timestamp}"
    try:
        jamai.table.duplicate_table(
            table_type=p.TableType.chat,
            table_id_src="chatbot_student2",
            table_id_dst=new_table_id,
            include_data=True,
            create_as_child=True
        )
        return new_table_id
    except Exception as e:
        print(f"Error creating new chat: {str(e)}")
        return None

def format_as_numbered_list(items):
    return "\n".join([f"{i + 1}. {item}" for i, item in enumerate(items)])

# Interact with chatbot and fetch response
def chat_interaction(table_id, user_message):

    try:
        # Predefined responses
        if user_message.lower() in ['hi', 'hello', 'hey']:
            return "Hello! How can I assist you today?"
        elif user_message.lower() in ['bye', 'goodbye']:
            return "Goodbye! Have a great day!"
        elif user_message.lower() in ['thanks', 'thank you']:
            return "You're welcome! Let me know if there's anything else I can help with."


        response = jamai.table.add_table_rows(
            table_type=p.TableType.chat,
            request=p.RowAddRequest(
                table_id=table_id,
                data=[{"User": user_message}],
                stream=True  # For streaming responses
            )
        )
        # Collect streamed response
        full_response = ""
        for chunk in response:
            if isinstance(chunk, p.GenTableStreamChatCompletionChunk) and chunk.output_column_name == 'AI':
                # Example for structured list formatting
                if isinstance(chunk.choices[0].message.content, list):  # If the response is a list of items
                    title = "Here is the information you requested:"
                    items = chunk.choices[0].message.content  # Assume this is a list of strings
                    formatted_list = f"{title}<br>" + "<br>".join(f"{i + 1}. {item}" for i, item in enumerate(items))
                    full_response += formatted_list
                else:
                    full_response += chunk.choices[0].message.content.replace('\n', '<br>')

        # Check if the bot response is empty
        if not full_response.strip():
            return "I'm sorry, I didn't quite understand that. Can you rephrase?"

        return full_response
    except Exception as e:
        print(f"Error during chat interaction: {str(e)}")
        return "I'm sorry, something went wrong. Please try again later."

# Flask route for chatbot API
@app.route('/chatbot', methods=['GET','POST'])
def chatbot():
    if request.method == 'GET':
        # Render the chatbot HTML page
        return render_template('chatbot.html')

    if request.method == 'POST':
        # Handle chatbot interactions
        global chat_id
        if not chat_id:
            chat_id = create_new_chat()

    if not chat_id:
        return jsonify({'response': "Unable to start a new chat session. Please try again later."}), 500

    user_message = request.json.get('message', '').strip()
    if not user_message:
        return jsonify({'response': "Please enter a message."}), 400

    bot_response = chat_interaction(chat_id, user_message)
    return jsonify({'response': bot_response}), 200

# Dashboard route
@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/attendance_overview', methods=['GET'])
def attendance_overview():
    try:
        ref = db.reference('Students')
        data = ref.get()

        if not data:
            return jsonify({
                'total_records': 0,
                'total_attendance': 0,
                'attendance_count': 0,
                'absent_count': 0,
                'attendance_percentage': 0
            }), 200

        # Total number of student records
        total_records = len(data)

        # Total attendance across all students
        total_attendance = sum(student.get('total_attendance', 0) for student in data.values())

        # Count of students who have at least one attendance record
        attendance_count = sum(1 for student in data.values() if student.get('total_attendance', 0) > 0)

        # Count of students with zero attendance
        absent_count = total_records - attendance_count

        # Attendance percentage
        attendance_percentage = (attendance_count / total_records) * 100 if total_records > 0 else 0

        result = {
            'total_records': total_records,
            'total_attendance': total_attendance,
            'attendance_count': attendance_count,
            'absent_count': absent_count,
            'attendance_percentage': round(attendance_percentage, 2)
        }
        return jsonify(result), 200
    except Exception as e:
        print(f"Error in attendance overview: {e}")
        return jsonify({'error': str(e)}), 500


# Attendance trends API
@app.route('/api/attendance_trends', methods=['GET'])
def attendance_trends():
    try:
        ref = db.reference('Students')
        students = ref.get()
        trends = {}
        for student in students.values():
            for record in student.get('attendance_history', []):
                date = record['date']
                trends[date] = trends.get(date, 0) + 1
        sorted_trends = dict(sorted(trends.items()))
        return jsonify({'dates': list(sorted_trends.keys()), 'attendance_counts': list(sorted_trends.values())}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Student details API
@app.route('/api/student_details', methods=['GET'])
def student_details():
    try:
        ref = db.reference('Students')
        students = ref.get()
        return jsonify(students or {}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Attendance history API for specific student
@app.route('/api/attendance_history/<student_id>', methods=['GET'])
def attendance_history(student_id):
    try:
        ref = db.reference(f'Students/{student_id}/attendance_history')
        history = ref.get()
        return jsonify(history or []), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Course-wise attendance API
@app.route('/api/course_attendance', methods=['GET'])
def course_attendance():
    try:
        courses_ref = db.reference('Courses')
        courses = courses_ref.get()
        course_attendance = {
            course_id: {
                "name": course_data['course_name'],
                "attendance_count": len(course_data.get('students', []))
            }
            for course_id, course_data in courses.items()
        }
        return jsonify(course_attendance), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Visualization route
@app.route('/visualize')
def visualize():
    ref = db.reference('Students')
    students_data = ref.get() or {}
    return render_template('visualize.html', students=students_data)

if __name__ == '__main__':
    app.run(debug=True)
