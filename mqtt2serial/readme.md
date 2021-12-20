# MQTT2Serial

Jednoduchý nástroj, pomocou ktorého je možné preposielať správy prijaté z MQTT brokera cez sériovú linku do vášho
mikrokontroléra. Použitie je ideálne pre mikrokontroléry, ktoré nie sú vybavené WiFi alebo ethernetovým modulom (napr.
_Arduino UNO_, _Raspberry Pi Pico_, _BBC Micro:bit_ a iné).


## Inštalácia

Projekt používa pre zjednodušenie práce nástroj [Poetry](https://python-poetry.org/). Pre inštaláciu všetkých potrebných
závislostí tým pádom stačí z príkazového riadku spustiť príkaz:

```bash
$ poetry install
```


## Použitie

Nástroj je primárne určený pre projekt _Namakaný vianočný stromček_, ale môžete ho použiť bez problémov aj na iné
vlastné projekty. Príkaz má niekoľko voliteľných parametrov:

* `--host` - adresa MQTT broker-a, predvolená hodnota: `broker.hivemq.com`
* `--port` - port MQTT broker-a, predvolená hodnota: `1883`
* `--topic` - téma, na ktorej odber sa v rámci nástroja prihlasujeme, predvolená hodnota: `namakanyden/things/stromcek`
* `--baudrate` - rýchlosť prenosu údajov na sériovej linke: predvolená hodnota: `115200`
* `--serial` - sériová linka, povinný parameter, pre Linux napr. `/dev/ttyUSB0`, pre Windows napr. `COM7`

Použitie príkazu pomocou nástroja [Poetry](https://python-poetry.org/) môže vyzerať nasledovne:

```bash
$ poetry run app --serial /dev/ttyUSB0
```

Ak je skript `mqtt2serial` spustiteľný, bude jeho použitie vyzerať nasledovne:

```bash
$ mqtt2serial --serial /dev/ttyUSB0
```


## Tvorba vlastných klientov

Ak vytvárate vlastný klientsky program, pre čítanie zo sériovej linky môžete využiť nasledovné fragmenty kódov.


### Arduino SDK

Ak chcete čítať správy zo sériovej linky na mikrokontroléroch _Arduino_, resp. na mikrokontroléroch, ktoré je možné
programovať pomocou _Arduino SDK_, môžete použiť nasledujúci fragment kódu:

```cpp
int main() {
    // setup
    String message;
    Serial.begin(9600);

    // superloop
    for(;;){
        if(Serial.available()){
            message = Serial.readString();
            Serial.println(message);
        }
    }  
}
```


### MicroPython

Ak chcete čítať správy zo sériovej linky na mikrokontroléroch, do ktorých je možné nahrať
jazyk [MicroPython](http://micropython.org/) (napr. _ESP32_, _BBC Micro:bit_, _Raspberry Pi Pico_ a iné), môžete použiť
nasledujúci fragment kódu:

```python
while True:
    print('>> waiting...')
    data = input()
    print('Received: ' + data)
```


## Poďakovanie

Do ladenia a testovania nástroja sa aktívne zapojil aj _Marek Pohančeník_.
