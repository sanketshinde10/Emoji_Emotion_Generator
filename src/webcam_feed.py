import cv2
import mediapipe as mp
from emotion_detection import detect_emotion

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert frame to RGB for Mediapipe processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to detect landmarks
    results = face_mesh.process(rgb_frame)
    
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Extract landmarks
            landmarks = [(lm.x, lm.y) for lm in face_landmarks.landmark]
            
            # Detect emotion based on landmarks
            emotion = detect_emotion(landmarks)
            
            # Display the detected emotion
            print(f"Detected Emotion: {emotion}")
            
            # Display the result (optional)
            cv2.putText(frame, emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    
    # Show the frame
    cv2.imshow("Emotion Detection", frame)
    
    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
