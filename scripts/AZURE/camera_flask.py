from flask import Flask
from TakePicture import camera

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from python flask webapp!, try /image.jpg /postimage"

@app.route('/image.jpg')
def image():
    cam.TakePicture()
    return app.send_static_file("image.jpg")

@app.route('/postimage')
def postimage():
    postblob()
    return "image posted https://portalvhdskb2vtjmyg3mg.blob.core.windows.net/webcam/picture"

if __name__=='_main_':
    #initialize the camera
    cam = camera()
    #initialize IoTHub
    client = iothub_client_init()
    #run flask, host = 0.0.0.0 needed to get access to it 
    # outside of the host
    app.run(host = '0.0.0.0', port = 1337)