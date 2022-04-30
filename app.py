from flask import Flask
from flask import Flask,request,render_template
from flask import Response
from camera import Camera
import cv2 
app = Flask(__name__)

video = cv2.VideoCapture(0)

my_list = [["12","S1"],["13","S2"],["14","S3"],["15","S4"],["16","S5"]]
@app.route('/')
def index():
    return render_template('index.html',my_list = my_list, list_count = len(my_list))

def gen(camera):
    while True:
        success, image = video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        image = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')

@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),mimetype='multipart/x-mixed-replace; boundary=frame')


