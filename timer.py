import time
from random import randrange

def timer(start_time, end_time):
    '''
    Timer to snooze while scraping
    Para_1: start_time: integer for minimum seconds snooze
    Para_2: end_time: integer for maximum seconds snooze
    '''
    snoozer = randrange(start_time, end_time)
    print(f"Snoozing for {snoozer} seconds!")
    time.sleep(snoozer)## set timer