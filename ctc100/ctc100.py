import sys
import os
import importlib.util
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)

from instrument import Instrument
import interface as inter
import time
import json

class CTC100Protocol():
    def __init__(self):
        pass
    

    def wrap_string(self,message):
        message+='\r\n'
        return message
    
    def decode_data(self, data):
        ser_bytes = data
        var = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        return var


class CTC100(Instrument):
    def __init__(self,name):
        super().__init__(name)
        self.protocol = CTC100Protocol()

    def read_data(self):
        list_of_command = ["IN1", "IN2", "IN3", "IN4", "AIO1", "AIO2", "AIO3", "AIO4"]
        out_data = {}
        for key in list_of_command:
            towrite = "".join(key) + "?\n"
            self.interface.write(towrite.encode())
            data = self.interface.readline()
            ret_val = self.protocol.decode_data(data)
            out_data[key] = ret_val
        return out_data

               
if __name__ == '__main__':
    name = "ctc100"
    ctc100 = CTC100(name)
#    interface = inter.SerialInterface("Stanford Research Systems", port = '/dev/ttyACM1', baudrate = 115200, bytesize=8, stopbits=1, timeout=2, exclusive=True)
    interface = inter.SerialInterface("Stanford Research Systems", baudrate = 115200, bytesize=8, stopbits=1, timeout=2, exclusive=True)
    ctc100.set_interface(interface)

    ctc100.topic = 'sc/temp/ctc100'
    if importlib.util.find_spec('libABCD'):
        import libABCD
        libABCD.init(name)
        ctc100.start_logging(deltat=2)
        
