from smbus2 import SMBus

# Define your I2C settings
i2c_bus_number = 1  # I2C bus (usually 1 on Raspberry Pi)
i2c_address = 0x70  # Replace with your device's I2C address
register_address = 0x00  # Replace with the register you want to write to
data_to_write = 0x01  # Replace with the data you want to write

# Open the I2C bus
with SMBus(1) as bus:
    # Write to the register
    bus.write_byte_data(i2c_address, register_address, 0xA0)
    bus.write_byte_data(i2c_address, register_address, 0xAA)
    bus.write_byte_data(i2c_address, register_address, 0xA5)
    bus.write_byte_data(i2c_address, register_address, 0xE4)
