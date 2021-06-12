from flask import Flask,render_template,Response
import cv2
app = Flask(__name__)


#  Generating the camera
cap = cv2. VideoCapture(0)

def img_capture():
    while True:
        ret,photo = cap.read()
        if not ret:
            break
        else:
            ret, jpeg = cv2.imencode('.jpg',photo)
            print(photo)
            photo = jpeg.tobytes()
            yield (b'--photo\r\n' b'Content-Type: image/jpeg\r\n\r\n' + photo + b'\r\n')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/live_stream')
def live_stream():
    return Response(img_capture(),mimetype='multipart/x-mixed-replace;boundary=photo')


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')