import smbus
import time

# I2C kanalını belirleyin. Genellikle bu ya 1 ya da 0 olacaktır.
I2C_CHANNEL = 1

# DS3231 RTC modülünün I2C adresini belirleyin.
DS3231_ADDRESS = 0x68

# DS3231 içinde zaman bilgilerini tutan registerların adreslerini belirleyin.
DS3231_TIME_REG = 0x00

# I2C iletişimi için bir bus nesnesi oluşturun.
bus = smbus.SMBus(I2C_CHANNEL)

def bcd_to_int(bcd):
    """
    BCD (Binary-Coded Decimal) formatındaki bir sayıyı integer formatına çevirin.
    """
    return (bcd & 0xF) + ((bcd >> 4) * 10)

def get_time():
    """
    DS3231 RTC modülünden saat bilgisini okuyun ve ekrana yazdırın.
    """
    data = bus.read_i2c_block_data(DS3231_ADDRESS, DS3231_TIME_REG, 7)

    seconds = bcd_to_int(data[0])
    minutes = bcd_to_int(data[1])
    hours = bcd_to_int(data[2] & 0x3F)  # 24 saatlik format
    day = bcd_to_int(data[4])
    month = bcd_to_int(data[5])
    year = bcd_to_int(data[6])

    print(f'{day}/{month}/20{year} {hours}:{minutes}:{seconds}')

while True:
    get_time()
    time.sleep(1)  # her saniye güncellenmesi için
