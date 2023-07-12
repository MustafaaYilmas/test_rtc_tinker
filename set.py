import smbus
from datetime import datetime

I2C_CHANNEL = 1
DS3231_ADDRESS = 0x68
DS3231_TIME_REG = 0x00

bus = smbus.SMBus(I2C_CHANNEL)

def int_to_bcd(n):
    return (n // 10 << 4) + (n % 10)

def set_time():
    now = datetime.now()
    data = [0] * 7

    data[0] = int_to_bcd(now.second)
    data[1] = int_to_bcd(now.minute)
    data[2] = int_to_bcd(now.hour)
    data[4] = int_to_bcd(now.day)
    data[5] = int_to_bcd(now.month)
    data[6] = int_to_bcd(now.year - 2000)

    bus.write_i2c_block_data(DS3231_ADDRESS, DS3231_TIME_REG, data)

set_time()
