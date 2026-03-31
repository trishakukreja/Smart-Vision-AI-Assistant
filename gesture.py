import mediapipe as mp

class GestureDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

    def get_gesture(self, frame_rgb):
        results = self.hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            lm = results.multi_hand_landmarks[0].landmark
            
            # 1. THUMB UP (Thumb tip is higher than all other fingertips)
            if lm[4].y < lm[8].y and lm[4].y < lm[12].y:
                return "Thumb", results.multi_hand_landmarks[0]
            
            # 2. FIST (Index tip is below its base)
            if lm[8].y > lm[5].y:
                return "Fist", results.multi_hand_landmarks[0]
            
            # 3. PALM (Default if fingers are extended)
            return "Palm", results.multi_hand_landmarks[0]
            
        return "None", None