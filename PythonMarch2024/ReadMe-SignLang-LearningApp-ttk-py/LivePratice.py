import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting...")
        break
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1)
    if key == 27:  # Check for the Esc key (ASCII value 27)
        break

cap.release()
cv2.destroyAllWindows()
