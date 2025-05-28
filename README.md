<<<<<<< HEAD
# AttendAI
AttendAI is a real-time attendance tracking system using facial recognition built with Python and Flask. It leverages Firebase for data storage and Jam AI for a conversational chatbot, enabling seamless student registration, attendance logging, and interactive queries via a web dashboard.
=======
Here is your **final and fully updated `README.md` file**, combining all important details from both versions you provided. It's organized for clarity, GitHub-readiness, and developer usability:

---

# Face Attendance Real-Time System

## 📌 Overview

This project implements a real-time face recognition-based attendance system using **Flask**, **Firebase**, and **Python** libraries. It allows administrators to register students, encode their facial data, track attendance, and interact via a **Jam AI Base** chatbot and dashboard.

---

## ✨ Features

1. 🎥 **Real-Time Face Recognition** – Identifies students using live video and `face_recognition`.
2. 🔥 **Firebase Integration** – Stores and syncs student records and attendance.
3. 🌐 **Web-Based Interface** – Chatbot and admin dashboard built with Flask.
4. 📊 **Data Export** – Convert attendance logs to JSON and CSV for analysis or chatbot training.
5. 🤖 **Jam AI-Powered Chatbot** – Answers attendance queries from users.

---

## 🗂️ Project Structure

```
Facial_recognition_RealTimeDatabase/
│
├── env/                        # Virtual environment (not in repo)
├── Images/                     # Student face images
├── Resources/
│   └── Modes/                  # UI state images (e.g., background.png)
│
├── static/
│   ├── js/
│   │   └── script.js           # Web interactivity
│   ├── bot.png                 # Chatbot icon
│   └── user.png                # User icon
│
├── templates/
│   ├── chatbot.html            # JamAI chatbot interface
│   ├── dashboard.html          # Admin dashboard
│   └── visualize.html          # Visualization page
│
├── AddDataToDatabase.py        # Upload student data to Firebase
├── EncodeGenerator.py          # Generate face encodings
├── EncodeFile.p                # Serialized face encodings
├── main.py                     # Real-time facial recognition logic
├── web.py                      # Flask web app + chatbot + API routes
├── courses_data.csv / .json    # Sample course data
├── students_data.csv / .json   # Sample student data
├── convert_json_to_csv.py      # Converts student data for Jam AI Base
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

* Python 3.8+
* Firebase Project (Realtime Database + Storage)
* Jam AI Base Account & API Key

---

### 🚀 Installation

1. **Clone the repository**:

   ```bash
   git clone  <repository_url>
   cd <repository_folder>
   ```

2. **Create a virtual environment (optional)**:

   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Firebase**:

   * Go to [Firebase Console](https://console.firebase.google.com/).
   * Create a project and enable Realtime Database and Storage.
   * Download the service account JSON key.
   * Save it as `serviceAccountKey.json` in your project root.
     ⚠️ **Do not upload this file to GitHub.**

5. **Configure Jam AI API Key**:

   * Create a `.env` file in the root directory:

     ```bash
     JAMAI_API_KEY=your_jamai_api_key_here
     ```
   * Refer to `.env.example` as a guide.

---

## 🏁 Running the App

1. **Upload student data to Firebase**:

   ```bash
   python AddDataToDatabase.py
   ```

2. **Generate facial encodings**:

   ```bash
   python EncodeGenerator.py
   ```

3. **Start facial recognition system (optional)**:

   ```bash
   python main.py
   ```

4. **Run the web server**:

   ```bash
   python web.py
   ```

5. **Open in browser**:

   ```
   http://127.0.0.1:5000
   ```

---

## 🔍 Key Functionalities

### 🧑 Add Students to Firebase

Run `AddDataToDatabase.py` to push student details (name, course, year, etc.) to Firebase.

### 🧠 Encode Faces

Run `EncodeGenerator.py` to create and save facial encodings from images in `Images/`.

### 📹 Real-Time Recognition

`main.py` captures webcam video, identifies known faces, and logs attendance to Firebase.

### 💬 Chatbot Interface (Jam AI Base)

`web.py` runs a chatbot that:

* Answers queries like “Who attended Web Dev yesterday?”
* Uses the converted CSV (`students_data.csv`) uploaded to Jam AI.

### 📊 Dashboard & API

Includes:

* Attendance visualizations
* Student/course-level analytics
* JSON export for backup

---

## ☁️ Deployment Tips

* Recommended Platforms: **Render**, **Heroku**, **Vercel (via Python API route)**, **Google Cloud Run**
* Use `.env` variables securely
* Run Flask with `gunicorn` in production

---

## 🛠️ Known Issues & Roadmap

### Issues

* Face recognition accuracy depends on image quality & lighting
* No concurrency handling in webcam input
* Lag with large datasets

### Future Enhancements

* ✅ Multi-face recognition
* ✅ Mobile app version (Android/iOS)
* ✅ Role-based login for teachers/admins
* ✅ Enhanced chatbot analytics (Jam AI follow-ups)


## 📄 License

This project is licensed under the **MIT License**.

---

## 📬 Contact

* **Name**: \[Colman Tee]
* **Email**: \[[olmantjs03@gmail.com](mailto:colmantjs03@gmail.com)]
* **GitHub**: \[github.com/ColdTea15]
>>>>>>> 5495190 (Initial commit)
