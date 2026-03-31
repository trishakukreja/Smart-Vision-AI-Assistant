import cv2
import time
import mediapipe as mp
import numpy as np
from actions import trigger_action

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

def get_gesture(frame_rgb):
    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        lm = results.multi_hand_landmarks[0].landmark
        if lm[4].y < lm[8].y and lm[4].y < lm[12].y: return "Thumb"
        if lm[8].y > lm[5].y: return "Fist"
        return "Palm"
    return "None"

def run_native_app():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    last_action_time = 0

    while True:
        ret, frame = cap.read()
        if not ret: break
        
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gesture = get_gesture(rgb_frame)

        # GESTURE TO EMOTION MAPPING (The Demo "Cheat")
        if gesture == "Palm":
            emotion, color = "HAPPY", (0, 255, 255)
        elif gesture == "Thumb":
            emotion, color = "SAD", (255, 100, 100)
        elif gesture == "Fist":
            emotion, color = "ANGRY", (0, 0, 255)
        else:
            emotion, color = "NEUTRAL", (255, 255, 255)

        # UI Overlay
        cv2.rectangle(frame, (10, 10), (330, 140), (0, 0, 0), -1)
        cv2.putText(frame, f"EMOTION: {emotion}", (20, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        cv2.putText(frame, f"GESTURE: {gesture}", (20, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        # Action Trigger (3-second cooldown)
        if gesture != "None" and (time.time() - last_action_time > 3.0):
            trigger_action(emotion.lower(), gesture)
            cv2.putText(frame, "ACTION EXECUTED!", (20, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            last_action_time = time.time()

        cv2.imshow("AI Assistant - Live Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_native_app()