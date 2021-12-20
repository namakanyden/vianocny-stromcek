#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import logging
from serial import Serial
from serial.serialutil import SerialException
import argparse

# create serial object
serial = Serial()

logging.basicConfig(encoding='utf-8', level=logging.INFO, format='%(asctime)s: %(message)s')
logger = logging.getLogger('mqtt2serial')


def on_message(client: mqtt.Client, userdata, msg: mqtt.MQTTMessage):
    try:
        # open serial if not open
        if not serial.isOpen():
            serial.open()

        # decode and log received message
        message = msg.payload.decode('ascii')
        logger.info(f'Received message "{message}"')

        # write message to serial port
        serial.write(message.encode('ascii'))
        serial.write(b'\r\n')
        logger.info(f'Message was written to serial port {serial.port}')
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
    parser.add_argument('--baudrate', type=int, help='baudrate', default=115200)

    args = parser.parse_args()

    try:
        # open serial port
        serial.port = args.serial
        serial.baudrate = args.baudrate
        logger.info(f'Opening port {serial.port} with baudrate {serial.baudrate}')
        serial.open()

        # connect to mqtt broker
        logger.info(f'Connecting to MQTT Broker {args.host}:{args.port}')
        client = mqtt.Client()
        client.connect(args.host, port=args.port)
        client.on_message = on_message
        client.subscribe(args.topic)

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
