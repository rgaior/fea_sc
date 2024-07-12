import sys
import os
import importlib.util
current = os.path.dirname(os.path.realpath(__file__))
import csv 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)
# directory reach
#directory = path.path(__file__).abspath() 
import db_utils as db_utils
import sc_utils 
import time
import json
import datetime
import libABCD
libABCD.init('csvlogger',publisher=True, listener=True, connect=True)


ctc100_topic = 'sc/temp/ctc100/get'
caen1_topic = 'sc/hv/caen1/get'
caen2_topic = 'sc/hv/caen2/get'

log_folder = '/home/xenon/slowcontrol/datalogs/'

def get_source_from_topic(topic):
    stopic = topic.split('/')
    return stopic[-2]

def logtofile(msg='', topic=''):
    source = get_source_from_topic(topic)
    fname = log_folder + sc_utils.get_file_name(source, ".csv")
    newfile = False
    if not os.path.isfile(fname):
        newfile = True
    
    time = msg['timestamp']
    date = time
    if 'caen' in source :
        params = sc_utils.get_parameters(msg,'caen')
        msg_str = sc_utils.convert_to_csv(msg,'caen')
        params.insert(0, 'ch')
        params.insert(0, 'timestamp')
        with open(fname,"a") as f:
            writer = csv.writer(f,delimiter=",")
            if newfile:
                writer.writerow(params)
            for ch, data_array in msg_str.items():
                data_array.insert(0,ch)
                data_array.insert(0,date)
                writer.writerow(data_array)
    else:
        params = sc_utils.get_parameters(msg)
        msg_str = sc_utils.convert_to_csv(msg)
        params.insert(0, 'timestamp')
        with open(fname,"a") as f:
            writer = csv.writer(f,delimiter=",")
            if newfile:
                writer.writerow(params)
            msg_str.insert(0, date)
            writer.writerow(msg_str)
    

    
libABCD.subscribe(ctc100_topic)
libABCD.subscribe(caen1_topic)
libABCD.subscribe(caen2_topic)

libABCD.add_callback(ctc100_topic, logtofile)
libABCD.add_callback(caen1_topic, logtofile)
libABCD.add_callback(caen2_topic, logtofile)
