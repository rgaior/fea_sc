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
import sc_utils
import time
import json
list_of_saved_parameters = ["In1", "In2", "In3", "In4", "AIO1", "AIO2", "AIO3", "AIO4"]

class CTC100Protocol():
    def __init__(self):
        self.parameter_list = []

    
    def build_dict(self,data):
        output_dict ={}
        for key, val in zip(self.parameter_list,data):
            if key in list_of_saved_parameters:
                output_dict[key] = float(val)
        return output_dict
    

class CTC100(Instrument):
    def __init__(self,name):
        super().__init__(name)
        self.protocol = CTC100Protocol()

    def read_data(self):
#        list_of_saved_paramters = ["IN1", "IN2", "IN3", "IN4", "AIO1", "AIO2", "AIO3", "AIO4"]
        ctc100.interface.socket.sendall("getOutput\n".encode('utf-8'))
        data, client_address = ctc100.interface.socket.recvfrom(1024)
        data = data.decode('utf_8')   
        data = data.split(',')
        out_data = self.protocol.build_dict(data)
        return out_data

               
if __name__ == '__main__':
    name = "ctc100"
    ctc100 = CTC100(name)
    ip_address = '192.168.0.252'
    logger = sc_utils.get_logger(name,'/home/xenon/slowcontrol/logs/')
    logger.info(f"connecting to {name} at address {ip_address}")
    interface = inter.Ethernet("ctc100",ip = ip_address , port = 23)
    ctc100.set_interface(interface)
    ctc100.interface.socket.sendall("getOutput.names\n".encode('utf-8'))
    params,ip = ctc100.interface.socket.recvfrom(1024)
    params = params.decode('utf-8')
    params = params.replace(" ","")
    params  = params.split(',')
    ctc100.protocol.parameter_list = params    

    # doing on query because the first one is strange
    ctc100.interface.socket.sendall("getOutput\n".encode('utf-8'))
    dump,ip = ctc100.interface.socket.recvfrom(1024)
    
    ctc100.topic = 'sc/temp/ctc100'
    if importlib.util.find_spec('libABCD'):
        import libABCD
        libABCD.init(name)
        ctc100.start_logging(deltat=2)
        
