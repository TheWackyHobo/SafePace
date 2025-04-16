from picamera2.encoders import H264Encoder, Quality
from picamera2 import Picamera2
from datetime import datetime
import time
import os

def record_video(duration=10, save_dir="videos"):
    # Ensure the directory exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Initialize the camera
    picam2 = Picamera2()

    try:
        # Configure the camera for video
        picam2.configure(picam2.create_video_configuration())

        # Get current date and time for the filename
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{current_datetime}.h264"
        
        # Combine the directory path with the filename
        file_path = os.path.join(save_dir, filename)
        
        # Set up the encoder for 60fps and very high quality
        encoder = H264Encoder(iperiod=60)

        # Start recording
        picam2.start_recording(encoder, file_path, quality=Quality.VERY_HIGH)

        # Record for the given duration
        time.sleep(duration)

        # Stop recording
        picam2.stop_recording()

    except Exception as e:
        print(f"An error occurred during recording: {e}")

    finally:
        # Always clean up the camera after use
        picam2.close()

    # Return the file path for confirmation
    return file_path

# Call the function to start recording and save it in the "videos" folder
# filename = record_video(10, save_dir="videos")
# print(f"Video saved as: {filename}")

# # You can now call the function again and it will save in the same folder
# filename2 = record_video(15, save_dir="videos")
# print(f"Video saved as: {filename2}")
