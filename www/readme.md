# Webové rozhranie na ovládanie stromčeka

Jednoduchá webová stránka, ktorá funguje ako webový klient pre ovládanie vianočných svetielok na diaľku.

Vhodnou úpravou ho môžete vložiť aj do vašich vlastných webových stránok alebo ho môžete spraviť súčasťou vašich webových stránok. Stránka je vytvorená pomocou webového rámca [Bootstrap](https://getbootstrap.com).

Na komunikáciu s MQTT brokerom bola použitá JavaScript-ová knižnica [Paho](https://www.eclipse.org/paho/index.php?page=clients/js/index.php). Pre nakonfigurovanie MQTT broker-a použite súbor `settings.js`.

## Inštalácia

Jedná sa o statickú webovú stránku, ktorú netreba nijako inštalovať (spustíte ju aj z vášho operačného systému otvorením súboru `index.html` vo vašom prehliadači).

Stránku preto môžete jednoducho skopírovať do vašej vlastnej webovej stránky alebo ju vhodným spôsobom upraviť a vložiť takto upravený kód do vašej webovej stránky (aby napr. lícovala s témou vašich stránok).

## Konfigurácia

Konfigurácia sa nchádza v súbore `settings.js`. Význam jednotlivých možností konfigurácie je nasledovný:

-   `mqtt` - Objekt združujúci konfiguráciu pre pripojenie k MQTT broker-u.
    -   `broker` - IP adresa alebo URL MQTT broker-a
    -   `port` - číslo portu, na ktorom MQTT broker komunikuje
    -   `clientId` - jedinečný identifikátor klienta
    -   `topic` - zoznam tém, do ktorých sa klient pripojí

*   `lights` - Zoznam obsahujúci dvojice `(x, y)`, ktoré reprezentujú stredy svetielok (guličiek) na obrázku, ktoré sa dajú rozsvecovať a zhasínať.

## Živé vysielanie

Aby bol efekt úplný, súčasťou webovej stránky je aj živé vysielanie z kamery sledujúcej stromček. Za tým účelom je potrebné vybrať vhodnú službu, ktorá stream zabezpečí. Aktuálne používame videokonferenčný systém [Jitsi](https://jitsi.org), vďaka čomu vieme dosiahnuť ovládanie stromčeka (takmer) v reálnom čase.

V prípade streamovania pomocou služieb ako YouTube musíte rátať s niekoľkosekundovým oneskorením (v prípade YouTube-u je to asi až _10s_).

## Ďalšie zdroje

-   [Eclipse Paho JavaScript Client](https://www.eclipse.org/paho/index.php?page=clients/js/index.php) - JS knižnica pre komunikáciu s MQTT.
-   [Bootstrap](https://getbootstrap.com) - webový rámec
