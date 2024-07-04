import smbus2

# Define your I2C settings
i2c_bus_number = 1  # I2C bus (usually 1 on Raspberry Pi)
left = 0xE2 
right = 0xE4
back = 0xE6
command_reg = 0x00  

with SMBus(i2c_bus_number) as bus:
    