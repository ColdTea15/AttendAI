import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import pandas as pd

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ''
})

# Reference to the Students node in Firebase
ref_students = db.reference('Students')
ref_courses = db.reference('Courses')

students_data = {
    "24001":
        {
            "name": "A",
            "major": "Software Engineering",
            "intake": 2021,
            "total_attendance": 16,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-10-01 13:00:00",
            "enrolled_courses": ["CSC3034", "NET2201", "CSC2014", "NET3204"],
            "attendance_history": [
                {"date": "2024-10-03", "time": "14:05:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-04", "time": "08:08:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-10", "time": "14:02:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-11", "time": "08:06:00", "subject": "NET3204", "status": "Present"},

                {"date": "2024-10-07", "time": "14:05:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-09", "time": "12:08:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-10", "time": "14:07:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-11", "time": "13:56:00", "subject": "NET2201", "status": "Present"},

                {"date": "2024-10-17", "time": "09:05:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-18", "time": "11:08:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-24", "time": "08:07:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-25", "time": "11:56:00", "subject": "CSC3034", "status": "Present"},

                {"date": "2024-10-08", "time": "11:55:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-09", "time": "17:28:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-15", "time": "11:48:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-16", "time": "17:36:00", "subject": "CSC2014", "status": "Present"},
            ]
        },
    "24002":
        {
            "name": "B",
            "major": "Computer Science",
            "intake": 2022,
            "total_attendance": 4,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-10-17 14:00:00",
            "enrolled_courses": ["NET3204"],
            "attendance_history": [
                {"date": "2024-10-03", "time": "14:05:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-04", "time": "08:08:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-10", "time": "14:02:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-11", "time": "08:06:00", "subject": "NET3204", "status": "Present"}
            ]
        },
    "24003":
        {
            "name": "C",
            "major": "Computer Science",
            "intake": 2023,
            "total_attendance": 12,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2024-10-01 15:00:00",
            "enrolled_courses": ["CSC3034", "NET2201", "CSC2014", "NET3204"],
            "attendance_history": [
                {"date": "2024-10-03", "time": "14:05:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-04", "time": "08:08:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-10", "time": "14:02:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-11", "time": "08:06:00", "subject": "NET3204", "status": "Present"},

                {"date": "2024-10-07", "time": "14:05:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-09", "time": "12:08:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-10", "time": "14:07:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-11", "time": "13:56:00", "subject": "NET2201", "status": "Present"},

                {"date": "2024-10-17", "time": "09:05:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-18", "time": "11:08:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-24", "time": "08:07:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-25", "time": "11:56:00", "subject": "CSC3034", "status": "Present"},

                {"date": "2024-10-08", "time": "11:55:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-09", "time": "17:28:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-15", "time": "11:48:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-23", "time": "17:36:00", "subject": "CSC2014", "status": "Present"},
            ]
        },
    "24004":
        {
            "name": "D",
            "major": "Computer Science",
            "intake": 2021,
            "total_attendance": 18,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2024-10-02 10:00:00",
            "enrolled_courses": ["CSC3034", "NET3204", "PSY2164", "MKT2224"],
            "attendance_history": [
                {"date": "2024-10-03", "time": "14:05:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-04", "time": "08:08:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-10", "time": "14:02:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-11", "time": "08:06:00", "subject": "NET3204", "status": "Present"},

                {"date": "2024-10-07", "time": "13:05:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-10", "time": "12:08:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-14", "time": "13:07:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-17", "time": "12:56:00", "subject": "MKT2224", "status": "Late"},

                {"date": "2024-10-17", "time": "09:05:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-18", "time": "11:08:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-24", "time": "08:07:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-25", "time": "11:56:00", "subject": "CSC3034", "status": "Present"},

                {"date": "2024-10-07", "time": "09:55:00", "subject": "PSY2164", "status": "Late"},
                {"date": "2024-10-10", "time": "17:28:00", "subject": "PSY2164", "status": "Present"},
                {"date": "2024-10-14", "time": "09:48:00", "subject": "PSY2164", "status": "Present"},
                {"date": "2024-10-17", "time": "17:36:00", "subject": "PSY2164", "status": "Present"},
                {"date": "2024-11-04", "time": "09:55:00", "subject": "PSY2164", "status": "Late"},
                {"date": "2024-11-07", "time": "17:28:00", "subject": "PSY2164", "status": "Present"},
            ]
        },
    "24005":
        {
            "name": "E",
            "major": "Computer Science",
            "intake": 2022,
            "total_attendance": 17,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-10-03 10:00:00",
            "enrolled_courses": ["CSC3034", "NET3204", "PSY2164", "MKT2224"],
            "attendance_history": [
                {"date": "2024-10-03", "time": "14:05:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-04", "time": "08:08:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-10", "time": "14:02:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-11", "time": "08:06:00", "subject": "NET3204", "status": "Present"},

                {"date": "2024-10-07", "time": "13:05:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-10", "time": "12:08:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-14", "time": "13:07:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-17", "time": "12:56:00", "subject": "MKT2224", "status": "Late"},

                {"date": "2024-10-17", "time": "09:05:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-18", "time": "11:08:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-24", "time": "08:07:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-25", "time": "11:56:00", "subject": "CSC3034", "status": "Present"},

                {"date": "2024-10-10", "time": "17:28:00", "subject": "PSY2164", "status": "Present"},
                {"date": "2024-10-14", "time": "09:48:00", "subject": "PSY2164", "status": "Present"},
                {"date": "2024-10-17", "time": "17:36:00", "subject": "PSY2164", "status": "Present"},
                {"date": "2024-11-04", "time": "09:55:00", "subject": "PSY2164", "status": "Late"},
                {"date": "2024-11-07", "time": "17:28:00", "subject": "PSY2164", "status": "Present"},
            ]
        },
    "24006":
        {
            "name": "F",
            "major": "Computer Science",
            "intake": 2022,
            "total_attendance": 10,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-10-02 10:00:00",
            "enrolled_courses": ["NET3204", "MKT2224"],
            "attendance_history": [
                {"date": "2024-10-03", "time": "14:05:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-04", "time": "08:08:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-10", "time": "14:02:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-11", "time": "08:06:00", "subject": "NET3204", "status": "Present"},

                {"date": "2024-10-07", "time": "13:05:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-10", "time": "12:08:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-14", "time": "13:07:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-17", "time": "12:56:00", "subject": "MKT2224", "status": "Late"},
                {"date": "2024-11-04", "time": "13:05:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-11-07", "time": "12:08:00", "subject": "MKT2224", "status": "Present"},
            ]

        },
    "24007":
        {
            "name": "G",
            "major": "Computer Science",
            "intake": 2023,
            "total_attendance": 16,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-11-20 10:00:00",
            "enrolled_courses": ["CSC3034", "NET2201", "CSC2014", "NET3204"],
            "attendance_history": [
                {"date": "2024-10-03", "time": "14:02:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-04", "time": "08:08:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-10", "time": "14:02:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-11", "time": "08:06:00", "subject": "NET3204", "status": "Present"},

                {"date": "2024-10-07", "time": "14:05:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-09", "time": "12:08:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-10", "time": "14:07:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-11", "time": "13:56:00", "subject": "NET2201", "status": "Present"},

                {"date": "2024-10-17", "time": "09:05:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-18", "time": "11:08:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-24", "time": "08:07:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-25", "time": "11:56:00", "subject": "CSC3034", "status": "Present"},

                {"date": "2024-10-08", "time": "11:55:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-09", "time": "17:28:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-15", "time": "11:48:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-23", "time": "17:36:00", "subject": "CSC2014", "status": "Present"},
            ]
        },
    "24008":
        {
            "name": "H",
            "major": "Computer Science",
            "intake": 2021,
            "total_attendance": 17,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-11-20 10:00:00",
            "enrolled_courses": ["PSY2164", "NET2201", "CSC2014", "NET3204"],
            "attendance_history": [
                {"date": "2024-10-10", "time": "17:18:00", "subject": "PSY2164", "status": "Present"},
                {"date": "2024-10-14", "time": "09:48:00", "subject": "PSY2164", "status": "Present"},
                {"date": "2024-10-17", "time": "17:36:00", "subject": "PSY2164", "status": "Present"},
                {"date": "2024-11-04", "time": "09:55:00", "subject": "PSY2164", "status": "Late"},
                {"date": "2024-11-07", "time": "17:28:00", "subject": "PSY2164", "status": "Present"},

                {"date": "2024-10-03", "time": "14:05:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-04", "time": "08:08:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-10", "time": "14:02:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-11", "time": "08:06:00", "subject": "NET3204", "status": "Present"},

                {"date": "2024-10-07", "time": "14:05:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-09", "time": "12:08:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-10", "time": "14:07:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-11", "time": "13:56:00", "subject": "NET2201", "status": "Present"},

                {"date": "2024-10-08", "time": "11:55:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-09", "time": "17:28:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-15", "time": "11:48:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-23", "time": "17:36:00", "subject": "CSC2014", "status": "Present"},
            ]
        },
    "24009":
        {
            "name": "J",
            "major": "Computer Science",
            "intake": 2022,
            "total_attendance": 12,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-11-20 10:00:00",
            "enrolled_courses": ["NET2201", "CSC2014", "NET3204"],
            "attendance_history": [
                {"date": "2024-10-03", "time": "14:05:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-04", "time": "08:08:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-10", "time": "14:02:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-11", "time": "08:06:00", "subject": "NET3204", "status": "Present"},

                {"date": "2024-10-07", "time": "14:05:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-09", "time": "12:08:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-10", "time": "14:07:00", "subject": "NET2201", "status": "Present"},
                {"date": "2024-10-11", "time": "13:56:00", "subject": "NET2201", "status": "Present"},

                {"date": "2024-10-08", "time": "11:55:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-09", "time": "17:28:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-15", "time": "11:48:00", "subject": "CSC2014", "status": "Present"},
                {"date": "2024-10-23", "time": "17:36:00", "subject": "CSC2014", "status": "Present"},
            ]
        },
    "24010":
        {
            "name": "K",
            "major": "Business Studies",
            "intake": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-11-20 10:00:00",
            "enrolled_courses": ["MKT2224"],
            "attendance_history": [
                {"date": "2024-09-23", "time": "15:06:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-09-26", "time": "12:56:00", "subject": "MKT2224", "status": "Late"},
                {"date": "2024-10-07", "time": "15:10:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-10", "time": "12:08:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-14", "time": "15:38:00", "subject": "MKT2224", "status": "Late"},
                {"date": "2024-11-04", "time": "15:02:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-11-07", "time": "12:02:00", "subject": "MKT2224", "status": "Present"},
            ]
        },
    "24011":
        {
            "name": "L",
            "major": "Computer Science",
            "intake": 2023,
            "total_attendance": 14,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-11-21 10:00:00",
            "enrolled_courses": ["NET3204", "MKT2224", "CSC3034"],
            "attendance_history": [
                {"date": "2024-10-03", "time": "14:05:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-04", "time": "08:08:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-10", "time": "14:02:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-11", "time": "08:06:00", "subject": "NET3204", "status": "Present"},

                {"date": "2024-10-03", "time": "09:05:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-04", "time": "11:08:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-24", "time": "08:07:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-25", "time": "11:56:00", "subject": "CSC3034", "status": "Present"},

                {"date": "2024-10-07", "time": "13:05:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-10", "time": "12:08:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-14", "time": "13:07:00", "subject": "MKT2224", "status": "Late"},
                {"date": "2024-10-17", "time": "12:56:00", "subject": "MKT2224", "status": "Late"},
                {"date": "2024-11-04", "time": "13:05:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-11-07", "time": "12:08:00", "subject": "MKT2224", "status": "Present"},
            ]
        },
    "24012":
        {
            "name": "M",
            "major": "Computer Science",
            "intake": 2022,
            "total_attendance": 14,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2024-11-22 10:00:00",
            "enrolled_courses": ["NET3204", "MKT2224", "CSC3034"],
            "attendance_history": [
                {"date": "2024-10-03", "time": "14:05:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-04", "time": "08:08:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-10", "time": "14:02:00", "subject": "NET3204", "status": "Present"},
                {"date": "2024-10-11", "time": "08:07:00", "subject": "NET3204", "status": "Present"},

                {"date": "2024-10-03", "time": "09:05:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-18", "time": "11:10:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-24", "time": "08:04:00", "subject": "CSC3034", "status": "Present"},
                {"date": "2024-10-25", "time": "11:56:00", "subject": "CSC3034", "status": "Present"},

                {"date": "2024-10-07", "time": "13:06:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-10", "time": "12:08:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-10-14", "time": "13:03:00", "subject": "MKT2224", "status": "Late"},
                {"date": "2024-10-17", "time": "12:58:00", "subject": "MKT2224", "status": "Late"},
                {"date": "2024-11-04", "time": "13:02:00", "subject": "MKT2224", "status": "Present"},
                {"date": "2024-11-07", "time": "12:02:00", "subject": "MKT2224", "status": "Present"},
            ]
        }
}

# Data for courses
courses_data = {
    "CSC3034": {
        "course_name": "Computational Intelligence",
        "instructor": "Dr. Richard",
        "schedule": {
            "Thursday": "08:00 - 10:00",
            "Friday": "10:00 - 12:00"
        },
        "students": ["24001", "24003", "24004", "24005", "24007", "24011", "24012"],
    },
    "PSY2164": {
        "course_name": "Intro to Psychology",
        "instructor": "Dr. Fam",
        "schedule": {
            "Monday": "08:00 - 10:00",
            "Thursday": "16:00 - 18:00"
        },
        "students": ["24004", "24005", "24008"]
    },
    "NET2201": {
        "course_name": "Computer Networks",
        "instructor": "Dr. Saad",
        "schedule": {
            "Monday": "14:00 - 16:00",
            "Wednesday": "12:00 - 14:00"
        },
        "students": ["24001", "24003", "24007", "24008", "24009"]
    },
    "MKT2224": {
        "course_name": "Principles of Marketing",
        "instructor": "Dr. Anjue",
        "schedule": {
            "Monday": "15:00 - 16:00",
            "Thursday": "12:00 - 13:00"
        },
        "students": ["24004", "24005", "24006", "24010", "24011", "24012"]
    },
    "CSC2014": {
        "course_name": "Digital Image Processing",
        "instructor": "Dr. David",
        "schedule": {
            "Tuesday": "10:00 - 12:00",
            "Wednesday": "14:00 - 16:00"
        },
        "students": ["24001", "24003", "24007", "24008", "24009"]
    },
    "NET3204": {
        "course_name": "Distributed Systems",
        "instructor": "Dr. Yawar",
        "schedule": {
            "Thursday": "14:00 - 16:00",
            "Friday": "08:00 - 10:00"
        },
        "students": ["24001"", 24002", "24003", "24004", "24005", "24006", "24007", "24008", "24009", "24011", "24012"]
    },
}

# Upload the data to Firebase
print("Uploading students data...")
ref_students.set(students_data)

print("Uploading courses data...")
ref_courses.set(courses_data)

print("Data uploaded successfully!")


# Save students data
with open('students_data.json', 'w') as json_file:
    json.dump(students_data, json_file, indent=4)

# Save courses data
with open('courses_data.json', 'w') as json_file:
    json.dump(courses_data, json_file, indent=4)

print("JSON files saved successfully.")

# Load the JSON file
with open('students_data.json', 'r') as json_file:
    students_data = json.load(json_file)

# Convert JSON to a pandas DataFrame
students_list = [
    {
        "student_id": student_id,
        **student_info
    }
    for student_id, student_info in students_data.items()
]
students_df = pd.DataFrame(students_list)

# Save to CSV
students_df.to_csv('students_data.csv', index=False)
print("Students data converted to CSV.")

# Load the JSON file
with open('courses_data.json', 'r') as json_file:
    courses_data = json.load(json_file)

# Convert JSON to a pandas DataFrame
courses_list = [
    {
        "course_id": course_id,
        **course_info
    }
    for course_id, course_info in courses_data.items()
]
courses_df = pd.DataFrame(courses_list)

# Save to CSV
courses_df.to_csv('courses_data.csv', index=False)
print("Courses data converted to CSV.")




