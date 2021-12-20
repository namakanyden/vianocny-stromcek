#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import logging
from serial import Serial
from serial.serialutil import SerialException
import argparse
from time import sleep

# create serial object
serial = Serial()
serial.baudrate = 9600
#
# device.open()
# data = bytearray('hello world\n', 'utf-8')
# device.write(data)
# xxx = device.read()
# print(xxx)
# device.close()
# print('closed')


logging.basicConfig(encoding='utf-8', level=logging.DEBUG, format='%(asctime)s: %(message)s')
logger = logging.getLogger('mqtt2serial')


def on_message(client: mqtt.Client, userdata, msg: mqtt.MQTTMessage):
    try:
        # open serial if not open
        if not serial.isOpen():
            serial.open()

        # decode and log received message
        message = msg.payload.decode('utf-8')
        logger.debug(f'received "{message}"')

        # write message to serial port
        serial.write(msg.payload)
        logger.info(f'Message was written to {serial.port}')
        serial.close()

    except Exception as ex:
        logger.exception(ex)
        return


def main():
    parser = argparse.ArgumentParser(description='Receives the data from MQTT broker and passes them directly to the '
                                                 'serial port.',
                                     prog='mqtt2serial', epilog='Created by (c)2021 mirek@namakanyden.sk')
    parser.add_argument('--port', type=int, default=1883,
                        help='MQTT broker port')
    parser.add_argument('--host', type=str, default='broker.hivemq.com',
                        help='address of MQTT broker')

    parser.add_argument('--topic', type=str, default='namakanyden/things/stromcek',
                        help='name of the topic where to listen')
    parser.add_argument('--serial', type=str, help='serial port', required=True)

    args = parser.parse_args()

    try:
        # open serial port
        serial.port = args.serial
        serial.open()

        while True:
            data = bytearray('hello world\n', 'utf-8')
            serial.write(data)
            print('.', end='')
            sleep(5)

        # connect to mqtt broker
        logger.info(f'Connecting to MQTT Broker {args.host}:{args.port}')
        client = mqtt.Client()
        client.connect(args.host, port=args.port)
        client.on_message = on_message
        client.subscribe(args.topic)
        logger.info('connected')

        # loop
        client.loop_forever()

    # wrong serial port
    except SerialException:
        logger.error("Given port doesn't exist.")
        quit(1)

    # wrong mqtt broker port - timeout error
    except TimeoutError:
        logger.error("Can't connect to MQTT broker. Timeout.")
        quit(1)

    # other errors
    except Exception as ex:
        logger.error("Unknown error occured. Can't continue.")
        logger.exception(ex)
        quit(1)


if __name__ == '__main__':
    main()