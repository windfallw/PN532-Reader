import serial
import serial.tools.list_ports
import time

readonlyCard = b'\x43\xBC\x0B\x01\x02\x03\x86\x85\x03\xC7\xBD'
HF14443_find = b'\x43\xBC\x09\x02\x02\x02\x26\xBA\xB0'
HF14443_conflict = b'\x43\xBC\x08\x02\x01\x03\xAB\xB4'
HF14443_select = b'\x43\xBC\x08\x02\x01\x04\xDF\x0B'


class RFID_YES:
    port_list = []

    def __init__(self, Port, BaudRate):
        self.ser = serial.Serial(port=Port, baudrate=BaudRate, timeout=0.5)
        self.ser.close()

    def open(self):
        self.ser.open()

    def close(self):
        self.ser.close()

    def getSerial(self):
        self.port_list = list(serial.tools.list_ports.comports())

# ser.write(readonlyCard)
# s = ser.readall()
# print(s)

# ser.write(HF14443_find)
# s = ser.readall()
# print(s)
# ser.write(HF14443_conflict)
# s = ser.readall()
# print(s)
# ser.write(HF14443_select)
# s = ser.readall()
# print(s)

# ser.close()
