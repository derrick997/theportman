import time
import datetime

# ESTAMPA DE TIEMPO
def timestamp():
    return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) #+ "\n"

def timenow():
    return datetime.datetime.now()

def timeEightHoursAgo():
    now = datetime.datetime.now()
    if (now.hour >= 8):
        newHour = now.hour - 8
        return now.replace(hour = newHour)
    elif (now.day > 1):
        now = now - datetime.timedelta(1)
        newHour = now.hour-8+24
        return now.replace(hour=newHour)

