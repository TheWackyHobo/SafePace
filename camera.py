from picamera2.encoders import H264Encoder, Quality
from picamera2 import Picamera2
from datetime import datetime
import time

def record_video(duration = 10):
    # Initialize the camera
    picam2 = Picamera2()
    picam2.configure(picam2.create_video_configuration())
    
    # Get current date and time for the filename
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{current_datetime}.h264"
    
    # Set up the encoder for 60fps and very high quality
    encoder = H264Encoder(iperiod=60)
    
    # Start recording
    picam2.start_recording(encoder, filename, quality=Quality.VERY_HIGH)
    
    # Record for 10 seconds
    time.sleep(duration)
    
    # Stop recording
    picam2.stop_recording()
    
    # Return the filename for confirmation
    return filename

# Call the function to start recording
#filename = record_video(10)
#print(f"Video saved as: {filename}")
