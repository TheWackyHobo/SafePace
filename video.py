from picamera2.encoders import H264Encoder, Quality
from picamera2 import Picamera2
from datetime import datetime
import time
picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration())
encoder = H264Encoder(iperiod=60)
picam2.start_recording(encoder, 'test_very_high_60_frames.h264', quality=Quality.VERY_HIGH)
time.sleep(20)
picam2.stop_recording()\




current_datetime = datetime.now()
print(current_datetime)