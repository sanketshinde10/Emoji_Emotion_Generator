import tkinter as tk
from webcam_feed import detect_emotion
import cv2
import mediapipe as mp

# Initialize Tkinter window
root = tk.Tk()
root.title("Emotion Generator")

# Create label to display emotion and emoji
emotion_label = tk.Label(root, text="Emotion: ", font=("Helvetica", 24))
emotion_label.pack()

# Emoji dictionary
emotions_dict = {
    "happy": "🙂",
    "sad": "☹️",
    "angry": "😡",
    "surprised": "😲",
    "neutral": "😐"
}

# Webcam capture and emotion detection
cap = cv2.VideoCapture(0)
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

def update_frame():
    ret, frame = cap.read()
    if ret:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)
        
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                landmarks = [(lm.x, lm.y) for lm in face_landmarks.landmark]
                emotion = detect_emotion(landmarks)
                emoji = emotions_dict.get(emotion, "😐")
                
                # Update the emotion label with detected emotion and emoji
                emotion_label.config(text=f"Emotion: {emotion} {emoji}")
    
    # Update frame every 100ms
    root.after(100, update_frame)

# Start updating the frame
update_frame()

# Start the Tkinter event loop
root.mainloop()
