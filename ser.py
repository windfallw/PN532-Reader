import serial
import serial.tools.list_ports
import time

readonlyCard = b'\x43\xBC\x0B\x01\x02\x03\x86\x85\x03\xC7\xBD'
HF14443_find = b'\x43\xBC\x09\x02\x02\x02\x26\xBA\xB0'
HF14443_conflict = b'\x43\xBC\x08\x02\x01\x03\xAB\xB4'
HF14443_select = b'\x43\xBC\x08\x02\x01\x04\xDF\x0B'


def printSerial():
    port_list = list(serial.tools.list_ports.comports())
    for dev in port_list:
        print(dev)


def openSerial():
    ser = serial.Serial('COM1', 9600, timeout=0.5)
    print(ser.name, ser.port)


printSerial()

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
