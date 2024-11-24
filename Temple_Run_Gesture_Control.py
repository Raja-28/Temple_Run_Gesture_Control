import cv2
import mediapipe as mp
import pyautogui

# Disable PyAutoGUI fail-safe (optional)
pyautogui.FAILSAFE = False

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Capture video from webcam
cap = cv2.VideoCapture(0)

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame for a mirror effect and process it
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = pose.process(rgb_frame)

        if result.pose_landmarks:
            # Extract body landmarks
            landmarks = result.pose_landmarks.landmark

            # Get key points for hands and hips
            left_hand = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
            right_hand = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
            left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
            right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
            nose = landmarks[mp_pose.PoseLandmark.NOSE.value]

            # 1. **Move Left** - Left hand is higher than the left shoulder
            if left_hand.y < left_hip.y and right_hand.y > right_hip.y:
                print("Left Hand Raised - Moving Left")
                pyautogui.press('left')

            # 2. **Move Right** - Right hand is higher than the right shoulder
            elif right_hand.y < right_hip.y and left_hand.y > left_hip.y:
                print("Right Hand Raised - Moving Right")
                pyautogui.press('right')

            # 3. **Jump** - Both hands raised above the shoulders
            elif left_hand.y < nose.y and right_hand.y < nose.y:
                print("Both Hands Raised - Jumping")
                pyautogui.press('up')

            # 4. **Roll Down** - Both hands are below the hips
            elif left_hand.y > left_hip.y and right_hand.y > right_hip.y:
                print("Hands Down - Rolling Down")
                pyautogui.press('down')

            # Visual feedback: Draw pose landmarks
            mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Display the frame
        cv2.imshow('Temple Run Hand Gesture Control', frame)

        # Exit loop when 'q' is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Release resources
    cap.release()
    cv2.destroyAllWindows()
