<<<<<<< HEAD
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        # If only one face, convert to list
        if isinstance(results, dict):
            results = [results]

        for face in results:
            region = face['region']

            # Correct extraction
            x = region['x']
            y = region['y']
            w = region['w']
            h = region['h']

            emotion = face['dominant_emotion']

            # Draw box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Emotion above box
            cv2.putText(frame, emotion, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (0, 255, 0), 2)

    except Exception as e:
        print("Error:", e)

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
=======
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        # If only one face, convert to list
        if isinstance(results, dict):
            results = [results]

        for face in results:
            region = face['region']

            # Correct extraction
            x = region['x']
            y = region['y']
            w = region['w']
            h = region['h']

            emotion = face['dominant_emotion']

            # Draw box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Emotion above box
            cv2.putText(frame, emotion, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (0, 255, 0), 2)

    except Exception as e:
        print("Error:", e)

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
>>>>>>> 7dcb794e88e1107acfff1074e58dafc02225cf19
