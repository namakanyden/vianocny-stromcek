# Ovládanie stromčeka mikrokontrolérom ESP32

Riadenie stromčeka je realizované pomocou mikrokontroléra ESP32 v jazyku MicroPython.


## Zapojenie

Pre pripojenie NeoPixel svetiel sa tiež odporúča medzi mikrokontrolér a svetlá zapojiť do série malý odpor. Pri našom testovaní sme však s 330ohm odporom nevedeli NeoPixel svetlá rozsvietiť. Realizovali sme teda zapojenie bez tohto odporu.


## Inštalácia

Na realizáciu nie je potrebné sťahovať a inštalovať žiadnu ďalšiu knižnicu. Všetko potrebné je už obsiahnuté priamo v obraze MicroPython-u pre tento mikrokontrolér.

Jednotlivé súbory projektu stačí prekopírovať na mikrokontrolér ESP32.


## Konfigurácia

Konfigurácia sa nachádza v súbore `settings.py`. Význam jednotlivých možností konfigurácie je nasledovný:

-   `WIFI_NETWORKS` - Slovník, ktorý pod kľúčmi obsahuje názvy WiFi sietí a hodnotou kľúča je heslo na pripojenie do tejto siete.
-   `MQTT_BROKER` - Slovník združujúci konfiguráciu na pripojenie k MQTT brokeru. Zoznam kľúčov:
    -   `broker-ip` - IP adresa alebo URL MQTT broker-a
    -   `port` - číslo portu, na ktorom MQTT broker komunikuje
    -   `client-id` - jedinečný identifikátor klienta
    -   `topics` - zoznam tém, do ktorých sa klient pripojí
-   `WDT_TIMEOUT` - Čas (v milisekundách), ktorý po uplynutí a "nenakŕmení" strážneho psa (watchdog) zabezpečí reštartovanie mikrokontroléra. Je to vlastne ochrana v prípade výpadku siete alebo v prípade prerušenia behu programu.
-   `NEOPIXEL` - Slovník združujúci konfiguráciu svetiel NeoPixel. Zoznam kľúčov:
    -   `pin` - obsahuje číslo pin-u, ku ktorému sú svetlá pripojené
    -   `pixels` - počet svetiel

Pre vytvorenie konfiguračného súboru s vašimi nastaveniami použite šablónu `settings.tpl.py`.


# Ďalšie zdroje

-   [Firmware for Generic ESP32 module](http://micropython.org/download/esp32/) - firmvér s jazykom MicroPython pre mikrokontrolér ESP32
-   [Controlling NeoPixels](http://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html?highlight=neopixel) - Modul `neopixel` pre podporu komunikácie so svetlami NeoPixel v jazyku MicroPython
-   [`umqtt.simple`](https://github.com/micropython/micropython-lib/tree/master/umqtt.simple) - Dokumentácia k modulu `umqtt.simple`, ktorý zabezpečuje komunikáciu pomocou protokolu MQTT v jazyku MicroPython.
