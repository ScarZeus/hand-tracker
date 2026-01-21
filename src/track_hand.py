import cv2
import mediapipe as mp
import time
import numpy as np
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2

model_path = "/home/k-kevin-gladson/Documents/hand-track-counter/models/hand_landmarker.task"

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = vision.HandLandmarker
HandLandmarkerOptions = vision.HandLandmarkerOptions
VisionRunningMode = vision.RunningMode


def open_camera(camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise RuntimeError("Could not open camera")
    return cap


def draw_landmarks_on_image(image, result):
    if not result.hand_landmarks:
        return image

    annotated = image.copy()

    for hand_landmarks in result.hand_landmarks:
        proto = landmark_pb2.NormalizedLandmarkList()
        proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=l.x, y=l.y, z=l.z)
            for l in hand_landmarks
        ])

        mp.solutions.drawing_utils.draw_landmarks(
            annotated,
            proto,
            mp.solutions.hands.HAND_CONNECTIONS,
            mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
            mp.solutions.drawing_styles.get_default_hand_connections_style()
        )

    return annotated


def track_hand_in_frame(cap):
    cv2.namedWindow("Track Window", cv2.WINDOW_AUTOSIZE)

    options = HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=model_path),
        running_mode=VisionRunningMode.VIDEO,
        num_hands=2,
        min_hand_detection_confidence=0.3,
        min_hand_presence_confidence=0.3,
        min_tracking_confidence=0.3,
    )

    with HandLandmarker.create_from_options(options) as landmarker:
        timestamp_ms = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=frame
            )

            result = landmarker.detect_for_video(mp_image, timestamp_ms)

            frame = draw_landmarks_on_image(frame, result)

            cv2.imshow("Track Window", frame)

            timestamp_ms += int(1000 / 30)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    close_camera(cap)


def close_camera(cap):
    cap.release()
    cv2.destroyAllWindows()


def handTracker():
    cap = open_camera()
    track_hand_in_frame(cap)
