from machine import unique_id
import ubinascii


# WIFI_NETS
WIFI_NETWORKS = {
    'IoTLab':  'hello.world',
    'J14P3B7': 'PlmkO098',
    'chalupka': 'u.nas.doma'
}

# MQTT_BROKER
MQTT_BROKER = {
    'broker-ip': 'broker.hivemq.com',
    'port': 1883,
    'client-id': ubinascii.hexlify(unique_id()),  #'iotlab-vianocny-stromcek',
    'topics': ('iotlab/things/stromcek',)
}

# timeout (in millis) for watchdog timer
WDT_TIMEOUT = 300 * 1000

# NeoPixel configuration
NEOPIXEL = {
    'pin': 12,    # Pin nr, where are NeoPixels connected
    'pixels': 50  # nr of neopixels
}
