from base import *
from devices import *

class Esp32PicoV4(Board):

    @staticmethod
    def match(dev):
        return dev["vid"]=="10C4" and dev["pid"] in ("003D","EA60")
    

    def reset(self):
        import time
        conn = ConnectionInfo()
        conn.set_serial(self.port,**self.connection)
        ch = Channel(conn)
        try:
            ch.open(timeout=2)
        except:
            fatal("Can't open serial:",self.port)
        esp32r0_delay=True
        ch.setDTR(False)  # IO0=HIGH
        ch.setRTS(True)   # EN=LOW, chip in reset
        time.sleep(0.1)
        if esp32r0_delay:
            # Some chips are more likely to trigger the esp32r0
            # watchdog reset silicon bug if they're held with EN=LOW
            # for a longer period
            time.sleep(1.2)
        #ch.setDTR(True)   # IO0=LOW
        ch.setRTS(False)  # EN=HIGH, chip out of reset
        if esp32r0_delay:
            # Sleep longer after reset.
            # This workaround only works on revision 0 ESP32 chips,
            # it exploits a silicon bug spurious watchdog reset.
            time.sleep(0.4)  # allow watchdog reset to occur
        time.sleep(0.05)
        ch.setDTR(False)  # IO0=HIGH, done
        ch.close()
        time.sleep(0.5)

    def burn(self,bin,outfn=None):
        rom = bin[3]    #bootloader
        irom = bin[1]   #app
        brom = bin[2]   #partition
        vrom = bin[0]   #vstore
        romf = fs.get_tempfile(rom)
        iromf = fs.get_tempfile(irom)
        bromf = fs.get_tempfile(brom)
        vromf = fs.get_tempfile(vrom)
        res,out,err = proc.runcmd("python",tools["esptool32"],"--chip", "esp32","--port",self.port,"--baud","115200","--before", "default_reset", "--after", "hard_reset","write_flash","-z","--flash_freq","40m","--flash_mode","dio","--flash_size","detect","0x1000",romf, "0x10000",iromf, "0x8000", bromf,"0x390000",vromf,outfn=outfn)
        fs.del_tempfile(romf)
        fs.del_tempfile(iromf)
        fs.del_tempfile(bromf)
        fs.del_tempfile(vromf)
        if res:
            return False,out
        return True,out

    def erase(self,outfn=None):
        res,out,err = proc.runcmd("python",tools["esptool32"],"--chip", "esp32","--port",self.port,"--baud","115200","erase_flash",outfn=outfn)
        if res:
            return False,out
        return True,out

    def custom_get_chipid(self,method=0,outfn=None):
        res,out,err = proc.runcmd("python",tools["esptool32"],"--chip", "esp32","--port",self.port,"--baud","115200","--before", "default_reset", "--after", "hard_reset","read_mac",outfn=outfn)

        if res:
            return None
        lines=out.split("\n")
        for line in lines:
            if line.startswith("MAC: "):
                smac = line[5:].split(":")
                mac = ""
                for m in smac:
                    mac = mac+m[1]+m[0]
                return mac
        return None

    def custom_burn_layout(self,layout,options={},outfn=None):
        args = []
        for chunk in layout.chunks():
            args.append(hex(chunk["loc"]) if not isinstance(chunk["loc"],str) else chunk["loc"])
            tfile = fs.get_tempfile(chunk["bin"])
            args.append(tfile)
        baud = str(options.get("baud",115200))
        res,out,err = proc.runcmd("python",tools["esptool32"],"--chip", "esp32","--port",self.port,"--baud",baud,"--before", "default_reset", "--after", "hard_reset","write_flash","-z","--flash_freq","40m","--flash_mode","dio","--flash_size","detect",*args,outfn=outfn)

        for arg in args:
            # cleanup
            if not arg.startswith("0x"):
                fs.rm_file(arg)

        if res:
            return False,out
        return True,out
