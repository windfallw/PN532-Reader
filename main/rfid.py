import serial.tools.list_ports
import serial


class RFID:
    pn532_wake = b'\x55\x55\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x03\xfd\xd4\x14\x01\x17\x00'
    pn532_res_wake = b'\x00\x00\xff\x00\xff\x00\x00\x00\xff\x02\xfe\xd5\x15\x16\x00'
    pn532_find = b'\x00\x00\xff\x04\xfc\xd4\x4a\x01\x00\xe1\x00'

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
        if self.ser.isOpen():
            return False
        else:
            try:
                self.ser.open()
            except Exception as e:
                print('error:', e)
                return False
            return True

    def close(self):
        self.ser.close()

    def pn532WakeUp(self):
        self.ser.write(self.pn532_wake)

    def pn532find(self):
        self.ser.write(self.pn532_find)
