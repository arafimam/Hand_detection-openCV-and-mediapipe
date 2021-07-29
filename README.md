# Hand_detection
This is a very basic hand detection solution.
Frameworks used: mediapipe
MediaPipe Hands is a high-fidelity hand and finger tracking solution. It employs machine learning (ML) to infer 21 3D landmarks of a hand from just a single frame.

MediaPipe Hands has multiple models working together. At first, we have the palm detection method that operates on the full image and returns an oriented hand bounding box. 
Then we have the hand landmark model that operates on the cropped image region defined by the palm detector and returns high-fidelity 3D hand keypoints


MULTI_HAND_LANDMARKS
Collection of detected/tracked hands, where each hand is represented as a list of 21 hand landmarks and each landmark is composed of x, y and z. x and y are
normalized to [0.0, 1.0] by the image width and height respectively. z represents the landmark depth with the depth at the wrist being the origin, 
and the smaller the value the closer the landmark is to the camera. The magnitude of z uses roughly the same scale as x.

I have also impletemented a technique that shows that frame per second in the web camera that will be opened. You can see it in the top left corner of the opened webcam:

![Screenshot (909)](https://user-images.githubusercontent.com/86128944/127511779-85cd2684-4e7e-4337-acce-bd57c374f7a3.png)


![Screenshot (906)](https://user-images.githubusercontent.com/86128944/127511919-9304e670-2279-47a4-b227-abff402f8a69.png)



