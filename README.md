# Attendance System Using Face Recognition

![Banner](path/to/your/banner-image.png)

## 📸 Overview

Welcome to the **Facial Recognition Attendance System**! This project leverages the power of Python, Dlib, and OpenCV to provide a seamless, real-time attendance tracking solution using facial recognition technology. The system captures images from a live camera feed, recognizes faces, and logs attendance into a SQLite database. A user-friendly Flask web interface allows you to view attendance records effortlessly.

## 🌟 Features

- **Real-Time Face Detection & Recognition**: Efficiently detects and recognizes faces using Dlib's ResNet model.
- **Automatic Attendance Logging**: Records attendance with precise timestamps directly into a SQLite database.
- **Web Interface**: View attendance records for any selected date through a sleek Flask web app.
- **Centroid Tracking**: Ensures accurate tracking of faces across video frames for reliable recognition.

![Demo](path/to/your/demo-image.gif)

## 🛠️ Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/facial-recognition-attendance-system.git
    cd facial-recognition-attendance-system
    ```

2. **Install required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Download Dlib's pretrained models:**
    - [shape_predictor_68_face_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
    - [dlib_face_recognition_resnet_model_v1.dat](http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2)

    Place these files in the `data/data_dlib/` directory.

4. **Run the system:**
    ```bash
    python app.py
    ```

5. **Start the Flask web server:**
    ```bash
    python flask_app.py
    ```

## 🚀 Usage

1. **Capture and register faces:**
   Run the script to capture and register faces into the system. Make sure your camera is connected.

2. **Start the attendance system:**
   Begin real-time face recognition and attendance logging by running the main script.

3. **View attendance records:**
   Open your browser and go to `http://localhost:9879` to access the web interface. Select the date to view attendance records.

![Web Interface](path/to/your/web-interface-image.png)



## 🛡️ Security

- **Data Encryption**: Ensures secure data transmission between the client and server.
- **Authentication**: Only authorized users can access the attendance data.
- **Privacy Protection**: Facial recognition data is stored securely and used only for attendance purposes.

## 📚 Documentation

- **Face Detection & Recognition**: Utilizes Dlib's frontal face detector and ResNet-based face recognition model.
- **Database Management**: SQLite database for efficient and reliable attendance data storage.
- **Web Interface**: Flask framework for a simple yet powerful web interface to display attendance records.

## 🧩 System Architecture

[Architecture](path/to/your/footer-image.png)

## 📜 License

This project is licensed under the MIT License. See the License file for more details.

## 👥 Contributors

- ARMAN AHMED

## 💬 Contact

For any queries or suggestions, feel free to reach out via armanofficial2401@gmail.com or open an issue on GitHub.

![Footer](path/to/your/footer-image.png)

