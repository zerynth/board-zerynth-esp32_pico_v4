from espressif.esp32net import esp32eth as drv
import eth

def init():
    drv.auto_init()
    return drv

def interface():
    return eth






