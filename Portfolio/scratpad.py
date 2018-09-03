import datetime

#unix time to python readable
print(datetime.datetime.fromtimestamp(int("1535140627")).strftime('%Y-%m-%d %H:%M:%S'))