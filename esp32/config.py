# this is just a template file. modify it to your needs

from machine import unique_id
import ubinascii


# wifi networks
WIFI_NETWORKS = {
    'IoTLab': 'hello.world',
    'oliver.at.home': 'Indiana.Jones',
    'chalupka' : 'u.nas.doma'
}

# configuration for connecting to MQTT broker
MQTT_BROKER = {
    'broker-ip': 'broker.hivemq.com',
    'port': 1883,
    'client-id': ubinascii.hexlify(unique_id()),
    'topics': ('namakanyden/things/stromcek',)
}

# timeout (in millis) for watchdog timer
WDT_TIMEOUT = 30 * 1000

# NeoPixel configuration
NEOPIXEL = {
    'pin': 19,    # Pin nr, where are NeoPixels connected
    'pixels': 50  # nr of neopixels
}