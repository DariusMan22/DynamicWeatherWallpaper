import threading
import time


def call_at_interval(period, callback, args):
    while True:
        time.sleep(period)
        callback(*args)


def setInterval(period, callback, *args):
    """Used to set a periodic time interval in which I call the weather API"""

    t = threading.Thread(target=call_at_interval, args=(period, callback, args))
    t.daemon = True
    t.start()

