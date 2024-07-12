import sys
import os
import importlib.util
import argparse
current = os.path.dirname(os.path.realpath(__file__))
import atexit
from datetime import datetime
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)
# directory reach
#directory = path.path(__file__).abspath() 
import time
import libABCD
import curses

libABCD.init('display',publisher=True, listener=True, connect=True)

parser = argparse.ArgumentParser(description='Display')
parser.add_argument('topic',type=str, help='MQTT Topic of the caen HV')
args = parser.parse_args()
topic = args.topic

#topic = 'sc/hv/caen/get'

    

def display(msg='', topic=topic):
    timestamp = msg['timestamp']
    msg_ch0 = msg['payload'][0]['data']
    print(msg_ch0)

libABCD.subscribe(topic)
libABCD.add_callback(topic, display)

# if __name__ == '__main__':
#     set_topic(topic)
#    display()
               
