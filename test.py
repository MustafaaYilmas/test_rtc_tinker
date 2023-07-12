import smbus
import time

I2C_CHANNEL = 1
DS3231_ADDRESS = 0x68
DS3231_TIME_REG = 0x00

bus = smbus.SMBus(I2C_CHANNEL)

def bcd_to_int(bcd):
    return (bcd & 0xF) + ((bcd >> 4) * 10)

def get_time():
    data = bus.read_i2c_block_data(DS3231_ADDRESS, DS3231_TIME_REG, 7)

    seconds = bcd_to_int(data[0])
    minutes = bcd_to_int(data[1])
    hours = bcd_to_int(data[2] & 0x3F)  
    day = bcd_to_int(data[4])
    month = bcd_to_int(data[5])
    year = bcd_to_int(data[6])

    print('%02d/%02d/20%02d %02d:%02d:%02d' % (day, month, year, hours, minutes, seconds))

while True:
    get_time()
    time.sleep(1)
