import logging
import datetime
def get_source_from_topic(topic):
    stopic = topic.split('/')
    return stopic[-2]


def celsius_to_kelvin(tempC):
    return tempC + 273.15


def get_logger(name, log_folder):
    '''
    set the common logger for all the code with the common properties.
    
    '''
    now = datetime.datetime.now() # current date and time
    date_time = now.strftime("%Y_%m_%d")
    logger = logging.getLogger(name)
    log_format = "%(asctime)s  - %(name)s - %(levelname)s - %(message)s"
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(log_format)
    fh = logging.FileHandler(log_folder + "/" + name + '_'+date_time+ '.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create formatter and add it to the handlers
    ch.setFormatter(formatter)
    
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.propagate = False
    return logger


def get_file_name(prefix="", ext ='.txt'):
    # get current date and time
#    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d")
#    print("Current date & time : ", current_datetime)

    # convert datetime obj to string
    str_current_datetime = str(current_datetime)

    # create a file object along with extension
    file_name = prefix + "_" + str_current_datetime+ext

    return file_name

def get_parameters(msg, mode = None):
    if not mode:
        return list(msg['payload'].keys())
    if 'caen' in mode:
        return list(msg['payload'][0]['data'].keys())

    
def convert_to_csv(msg, mode=None):
    if not mode:
        timestamp = msg['timestamp']
        data = msg['payload']
        return list(data.values())
    if 'caen' in mode:
        out_dict = {}
        for ch in [0,1,2,3]:
            msg_ch = msg['payload'][ch]['data']
            out_dict[ch] =  list(msg_ch.values())
        return out_dict
#                msg['payload'][3]['data']
#                return 
    
        

#  "payload": {"In1": NaN, "In2": NaN, "In3": NaN, "In4": NaN, "AIO1": 0.090614, "AIO2": -0.003064, "AIO3": -275.8164, "AIO4": -0.021752}
    #         msg_ch3 = msg['payload'][3]['data']
    # device = sc_utils.get_source_from_topic(topic)

    # pad.addstr(0, 5, f"########## display of {device} ##########", curses.A_BOLD)

    # i = 1
    # # channel line:
    # pad.addstr(i, 15, "Ch0")
    # pad.addstr(i, 30, "Ch1")
    # pad.addstr(i, 45, "Ch2")
    # pad.addstr(i, 60, "Ch3")

    
    # pad.addstr(i+1, 0, "polarity")
    # for ch, ch_msg in zip([0,1,2,3], [msg_ch0,msg_ch1,msg_ch2,msg_ch3]):
    #     pad.addstr(i+1, 15+ ch*15, f"{str(ch_msg['POL'])}")

    # pad.addstr(i+2, 0, "VMON")
    # for ch, ch_msg in zip([0,1,2,3], [msg_ch0,msg_ch1,msg_ch2,msg_ch3]):

