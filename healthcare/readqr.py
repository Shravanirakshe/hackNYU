from flask import Flask
import cv2
import json
from flask import render_template

app = Flask(__name__)

@app.route('/data/')
def show_details():

    # import the opencv library
    # define a video capture object
    vid = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        # Capture the video frame by frame
        ret, frame = vid.read()
        data, bbox, straight_qrcode = detector.detectAndDecode(frame)
        if len(data) > 0:
            break
        # Display the resulting frame
        cv2.imshow('frame', frame)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    data = data.replace('\'', '"')
    data = json.loads(data)
    return render_template('data.html', data = data)

@app.route("/")
def home():
    # This is the home page
    return render_template('index.html')
    
