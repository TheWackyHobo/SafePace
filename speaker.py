import RPi.GPIO as GPIO
import wave
import struct
import time
import os

# Setup
BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

base_dir = os.path.dirname(__file__)
path_to_wav = os.path.join(base_dir, "levels.wav")

def play_square_wave_wav(filename, downsample=1):
    with wave.open(filename, 'rb') as wf:
        rate = wf.getframerate()
        width = wf.getsampwidth()
        frames = wf.getnframes()
        channels = wf.getnchannels()

        raw = wf.readframes(frames)
        delay = 1.0 / rate * downsample

        print(f"Sample Rate: {rate}, Sample Width: {width}, Channels: {channels}, Downsample: {downsample}")

        for i in range(0, len(raw), width * downsample):
            if width == 1:
                val = struct.unpack('<B', raw[i:i+1])[0] - 128  # unsigned 8-bit PCM
            elif width == 2:
                val = struct.unpack('<h', raw[i:i+2])[0]       # signed 16-bit PCM
            else:
                print("Unsupported sample width")
                break

            # GPIO HIGH for positive sample, LOW otherwise
            GPIO.output(BUZZER_PIN, GPIO.HIGH if val > 0 else GPIO.LOW)
            time.sleep(delay)

try:
    play_square_wave_wav(path_to_wav, downsample=4)
finally:
    GPIO.cleanup()
