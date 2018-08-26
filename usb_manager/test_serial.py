from . import UsbManager

def test_serial():
    usb = UsbManager(True)
    usb.show()
    dev = usb.filterBy(vid="1659", pid="8963").get("device")
    assert dev[0] == "tester"
    usb.reset()
    dev = usb.filterBy(hwid="non-existent").get("device")
    assert dev == []
