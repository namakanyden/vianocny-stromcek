from machine import Pin, WDT, Timer
import random
import ujson
import utime
import gc
from umqtt.robust import MQTTClient

from settings import WIFI_NETWORKS, MQTT_BROKER, WDT_TIMEOUT
from helper import *
import effects


def on_message(topic, message):
    global scenario
    
    try:
        # decode the data
        topic = topic.decode('utf-8')
        message = message.decode('utf-8')
        
        # log message
        log('message received: "{}: {}"'.format(topic, message))
        
        # create dict and extract general data
        payload = ujson.loads(message)
        color = Color(payload.get('color', '#000000'))
        delay = int(payload.get('duration', 100))
        name = payload.get('scenario', 'clear')
        
        # play scenario
        if name == 'clear':
            scenario = effects.clear(pixels)
            
        elif name == 'rainbow':
            scenario = effects.rainbow_cycle(pixels, delay)
        
        elif name == 'set color':
            scenario = effects.set_color(pixels, color)
        
        elif name == 'bounce':
            scenario = effects.bounce(pixels, color, delay)

        elif name == 'cycle':
            scenario = effects.cycle(pixels, color, delay)
        
        elif name == 'random color':
            scenario = effects.set_random_color(pixels, delay)
        
        elif name == 'fade':
            scenario = effects.fade(pixels, color, delay)

        elif name == 'knight rider':
            scenario = effects.knight_rider(pixels, color, delay)
        
        elif name == 'part of tree':
            index = int(payload.get('index', 0))
            parts = int(payload.get('parts', 10))
            
            scenario = effects.light_up_part_of_tree(pixels, color, parts, index)
        
        else:
            log('Error: Unknown scenario "{}"'.format(name))
            return
    except Exception as ex:
        log('Error: {}'.format(ex))
        return
    finally:
        gc.collect()

    
def wake_up(timer):
    global check_mqtt
    check_mqtt = True
    
    
def mqtt_ping(timer):
    global ping_mqtt
    ping_mqtt = True
    
    
def mqtt_connect():
    client = MQTTClient(MQTT_BROKER['client-id'], MQTT_BROKER['broker-ip'])
    client.set_callback(on_message)
    client.connect()
    client.keepalive = 1
    
    # subscribe to mqtt topics
    for topic in MQTT_BROKER['topics']:
        log('subscribing to topic {}'.format(topic))
        client.subscribe(topic)
        
    return client
    
#if __name__ == '__main__':global scenario, check_mqtt, client
scenario = effects.clear(pixels)
check_mqtt = False
ping_mqtt = False

# set Watchdog first
wdt = WDT(timeout = WDT_TIMEOUT)
  
# connect to wifi
wlan = do_connect(WIFI_NETWORKS)

# connect to mqtt broker
client = mqtt_connect()
    
# set timer for periodic mqtt updates
timer = Timer(1)
timer.init(period=1000, mode=Timer.PERIODIC, callback=wake_up)

# set timer for periodic ping of mqtt server/broker
timer = Timer(2)
timer.init(period = 60 * 1000, mode=Timer.PERIODIC, callback=mqtt_ping)

# main loop
log('waiting for message...')

while True:
    if check_mqtt == True:
        client.check_msg()
        check_mqtt = False
        wdt.feed()
        
    if ping_mqtt == True:
        #log('pinging mqtt')
        client.ping()
        ping_mqtt = False
        
    if scenario is None:
        utime.sleep_ms(400)
    else:
        next(scenario)
