import serial
import serial.tools.list_ports
import sqlite3
import time

readonlyCard = b'\x43\xBC\x0B\x01\x02\x03\x86\x85\x03\xC7\xBD'
HF14443_find = b'\x43\xBC\x09\x02\x02\x02\x26\xBA\xB0'
HF14443_conflict = b'\x43\xBC\x08\x02\x01\x03\xAB\xB4'
HF14443_select = b'\x43\xBC\x08\x02\x01\x04\xDF\x0B'


class RFID_YES:
    bd_list = ['2400', '4800', '9600', '19200', '38400', '57600', '115200']
    port_list = []
    dev_list = []

    def __init__(self, baudrate=9600, timeout=0.5):
        self.ser = serial.Serial(port=None, baudrate=baudrate, timeout=timeout)
        self.getSerial()

    def getSerial(self):
        dev = []
        self.port_list = list(serial.tools.list_ports.comports())
        for d in self.port_list:
            dev.append(d.device)
            print(d.description)
        self.dev_list = dev

    def open(self):
        print(self.ser.port, self.ser.baudrate)
        self.ser.open()

    def close(self):
        self.ser.close()

    def readOnlyCard(self):
        self.ser.write(readonlyCard)

    def HF14443(self):
        self.ser.write(HF14443_find)
        time.sleep(0.001)
        self.ser.write(HF14443_conflict)
        time.sleep(0.001)
        self.ser.write(HF14443_select)
