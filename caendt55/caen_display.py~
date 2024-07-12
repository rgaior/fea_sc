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
import sc_utils


libABCD.init('display',publisher=True, listener=True, connect=True)

def stop_curses():
    curses.endwin()

atexit.register(stop_curses)


stdscr = curses.initscr()
# # #curses.noecho()
curses.cbreak()
stdscr.keypad(True)

parser = argparse.ArgumentParser(description='Display')
parser.add_argument('topic',type=str, help='MQTT Topic of the caen HV')
args = parser.parse_args()
topic = args.topic




def display(msg='', topic=topic):
    #    print(msg)
    pad = curses.newpad(100, 100)
    
    timestamp = msg['timestamp']
    msg_ch0 = msg['payload'][0]['data']
    msg_ch1 = msg['payload'][1]['data']
    msg_ch2 = msg['payload'][2]['data']
    msg_ch3 = msg['payload'][3]['data']
    device = sc_utils.get_source_from_topic(topic)

    pad.addstr(0, 5, f"########## display of {device} ##########", curses.A_BOLD)

    i = 1
    # channel line:
    pad.addstr(i, 15, "Ch0")
    pad.addstr(i, 30, "Ch1")
    pad.addstr(i, 45, "Ch2")
    pad.addstr(i, 60, "Ch3")

    
    pad.addstr(i+1, 0, "polarity")
    for ch, ch_msg in zip([0,1,2,3], [msg_ch0,msg_ch1,msg_ch2,msg_ch3]):
        pad.addstr(i+1, 15+ ch*15, f"{str(ch_msg['POL'])}")

    pad.addstr(i+2, 0, "VMON")
    for ch, ch_msg in zip([0,1,2,3], [msg_ch0,msg_ch1,msg_ch2,msg_ch3]):
        pad.addstr(i+2, 15+ ch*15, f"{str(ch_msg['VMON'])} V")

    pad.addstr(i+3, 0, "IMON")
    for ch, ch_msg in zip([0,1,2,3], [msg_ch0,msg_ch1,msg_ch2,msg_ch3]):
        pad.addstr(i+3, 15+ ch*15, f"{str(ch_msg['IMON'])} uA")

    pad.addstr(i+5, 0, "VSET")
    for ch, ch_msg in zip([0,1,2,3], [msg_ch0,msg_ch1,msg_ch2,msg_ch3]):
        pad.addstr(i+5, 15+ ch*15, f"{str(ch_msg['VSET'])} V")

    pad.addstr(i+6, 0, "ISET")
    for ch, ch_msg in zip([0,1,2,3], [msg_ch0,msg_ch1,msg_ch2,msg_ch3]):
        pad.addstr(i+6, 15+ ch*15, f"{str(ch_msg['ISET'])} uA")

    pad.addstr(i+7, 0, "VMAX")
    for ch, ch_msg in zip([0,1,2,3], [msg_ch0,msg_ch1,msg_ch2,msg_ch3]):
        pad.addstr(i+7, 15+ ch*15, f"{str(ch_msg['VMAX'])}")

    pad.addstr(i+8, 0, "Ramp Up")
    for ch, ch_msg in zip([0,1,2,3], [msg_ch0,msg_ch1,msg_ch2,msg_ch3]):
        pad.addstr(i+8, 15+ ch*15, f"{str(ch_msg['RUP'])}")

    pad.addstr(i+9, 0, "Ramp Down")
    for ch, ch_msg in zip([0,1,2,3], [msg_ch0,msg_ch1,msg_ch2,msg_ch3]):
        pad.addstr(i+9, 15+ ch*15, f"{str(ch_msg['RDW'])}")

    pad.addstr(i+10, 0, "Trip")
    for ch, ch_msg in zip([0,1,2,3], [msg_ch0,msg_ch1,msg_ch2,msg_ch3]):
        pad.addstr(i+10, 15+ ch*15, f"{str(ch_msg['TRIP'])}")

    pad.addstr(i+11, 0, "IMON Range")
    for ch, ch_msg in zip([0,1,2,3], [msg_ch0,msg_ch1,msg_ch2,msg_ch3]):
        pad.addstr(i+11, 15+ ch*15, f"{str(ch_msg['IMRANGE'])}")

    pad.addstr(i+15, 0, "POWER",curses.A_BOLD)
    for ch, ch_msg in zip([0,1,2,3], [msg_ch0,msg_ch1,msg_ch2,msg_ch3]):
        pad.addstr(i+15, 15+ ch*15, f"{str(ch_msg['POWER'])}",curses.A_BOLD)

    last_data = datetime.fromtimestamp(timestamp)
    pad.addstr(i+17, 0, f"last sampled point: {last_data.strftime('%Y-%m-%d %H:%M:%S')} ", curses.A_BLINK)
        
        #        pad.addstr(1, 30, f"{msg_ch1['POL'][:-1]}",curses.A_BLINK)
#    pad.addstr(1, 45, f"{msg_ch2['POL'][:-1]}",curses.A_BLINK)
#    pad.addstr(1, 60, f"{msg_ch3['POL'][:-1]}",curses.A_BLINK)

     
    pad.refresh( 0,0, 5,5, 25,100)
    #    curses.endwin()
    
#def set_topic(topic):

libABCD.subscribe(topic)
libABCD.add_callback(topic, display)

# if __name__ == '__main__':
#     set_topic(topic)
#    display()
               
