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
import time


import libABCD
libABCD.init('dblogger',publisher=True, listener=True, connect=True)


ctc100_topic = 'sc/temp/ctc100/get'
caen1_topic = 'sc/hv/caen1/get'
caen2_topic = 'sc/hv/caen2/get'

measurement = 'test_meas4'
run_name = 'continuous_run'
def get_source_from_topic(topic):
    stopic = topic.split('/')
    return stopic[-2]

def logtodb(msg='', topic=''):
    time = int(msg['timestamp']*1e9)
    tags = {}
    tags['run'] = run_name
    source = get_source_from_topic(topic)
    tags['source'] = source
    db_utils.push_to_influx(measurement, time, msg['payload'], tags=tags)

def logtodb_caen(msg='', topic=''):
    time = int(msg['timestamp']*1e9) 
    tags = {}
    source =  get_source_from_topic(topic)
    for l in msg['payload']:
        tags = l['tags']
        tags['run'] = run_name
        tags['source'] = source
        print('tags =' , tags)
        print('l[data]', l['data'])
        db_utils.push_to_influx(measurement,time,l['data'],tags=tags)
        
        

    
libABCD.subscribe(ctc100_topic)
libABCD.subscribe(caen1_topic)
libABCD.subscribe(caen2_topic)

libABCD.add_callback(ctc100_topic, logtodb)
libABCD.add_callback(caen1_topic, logtodb_caen)
libABCD.add_callback(caen2_topic, logtodb_caen)



