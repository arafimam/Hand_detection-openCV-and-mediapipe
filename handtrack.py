import cv2
import mediapipe as mp
import time

#algorithm:
#1. prompt IDE to open webcamera
#2.Create object for hands
#3.Convert image img to RGB image for multi_hand_landmark
#4.If results.multi_hand_landmarks is true draw on the img using the drawing utilities and connect using HAND_CONNECTIONS.
#5.put fps on screen. fps=1/(current_time-previous_time)
#Inspired from: https://google.github.io/mediapipe/solutions/hands.html


cap=cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpDraw=mp.solutions.drawing_utils

current_time=0
previous_time=0


while True:
    success, img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    current_time=time.time()
    fps=1/(current_time-previous_time)
    previous_time=current_time
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image",img)
    cv2.waitKey(1)

