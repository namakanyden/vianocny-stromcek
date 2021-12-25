from machine import RTC


CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0


_rtc = RTC()
_format = '{hours:02}:{minutes:02}:{seconds:02} {level} {message}'
_level = INFO
_level_shortcuts = {
    50: 'C',
    40: 'E',
    30: 'W',
    20: 'I',
    10: 'D',
    0: 'N'
}


def set_level(level: int):
    if level in (CRITICAL, ERROR, WARNING, INFO, DEBUG):
        global _level
        _level = level
    else:
        raise ValueError('Log level should be one of 50, 40, 30, 20 or 10')


def log(level: int, message: str):
    global _level

    # do nothing, if message level is lower, then app level
    if level < _level:
        return
    
    # log message
    now = _rtc.datetime()
    print(_format.format(hours=now[3], minutes=now[4], seconds=now[5],
                         level=_level_shortcuts[level], message=message))
    
    
def debug(message: str):
    log(DEBUG, message)
    
    
def info(message: str):
    log(INFO, message)


def error(message: str):
    log(ERROR, message)
    
    
def warning(message: str):
    log(WARNING, message)
    
    
def critical(message: str):
    log(CRITICAL, message)
