from flask import Flask, render_template, Response, send_from_directory
from camera import Camera
from face_recognition import FaceRecognition
import cv2  # Importación de OpenCV
import os

app = Flask(__name__, static_folder="../", template_folder="../")
face_recognition = FaceRecognition()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(app.static_folder, path)

def generate_frames():
    camera = Camera()
    camera.start_camera()
    while True:
        frame = camera.capture_image()
        if frame is not None:
            face_recognition.recognize_faces(frame)
            _, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)