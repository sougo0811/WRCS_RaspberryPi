import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
while True:
    water_high_data = ser.read_all()
    print(water_high_data)
ser.close()