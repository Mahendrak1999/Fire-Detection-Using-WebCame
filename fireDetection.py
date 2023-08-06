import cv2
from playsound import playsound
import smtplib
import numpy as np

fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap = cv2.VideoCapture(0)

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 15., (640, 480))

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

    for (x, y, w, h) in fire:
        cv2.rectangle(frame, (x - 20, y - 20), (x + w + 20, y + h + 20), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        print("fire is detected")
        playsound('audio.mp3')
        li = ["mkkoravi1999@gmail.com", "mkkoravi1999@gmail.com"]
        for dest in li:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("hackercracker045@gmail.com", "Unoxhacker@123")
            message = "EMERGENCY .......! FIRE DETECTED AT YOUR SITE PLEASE CONFIRM AND CALL TO FIRE BRIGADE(02024458950)"
            s.sendmail("hackercracker045@gmail.com", dest, message)
            s.quit()
            boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))
            boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
            for (xA, yA, xB, yB) in boxes:
                # display the detected boxes in the colour picture
                cv2.rectangle(frame, (xA, yA), (xB, yB),
                              (0, 255, 0), 2)

            out.write(frame.astype('uint8'))
            print("person detected")

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
