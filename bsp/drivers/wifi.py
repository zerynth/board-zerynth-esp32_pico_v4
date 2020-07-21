from espressif.esp32net import esp32wifi as drv
from wireless import wifi as wifidrv

def init():
    drv.auto_init()
    return drv

def interface():
    return wifidrv


