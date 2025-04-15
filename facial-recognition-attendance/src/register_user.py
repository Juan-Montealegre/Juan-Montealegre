import face_recognition
import cv2
from database import add_user

def register_user(username):
    video_capture = cv2.VideoCapture(0)
    print("Por favor, mira a la cámara para registrar tu rostro.")

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Error al acceder a la cámara.")
            break

        cv2.imshow('Registro de Usuario', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Presiona 'q' para capturar
            face_locations = face_recognition.face_locations(frame)
            if len(face_locations) == 1:
                face_encoding = face_recognition.face_encodings(frame, face_locations)[0]
                add_user(username, face_encoding.tobytes())
                print(f"Usuario {username} registrado exitosamente.")
                break
            else:
                print("Por favor, asegúrate de que solo haya un rostro visible.")

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    username = input("Ingresa el nombre de usuario: ")
    register_user(username)