import cv2

# Initialize the webcam (0 is typically the default camera)
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Error: Could not open the webcam.")
else:
    while True:
        ret, frame = webcam.read()
        if not ret:
            print("Error: Could not read a frame from the webcam.")
            break

        # Display the frame in a window
        cv2.imshow("Webcam Feed", frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    webcam.release()
    cv2.destroyAllWindows()
