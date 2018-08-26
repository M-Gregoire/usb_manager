import serial
import serial.tools.list_ports

class UsbManager():
    def __init__(self, testing=False):
        if not testing:
            self.usbDevices = serial.tools.list_ports.comports()
        else:
            ser = serial.Serial()
            attrs = {"device": "tester", "vid": "1659", "pid": "8963", "serial_number": "",
                     "manufacturer":"", "product": "", "location":"", "hwid":""}
            ser.__dict__.update(attrs)
            self.usbDevices = [ser]

    def filterBy(self, device="",vid="",pid="",serial_number="",manufacturer="",product="",location="",hwid=""):
        usbDevicesTmp = list()
        for port in self.usbDevices:
            if (device in str(port.device)  and vid in str(port.vid) and pid in str(port.pid)
                and str(serial_number) in str(port.serial_number) and manufacturer in str(port.manufacturer)
                and product in str(port.product) and location in str(port.location) and hwid in str(port.hwid)):
                usbDevicesTmp.append(port)
        self.usbDevices = usbDevicesTmp
        return self

    def get(self, arg):
        usbDeviceTmp = list()
        for port in self.usbDevices:
            if arg is "device":
                usbDeviceTmp.append(port.device)
            elif arg is "vid":
                usbDeviceTmp.append(str(port.vid))
            elif arg is "pid":
                usbDeviceTmp.append(str(port.pid))
            elif arg is "serial_number":
                usbDeviceTmp.append(port.serial_number)
            elif arg is "manufacturer":
                usbDeviceTmp.append(port.manufacturer)
            elif arg is "product":
                usbDeviceTmp.append(port.product)
            elif arg is "location":
                usbDeviceTmp.append(port.location)
            elif arg is "hwid":
                usbDeviceTmp.append(port.hwid)
        return usbDeviceTmp

    def show(self):
        for port in self.usbDevices:
            print("-----------------------------------------------")
            print("Device : "+str(port.device)+" | vid/pid : "+str(port.vid)+"/"+str(port.pid))
            print("Serial_number : "+str(port.serial_number)+" | Manufacturer : "+str(port.manufacturer))
            print("Product : "+str(port.product)+"| Location : "+str(port.location))
            print("HWID : "+str(port.hwid))
            print("-----------------------------------------------\n")
        return  self

    def reset(self):
        self.usbDevices = serial.tools.list_ports.comports()
        return self
