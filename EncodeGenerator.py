import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-database-name.firebaseio.com/',
    'storageBucket': 'your-bucket-name.appspot.com',
    # Replace with your Firebase project details
})

# Importing student images
folderPath = 'Images'
pathList = [path for path in os.listdir(folderPath) if path.endswith(('.png', '.jpg', '.jpeg'))]
imgList = []
studentIDs = []

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIDs.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

def find_encodings(imagesList):
    encode_list = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list

print('Encoding Started...')
encodeListKnown = find_encodings(imgList)
encodeListKnownWithIDs = [encodeListKnown, studentIDs]
print('Encoding Complete')

file = open('EncodeFile.p', 'wb')
pickle.dump(encodeListKnownWithIDs, file)
file.close()
print('File Saved')
