# usb_manager
A Python library to interact with USB devices.

# Example code

``` python
from nfc_manager import usbManager

# Show all usb devices with a vendor id of 1659
UsbManager().filterBy(vid="1659").show()

# Print the serial number of every devices with vendor id of 1659 and pid of 8963
print(UsbManager().filterBy(vid="1659", pid="8963").get("device"))
```

# Filters and getters

|Filter/Getter   |Description   |
|---|---|
|name   | Short device name, e.g. ttyUSB0.   |
|device   |Full device name/path, e.g. /dev/ttyUSB0. This is also the information returned as first element when accessed by index.   |
|hwid   |Technical description or n/a. This is also the information returned as third element when accessed by index.   |
|vid   |USB Vendor ID (0...65535).   |
|pid   |USB product ID (0...65535).   |
|serial_number   |USB serial number   |
|location   |USB device location string (“<bus>-<port>[-<port>]...”)   |
|manufacturer  |USB manufacturer string, as reported by device.   |
|product   |USB product string, as reported by device.   |

*NB*: Every filter should be passed as a string. Every getter returns a string.

# Credits

This (nano-)library is just an easy to use alias exclusivly based on [pyserial](https://pyserial.readthedocs.io/en/latest/tools.html).
