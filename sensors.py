import smbus2
import time
from motors import motor

i2c_bus_number = 1  
left = 0x70
right = 0xE4
back = 0xE6
sensors = [left, right, back]
command_reg = 0x00  
distance_high_reg = 0x02  # High byte of the distance result
distance_low_reg = 0x03  # Low byte of the distance result

def read_distance(bus, sensor_address):
    try:
        # Write the command to initiate ranging in inches
        bus.write_byte_data(sensor_address, command_reg, 0x50)
        time.sleep(0.100)
        high_byte = bus.read_byte_data(sensor_address, distance_high_reg)
        low_byte = bus.read_byte_data(sensor_address, distance_low_reg)
        print(f"{hex(high_byte)}: {hex(low_byte)}")
        # Combine the bytes into a single 16-bit value
        distance_raw = (high_byte << 8) + low_byte
        distance_in = float(distance_raw)
        return distance_in
    except Exception as e:
        print(f"Error reading from sensor at address {hex(sensor_address)}: {e}")
        return None

with smbus2.SMBus(i2c_bus_number) as bus:
    while True:
        distance = read_distance(bus, left) 
 #       if distance < 84:
        print(f"Sensor at {hex(left)}: {distance:.2f} inches")
#            motor(distance)
        if distance is not None:
            #print(f"Sensor at {hex(left)}: {distance:.2f} inches")
            continue
        else:
            print(f"Sensor at {hex(left)}: Error reading data")
        # time.sleep(.001 ) 
