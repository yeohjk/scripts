#Import statement for pyserial
import serial

#Class for wind sensor ICD query and response
class icd_wind_speed:
    def __init__(self):
        self.query_hex_string = '010300000001840A'
        self.query_bytes = bytes.fromhex(self.query_hex_string)
        print(self.query_bytes)
        print(type(self.query_bytes))
        print(len(self.query_bytes))
        return
    def query_response(self):
        with serial.Serial('COM8', timeout=1) as ser:
             ser.write(self.query_bytes)
             self.response_bytes = ser.read(7)
             print(self.response_bytes)
             self.wind_speed_bytes = self.response_bytes[3:5]
             print(self.wind_speed_bytes.hex())
             self.wind_speed = int(self.wind_speed_bytes.hex(), 16)/100
             print("Wind Speed = " + str(self.wind_speed) + " m/s")
        return


query_1 = icd_wind_speed()
query_1.query_response()