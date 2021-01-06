import ntptime
from machine import RTC


class Color(object):
    def __init__(self, color):
        color = color.lstrip('#')
        self.g = int(color[0:2], 16)
        self.r = int(color[2:4], 16)
        self.b = int(color[4:6], 16)
        self.value = self.g * 256 * 256 + self.b * 256 + self.r
        
    def as_tuple(self):
        return (self.g, self.b, self.r)
    
    def __str__(self):
        return 'Color {} of value {}'.format(self.as_tuple(), self.value)
    
        
def do_connect(wifis):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        networks = wlan.scan()
        for net in networks:
            ssid = net[0].decode('utf-8')
            if ssid in wifis:
                print('connecting to network "{}"...'.format(ssid))
                wlan.connect(ssid, wifis[ssid])
            
                while not wlan.isconnected():
                    pass
                ntptime.settime()
                
    print('network config:', wlan.ifconfig())
    
    return wlan


def log(message):
    rtc = RTC()
    now = rtc.datetime()
    print('{:02}:{:02}:{:02} {}'.format(now[4], now[5], now[6], message))
