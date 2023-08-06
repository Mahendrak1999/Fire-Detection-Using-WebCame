# import the necessary packages
import cv2
from flask import Flask, render_template, redirect, url_for, request, Response

from camera import VideoCamera

app = Flask(__name__)

fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap = cv2.VideoCapture(0)

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), 15., (640, 480))


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('camera'))
    return render_template('login.html', error=error)


@app.route('/camera', methods=['GET', 'POST'])
def camera():
    return render_template('camera.html')


def generate_frames(camera):

                    frame = camera.get_frame()

                    yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_stream')
def video_stream():
    return Response(generate_frames(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
