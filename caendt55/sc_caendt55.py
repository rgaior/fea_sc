import sys
import os
import importlib.util
import numpy as np
import argparse
current = os.path.dirname(os.path.realpath(__file__))
from CAENpy.CAENDesktopHighVoltagePowerSupply import CAENDesktopHighVoltagePowerSupply

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)
import sc_utils
from instrument import Instrument
import interface as inter
import time
import json

ip_addresses = {'caen1':'192.168.0.250', 'caen2':'192.168.0.251'}

class CAENDT55(Instrument):
    def __init__(self,name):
        super().__init__(name)
        #        self.protocol = CAENDT55Protocol()
        
        
    def set(self, channel:int, command:str, value):
        ret_val = self.interface.set_single_channel_parameter(command,channel,value)
        logger.info(f"channel: {channel} -- setting: {command} -- value: {value}")
        return ret_val

    def poweron(self, ch):
        self.set(ch, "ON", 0)
    def poweroff(self, ch):
        self.set(ch, "OFF", 0)
        
    def clear_alarms(self):
        self.interface.query(CMD='MON', PAR='BDCLR')

    def channel_status(self,channel:int):
        status = self.interface.channel_status(channel)
        return status
    
    def read_data(self):
        list_of_command = ["VMON","VSET","VMAX","IMRANGE","IMON","ISET","POL","RUP","RDW","TRIP"]
        data_list = []
        for ch in [0,1,2,3]:
            data_dict = {}
            out_data = {}
            for key in list_of_command:
                data = self.interface.get_single_channel_parameter(parameter= key, channel=ch)
                if type(data) == str:
                    data = data.strip(';')
                if key not in ['IMRANGE','POL']:
                    data = float(data)
                out_data[key] = data
            power = self.channel_status(ch)['output']
            out_data['POWER'] = power
#            print(f"channel: {ch} --> {out_data}")
            data_dict["tags"] = {"channel":ch}
            data_dict["data"] = out_data
            data_list.append(data_dict)
        return data_list
    

    def discrete_ramp(self, ch:int, step_dict:dict):
        logger.info(f"starting a ramp on channel:{ch} with the step: {step_dict}")
        for v,t in step_dict.items():
            self.set(ch, "VSET", v)
            time.sleep(t)
    
    def discrete_ramp_array(self, ch:int, vi:float, vf:float, deltav:float, deltat:float):
        v_array = np.arange(vi, vf+0.1, deltav)
        t_array = [deltat]*len(v_array)
        ramp = dict(zip(v_array.tolist(), t_array))
        self.discrete_ramp(ch, ramp)
    
               
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display')
    parser.add_argument('name',type=str, help='either caen1 or caen2')
    args = parser.parse_args()

    name = args.name
    caenhv = CAENDT55(name)

    logger = sc_utils.get_logger(name,'/home/xenon/slowcontrol/logs/')
    logger.info(f"connecting to {name} at address {ip_addresses[name]}")
    print("ip_addresses[name] = ", ip_addresses[name])
    interface =  CAENDesktopHighVoltagePowerSupply(ip=ip_addresses[name])
    caenhv.set_interface(interface)

    caenhv.topic = 'sc/hv/'+name
    if importlib.util.find_spec('libABCD'):
        import libABCD
        libABCD.init(name)
        caenhv.start_logging(deltat=2)
               
    
