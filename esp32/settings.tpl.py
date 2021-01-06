# this is just a template file. modify it to your needs

from machine import unique_id
import ubinascii


# wifi networks
WIFI_NETWORKS = {
    'ssid':  'password',
}

# configuration for connecting to MQTT broker
MQTT_BROKER = {
    'broker-ip': 'broker.hivemq.com',
    'port': 1883,
    'client-id': ubinascii.hexlify(unique_id()),
    'topics': ('iotlab/things/stromcek',)
}

# timeout (in millis) for watchdog timer
WDT_TIMEOUT = 30 * 1000

# NeoPixel configuration
NEOPIXEL = {
    'pin': 12,    # Pin nr, where are NeoPixels connected
    'pixels': 50  # nr of neopixels
}
