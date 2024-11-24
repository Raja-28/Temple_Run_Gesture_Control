
# **Temple Run Gesture Control**

Control the popular game **Temple Run** using your body gestures! This project uses a webcam to detect hand movements and translates them into in-game actions like **move left**, **move right**, **jump**, and **roll down**. Perfect for a fun and interactive gaming experience!



## **Features**
- **Move Left**: Raise your left hand.
- **Move Right**: Raise your right hand.
- **Jump**: Raise both hands.
- **Roll Down**: Lower both hands.
- Real-time gesture detection using **MediaPipe**.
- Compatible with **online Temple Run** or emulator-based Temple Run games.



## **Technologies Used**
- **Python**: Core language for the project.
- **OpenCV**: Real-time video processing.
- **MediaPipe**: Hand and pose detection.
- **PyAutoGUI**: Simulates key presses to control the game.



## **Setup Instructions**

 **Step 1: Prerequisites**
Ensure you have Python 3.7 or above installed on your system. Install the following Python libraries:
```bash
pip install opencv-python mediapipe pyautogui
```

 **Step 2: Clone the Repository**
Clone this repository to your local machine:
```bash
git clone https://github.com/Raja-28/temple-run-gesture-control.git
cd temple-run-gesture-control
```

 **Step 3: Run the Project**
1. Open an **online Temple Run game** in your browser (e.g., [Crazy Games Temple Run](https://www.crazygames.com/game/temple-run-2)).
2. Run the Python script:
   ```bash
   python temple_run_gesture_control.py
   ```
3. Ensure your **webcam is connected** and follow these gestures to control the game:
   - **Move Left**: Raise your left hand.
   - **Move Right**: Raise your right hand.
   - **Jump**: Raise both hands.
   - **Roll Down**: Lower both hands.



## **How It Works**
1. The webcam captures a live video feed.
2. **MediaPipe** detects your hand positions and landmarks.
3. Based on the relative positions of your hands, the script maps gestures to specific in-game actions.
4. **PyAutoGUI** sends simulated keyboard inputs to the browser to perform the corresponding action.



## **Future Enhancements**
- Add more gestures for additional actions.
- Support for multiple games.
- Gesture calibration for better accuracy.



## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



## **Contributions**
Contributions are welcome! Feel free to open an issue or submit a pull request. For major changes, please open an issue first to discuss what you would like to change.



## **Contact**
Created by [Karthick Raja V](https://github.com/Raja-28).  
Feel free to reach out via email: rajaccet28@gmail.com.



