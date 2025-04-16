import cv2
import face_recognition
import os
import numpy as np
from encryption.crypto import encrypt_data, decrypt_data, load_key, save_key

ENCODED_FACE_PATH = "saved_data/face_data.enc"
KEY_PATH = "saved_data/key.key"

def capture_face():
    cam = cv2.VideoCapture(0)
    print("Capturing face. Press 'c' to capture.")
    face_encoding = None
    while True:
        ret, frame = cam.read()
        if not ret:
            continue
        cv2.imshow("Capture Face", frame)
        key = cv2.waitKey(1)
        if key == ord("c"):
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            faces = face_recognition.face_locations(rgb)
            if faces:
                face_encoding = face_recognition.face_encodings(rgb, faces)[0]
                print("Face captured and encoded.")
                break
            else:
                print("No face detected.")
    cam.release()
    cv2.destroyAllWindows()
    return face_encoding

def register_face():
    print("Registering new face...")
    encoding = capture_face()
    if encoding is not None:
        os.makedirs("saved_data", exist_ok=True)
        save_key(KEY_PATH)
        key = load_key(KEY_PATH)
        encrypt_data(ENCODED_FACE_PATH, encoding.tobytes(), key)
        print("Face registered and saved securely.")

def authenticate_face():
    if not os.path.exists(ENCODED_FACE_PATH) or not os.path.exists(KEY_PATH):
        print("No registered face found.")
        return
    key = load_key(KEY_PATH)
    enc_data = decrypt_data(ENCODED_FACE_PATH, key)
    registered_encoding = np.frombuffer(enc_data, dtype=np.float64)

    print("Authenticating face...")
    live_encoding = capture_face()
    
    # Use face_distance for real matching
    distance = face_recognition.face_distance([registered_encoding], live_encoding)[0]
    print(f"Face distance: {distance:.4f}")

    # The lower the distance, the better. 0.6 is default, we use 0.45 for stricter match
    if distance < 0.45:
        print("Authentication Successful ✅")
    else:
        print("Authentication Failed ❌")

if __name__ == "__main__":
    while True:
        print("\n1. Register Face\n2. Authenticate\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register_face()
        elif choice == "2":
            authenticate_face()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
