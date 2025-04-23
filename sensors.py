import smbus2
import time
from motors import motor
from camera import record_video
from button_no_edge import was_button_pressed
from sms import send_email
from light import light
i2c_bus_number = 1  
left = 0x71
right = 0x72
back = 0x70
sensors = [left, right, back]
command_reg = 0x00  
distance_high_reg = 0x02  # High byte of the distance result
distance_low_reg = 0x03  # Low byte of the distance result
check = False
camera_check = 0
recipient_email = "keegan.pham@slu.edu" 
message = "SafePace test"
sender_email = "safe.pac3@gmail.com"
sender_password = "vpqo hufr cetl bord"
def read_distance(bus, sensor_address):
    try:
        # Write the command to initiate ranging in inches
        bus.write_byte_data(sensor_address, command_reg, 0x50, True)
        time.sleep(0.08)
        high_byte = bus.read_byte_data(sensor_address, distance_high_reg, True)
        low_byte = bus.read_byte_data(sensor_address, distance_low_reg, True)
        
        # Combine the bytes into a single 16-bit value
        distance_raw = (high_byte << 8) + low_byte
        distance_in = float(distance_raw)
        return distance_in
    except Exception as e:
        print(f"Error reading from sensor {hex(sensor_address)}: {e}")
        return None  # Return None to indicate failure

with smbus2.SMBus(i2c_bus_number) as bus:
    while True:
        check = False
        camera_check = 0
        for sensor in sensors:  # Loop through each sensor in the array
            check = was_button_pressed()
            distance = read_distance(bus, sensor) 
            if distance is None:
                print(f"Skipping sensor at {hex(sensor)} due to error")
                continue  # Explicitly move to the next sensorcode

            if 7 < distance < 12: #change to 84 for 7ft
                print(f"Sensor at {hex(sensor)}: {distance:.2f} inches")
                camera_check = 1
                motor(distance, sensor)
                

        if(check == True):
            print("ahhhhhh, scary mode")
            send_email("helppppp","jason.nguyen.1@slu.edu" )
            light()
        else:
            print("safe")
        if(camera_check ==1):
            record_video()
        time.sleep(0.05)  # Small delay to avoid excessive bus usage