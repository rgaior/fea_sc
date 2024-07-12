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
# directory reach
#directory = path.path(__file__).abspath() 
import db_utils as db_utils
import sc_utils 
import time
import json

import libABCD
libABCD.init('jsonlogger',publisher=True, listener=True, connect=True)


ctc100_topic = 'sc/temp/ctc100/get'
caen1_topic = 'sc/hv/caen1/get'
caen2_topic = 'sc/hv/caen2/get'

log_folder = '/home/xenon/slowcontrol/datalogs/'

def get_source_from_topic(topic):
    stopic = topic.split('/')
    return stopic[-2]

def logtofile(msg='', topic=''):
    source = get_source_from_topic(topic)
    fname = log_folder + sc_utils.get_file_name(source, ".json")
    with open(fname, 'a') as fp:
        json.dump(msg, fp)

    
libABCD.subscribe(ctc100_topic)
#libABCD.subscribe(caen1_topic)
#libABCD.subscribe(caen2_topic)

libABCD.add_callback(ctc100_topic, logtofile)
#libABCD.add_callback(caen1_topic, logtodb_caen)
#libABCD.add_callback(caen2_topic, logtodb_caen)
