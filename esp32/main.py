from machine import Pin, Timer, RTC
import ntptime
import random
import ujson
import utime
import gc
from umqtt.robust import MQTTClient

from config import WIFI_NETWORKS, MQTT_BROKER, WDT_TIMEOUT
from effects import effects, SetColorEffect
from logging import info, error
    
        
def do_connect(wifis):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        networks = wlan.scan()
        for net in networks:
            ssid = net[0].decode('utf-8')
            if ssid in wifis:
                info(f'Connecting to network "{ssid}"...')
                wlan.connect(ssid, wifis[ssid])
            
                while not wlan.isconnected():
                    utime.sleep_ms(100)
                ntptime.settime()
            else:
                raise OSError(f"Can't connect to \"{ssid}\" WiFi network. Check your configuration")
                
    info(f'Network config: {wlan.ifconfig()}')
    
    return wlan


def on_message(topic, message):
    try:
        global scenario
        
        # create dict from incomming data
        payload = ujson.loads(message.decode('utf-8'))
        info(f'Received JSON: {payload}')
        
        # find effect by it's name and run it
        name = payload['scenario']
        effect = next(filter(lambda x: x.name == name, effects))
        info(f'Running scenario {name}')
        scenario = effect.run(pixels, **payload)
        
        # cleanup
        gc.collect()
     
    # missing name of scenario
    except KeyError:
        error('Missing scenario name. Invalid JSON object?')
        error(f'Received message was: {message.decode("utf-8")}')
        
    # invalid JSON
    except ValueError:
        error('Invalid data received. Not a JSON object?')
        error(f'Received message was: {message.decode("utf-8")}')
        
    # if effect was not found
    except StopIteration:
        error(f'Unknown scenario "{name}"')

    
def wake_up(timer):
    global check_mqtt
    check_mqtt = True
    
    
def mqtt_connect():
    client = MQTTClient(MQTT_BROKER['client-id'], MQTT_BROKER['broker-ip'])
    client.set_callback(on_message)
    client.connect()
    client.keepalive = 1
    
    # subscribe to mqtt topics
    for topic in MQTT_BROKER['topics']:
        info(f'Subscribing to topic {topic}')
        client.subscribe(topic)
        
    return client


def main():
    global scenario, check_mqtt, client
    
    # show info list of all loaded effects
    names = [effect.name for effect in effects]
    info(f'Loaded {len(effects)} effects: {", ".join(names)}')
    
    # set default scenario to color
    effect = SetColorEffect()
    scenario = effect.run(pixels, color = (0, 255, 0))
    
    check_mqtt = False

    # connect to wifi
    do_connect(WIFI_NETWORKS)

    # connect to mqtt broker
    client = mqtt_connect()
        
    # set timer for periodic mqtt updates
    timer = Timer(1)
    timer.init(period=1000, mode=Timer.PERIODIC, callback=wake_up)

    # main loop
    info('Waiting for message...')

    while True:
        if check_mqtt == True:
            client.check_msg()
            check_mqtt = False
            #wdt.feed()
            
        # if scenario is not generator, then take a break
        if scenario is None:
            utime.sleep_ms(400)
        else:
            next(scenario)
        
    
if __name__ == '__main__':
    main()
