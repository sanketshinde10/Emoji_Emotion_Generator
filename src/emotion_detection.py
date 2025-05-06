import cv2
import mediapipe as mp

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# Emotion detection logic based on facial landmarks
def detect_emotion(landmarks):
    # Get points for mouth, eyebrows, eyes (example indices)
    mouth_left = landmarks[61]
    mouth_right = landmarks[291]
    eyebrow_left = landmarks[52]
    eyebrow_right = landmarks[283]
    left_eye = landmarks[133]
    right_eye = landmarks[362]
    
    # Emotion rules (simplified)
    if mouth_right[1] - mouth_left[1] > 5:  # Smile (happy)
        return 'happy'
    elif eyebrow_left[1] > eyebrow_right[1]:  # Furrowed brows (angry)
        return 'angry'
    elif abs(left_eye[1] - right_eye[1]) > 10:  # Wide eyes (surprised)
        return 'surprised'
    elif mouth_left[1] - mouth_right[1] < -5:  # Downturned mouth (sad)
        return 'sad'
    else:
        return 'neutral'
