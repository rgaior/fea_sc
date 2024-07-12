import influxdb_client
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import datetime
#from backports.zoneinfo import ZoneInfo

#import pytz
bucket = "FEA_SC"
org = "IPMU"
token = "u0aOHcX1oQHJUg69ucy9iWnStCeNBuuC_S-3BMtKkWH7B9pjWhf-nw3hgvpnVHuvekZqWO_I_-eNlZGWR7ggyg=="
# Store the URL of your InfluxDB instance
url="http://localhost:8086"


client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
    org=org
)

write_api = client.write_api(write_options=SYNCHRONOUS)   

def push_to_influx(measurement, time, data_dict,tags={}):
#    date = datetime.datetime.fromtimestamp(time/1e9)
#    jp = ZoneInfo('Asia/Tokyo')
#    date_log = date.replace(tzinfo= jp)
#    date_log=date_log.astimezone(tz=pytz.timezone('UTC'))
#    print(date_log)

    to_push = {"measurement":measurement,
               "tags":tags,
               "fields":data_dict,
               "time": time
               }
    # print("measurement", measurement)
    # to_push = {"measurement":measurement,
    #            "tags":{"channel":0},
    #            "fields":data_dict,
    #            "time": datetime.datetime.now()
    #            }
    
    point = Point.from_dict(to_push)
    write_api.write(bucket=bucket, record=point)
    
