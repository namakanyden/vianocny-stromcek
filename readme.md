# Vianočný stromček

Vianočný stromček ovládaný na diaľku pomocou _IoT_ protokolu _MQTT_.

Riadenie stromčeka je realizované pomocou mikrokontroléra _ESP32_, ku ktorému sú pripojené svetielka _NeoPixel_. Používatelia môžu stromček ovládať pomocou webovej stránky, na ktorej vidia stromček prostredníctvom živého vysielania. Samotná komunikácia medzi webovou stránkou a mikrokontrolérom je realizovaná pomocou MQTT protokolu.

Poznámka: Nie je problém vytvoriť podobnú realizáciu pomocou iných mikrokontrolérov alebo priamo pomocou Raspberry Pi a to aj v inom jazyku ako je Python. Pre fungovanie je dôležité zachovať len formát správ a rovnaký MQTT broker.

## Prevedenie

Projekt sa skladá zo štyroch častí:

-   zo stromčeka,
-   MQTT broker-a,
-   z webovej stránky, a
-   zo živého vysielania.

### MQTT broker

MQTT broker funguje ako prostredník pre komunikáciu medzi webovým klientom a mikrokontrolérom ovládajúcim stromček. Týmto spôsobom je možné stromček umiestniť aj do domácej siete a vďaka MQTT brokeru bude ovládateľný z ľubovoľného miesta na svete.

Ako MQTT broker môžete použiť napr. verejný [HiveMQ](https://www.hivemq.com/public-mqtt-broker/) alebo [Eclipse Mosquitto](https://mosquitto.org), ktorý je dostupný v repozitároch štandardných linuxových distribúcií, ako aj na [Raspberry OS](https://www.raspberrypi.org/software/).

## Štruktúra projektu

-   `esp32/` - zdrojové kódy v jazyku MicroPython pre mikrokontrolér ESP32
-   `www/` - zdrojové kódy webovej stránky na ovládanie stromčeka na diaľku

## Zdroje

-   [prezentácia](https://youtu.be/AaIelMubuP8) z [webinára Namakaného dňa](http://www.namakanyden.sk/webinare/2020/12/20/vianocne-svetielka.html)
-   [videozáznam](https://youtu.be/AaIelMubuP8) z webinára
-   [HiveMQ](https://www.hivemq.com/public-mqtt-broker/) - verejný MQTT broker
-   [Eclipse Mosquitto](https://mosquitto.org) - otvorený MQTT broker
