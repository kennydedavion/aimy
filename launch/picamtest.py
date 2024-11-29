from picamera import PiCamera
from time import sleep

camera = PiCamera(stereo_mode='side-by-side')

camera.start_preview()
sleep(5)
camera.stop_preview()