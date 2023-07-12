import smbus

I2C_CHANNEL = 1

bus = smbus.SMBus(I2C_CHANNEL)

def scan_i2c_bus():
    print('Scanning I2C bus...')
    
    for address in range(0x03, 0x77):
        try:
            bus.read_byte(address)
            print(f'Device found at address: 0x{address:02x}')
        except:
            pass

scan_i2c_bus()
