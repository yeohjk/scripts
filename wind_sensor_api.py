#Import statement for os, pyserial and time
import os
import serial
import time

#Class for wind sensor ICD query and response
class wind_speed_sensor:
    def __init__(self):
        self.antenna = '13m'
        self.query_hex_string = '010300000001840A'
        self.query_bytes = bytes.fromhex(self.query_hex_string)
        print(self.query_bytes)
        print(type(self.query_bytes))
        print(len(self.query_bytes))
        return
    #Query and Response method with time interval between measurements
    def query_response_loop(self, interval):
        while True:
            with serial.Serial('/dev/ttyUSB0', timeout=1) as ser:
                ser.write(self.query_bytes)
                self.response_bytes = ser.read(7)
                print(self.response_bytes)
                self.wind_speed_bytes = self.response_bytes[3:5]
                print(self.wind_speed_bytes.hex())
                self.wind_speed = str(int(self.wind_speed_bytes.hex(), 16)/100)
                print(f"Wind Speed = {self.wind_speed} m/s")
                #Sending data to intranet database
                command = f"curl -u  incrs:newshunli++ -s -k \"https://192.168.39.199/~incrisp/wind/input_speed.php?speed={self.wind_speed}&antenna={self.antenna}\""
                result = os.popen(command).read()
                print(result)
                time.sleep(interval)
        return

#Wind speed sensor query and response loop execution
query_1 = wind_speed_sensor()
query_1.query_response_loop(60)