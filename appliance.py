import cv2
import numpy as np
import matplotlib.pyplot as plt

# Initialize the video capture
cap = cv2.VideoCapture(0)  # Use 0 for default camera, or provide a video file path

# Initialize heatmap parameters
heatmap = None
alpha = 0.5  # Heatmap transparency (adjust as needed)
scale_factor = 0.1  # Resize factor to reduce processing time (adjust as needed)

while True:
    # Capture a frame from the video feed
    ret, frame = cap.read()

    # Resize the frame for faster processing (optional, adjust scale_factor)
    small_frame = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor)

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)

    # Apply a colormap to create a heatmap
    heatmap_frame = cv2.applyColorMap(gray_frame, cv2.COLORMAP_JET)

    # Resize the heatmap to match the original frame size
    heatmap_frame = cv2.resize(heatmap_frame, frame.shape[:2][::-1])

    # Combine the original frame and the heatmap
    if heatmap is None:
        heatmap = heatmap_frame
    else:
        heatmap = cv2.addWeighted(heatmap, alpha, heatmap_frame, 1 - alpha, 0)

    # Display the combined frame with the heatmap
    cv2.imshow('Live Heatmap', heatmap)

    # Capture the frame with the heatmap when 'c' is pressed
    key = cv2.waitKey(1)
    if key & 0xFF == ord('c'):
        cv2.imwrite('heatmap_capture.png', heatmap)
        print('Heatmap captured as heatmap_capture.png')

    # Press 'q' to exit the loop
    if key & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
