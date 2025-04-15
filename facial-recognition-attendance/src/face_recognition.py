import face_recognition
import numpy as np
from database import get_users, add_attendance_record

class FaceRecognition:
    def __init__(self):
        self.users = get_users()
        self.known_face_encodings = [np.frombuffer(user.face_encoding, dtype=np.float64) for user in self.users]
        self.known_face_names = [user.username for user in self.users]

    def recognize_faces(self, frame):
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        recognized_faces = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Desconocido"

            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]
                add_attendance_record(name)

            recognized_faces.append(name)

        return face_locations, recognized_faces
