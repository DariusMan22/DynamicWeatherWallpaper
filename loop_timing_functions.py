from threading import Thread
from time import sleep

def call_at_interval(period, callback, args):
    while True:
        sleep(period)
        callback(*args)

def setInterval(period, callback, *args):
    """Use to set a periodic time interval in which I call the weather API"""
    
    Thread(target=call_at_interval, args=(period, callback, args)).start()
    
