import smbus2
import time
from motors import motor

i2c_bus_number = 1  
left = 0x71
right = 0x72
back = 0x70
sensors = [left, right, back]
command_reg = 0x00  
distance_high_reg = 0x02  # High byte of the distance result
distance_low_reg = 0x03  # Low byte of the distance result

def read_distance(bus, sensor_address):
    try:
        # Write the command to initiate ranging in inches
        bus.write_byte_data(sensor_address, command_reg, 0x50, True)
        #time.sleep(0.08)
        time.sleep(0.08)
        high_byte = bus.read_byte_data(sensor_address, distance_high_reg, True)
        low_byte = bus.read_byte_data(sensor_address, distance_low_reg, True)
        # Combine the bytes into a single 16-bit value
        distance_raw = (high_byte << 8) + low_byte
        distance_in = float(distance_raw)
        return distance_in
    except Exception as e:
        return None

with smbus2.SMBus(i2c_bus_number) as bus:
    while True:
        for sensor in sensors:  # Loop through each sensor in the array
            distance = read_distance(bus, sensor) 
            if distance is not None:
                if 7 < distance < 84:
                    print(f"Sensor at {hex(sensor)}: {distance:.2f} inches")
                    motor(distance)
            else:
                print(f"Sensor at {hex(sensor)}: Error reading data")
            time.sleep(0.1)  # Small delay to avoid excessive bus usage
