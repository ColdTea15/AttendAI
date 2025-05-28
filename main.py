import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials, db, storage
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-database-name.firebaseio.com/',
    'storageBucket': 'your-bucket-name.appspot.com',
    # Replace with your Firebase project details
})

bucket = storage.bucket()

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

imgBackground = cv2.imread('Resources/background.png')

# check size
height, width, channels = imgBackground.shape
print(f'Background Image Dimensions: {width}x{height}')

# Importing the mode images into a list
folderModePath = 'Resources/Modes'
modePath = sorted(
    [file for file in os.listdir(folderModePath) if file.endswith(('.png', '.jpg', '.jpeg'))],
    key=lambda x: int(os.path.splitext(x)[0])
)

# Initialize modeType
modeType = 0  # Default to the first mode

imgMode = []  # List to hold mode images
for mode in modePath:
    imgMode.append(cv2.imread(os.path.join(folderModePath, mode)))

# Print the dimensions of the specific mode image you are going to place
height_mode, width_mode, _ = imgMode[modeType].shape
print(f'Mode Image Dimensions: {width_mode}x{height_mode}')

# Load the encoding file
print('Loading Encode File...')
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIDs = pickle.load(file)
file.close()

encodeListKnown, studentIDs = encodeListKnownWithIDs
print(studentIDs)
print('Encode File Loaded')

modeType = 0
counter = 0
id = -1
studentInfo = []
imgStudent = []
prev_id = -1
stable_count = 0  # Counter to track stable recognition

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurrFrame = face_recognition.face_locations(imgS)
    encodeCurrFrame = face_recognition.face_encodings(imgS, faceCurrFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgMode[modeType]

    if faceCurrFrame:
        for encodeFace, faceLoc in zip(encodeCurrFrame, faceCurrFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace, tolerance=0.4)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                id = studentIDs[matchIndex]

                # Stabilization: ensure the same ID is detected consistently over multiple frames
                if prev_id == id:
                    stable_count += 1
                else:
                    stable_count = 0  # Reset counter if a different face is detected

                prev_id = id  # Track the last detected ID

                if stable_count >= 5:  # Proceed only after 5 consecutive frames
                    if counter == 0:
                        cv2.imshow('Face Attendance', imgBackground)
                        cv2.waitKey(1)
                        counter = 1
                        modeType = 1

        if counter != 0:
            if counter == 1:
                studentInfo = db.reference(f'Students/{id}').get()
                print(studentInfo)
                blob = bucket.get_blob(f'Images/{id}.png')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array, cv2.COLOR_BGR2RGB)

                datetimeObject = datetime.strptime(studentInfo['last_attendance_time'],
                                                   "%Y-%m-%d %H:%M:%S")
                seconds_elapsed = (datetime.now() - datetimeObject).total_seconds()
                print(seconds_elapsed)
                if seconds_elapsed > 10:  # Increased time check to avoid marking too often
                    ref = db.reference(f'Students/{id}')
                    studentInfo['total_attendance'] += 1
                    ref.child('total_attendance').set(studentInfo['total_attendance'])
                    ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    modeType = 3
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 + 414] = imgMode[modeType]

            if modeType != 3:
                if 10 < counter < 20:
                    modeType = 2

                imgBackground[44:44 + 633, 808:808 + 414] = imgMode[modeType]

                if counter <= 10:
                    cv2.putText(imgBackground, str(studentInfo['total_attendance']), (861, 125),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(studentInfo['major']), (940, 550),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(id), (980, 493),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(studentInfo['standing']), (910, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(studentInfo['year']), (1025, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(studentInfo['intake']), (1125, 625),
                                cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1)


                    (w, h), _ = cv2.getTextSize(studentInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                    offset = (414 - w) // 2
                    cv2.putText(imgBackground, str(studentInfo['name']), (808 + offset, 445),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

                    imgBackground[175:175 + 216, 909:909 + 216] = imgStudent

                counter += 1

                if counter >= 20:
                    counter = 0
                    modeType = 0
                    studentInfo = []
                    imgStudent = []
                    imgBackground[44:44 + 633, 808:808 + 414] = imgMode[modeType]

    else:
        modeType = 0
        counter = 0

    cv2.imshow('Face Attendance', imgBackground)
    cv2.waitKey(1)