import cv2

face_classfier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Accessing the webcam
video_capture = cv2.VideoCapture(0)

# Identifying faces in the video stream
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classfier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

# Creating a loop for real-time face detection
while True:
    result, video_frame = video_capture.read() # --> read the frames from the video
    if result is False:
        break # --> finishes the loop if the frame is not read successfully
    faces = detect_bounding_box(
        video_frame # --> apply the function we created to the video frame
    )
    cv2.imshow(
        "Face Detection Project", video_frame # it displays the processed window.
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()