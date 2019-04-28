import datetime
import time
import os

def update():
    today = datetime.date.today()
    dt  = datetime.datetime
    now = dt.now()
    #insert the date under V here V you want to count to.
    daysAndTime = str(dt(2019, 6, 4) - dt(year=now.year, month=now.month, day=now.day, minute=now.minute, second=now.second)).split()

    days = daysAndTime[0]

    theThree = daysAndTime[2].split(":")

    hours = theThree[0]
    minutes = theThree[1]
    seconds = theThree[2]

    totalseconds = int(seconds) + int(minutes) * 60 + int(hours) * 60 * 60 + int(days) * 24 * 60 * 60

    totalminutes = totalseconds / 60

    totalhours = totalminutes / 60
    

    
    return "Countdown Timer created by Ulf Olsen\n¤-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-¤\n \nCurrent time: {}\n\nCounting down to 2019 - 6 - 4\nCurrent date: {} - {} - {} \n\nTimeleft: {} : {} : {} : {}\nTotal Weeks {} \nTotal Hours: {} \nTotal Minutes: {} \nTotal Seconds: {}".format(time.strftime('%H:%M:%S',time.localtime()), today.year, today.month, today.day, days, hours, minutes, seconds,(((int(totalseconds)/60)/24)/7)/60 ,int(totalhours), int(totalminutes), totalseconds)

while True:
    
    x = update()
    os.system("clear")
    print(x)
    time.sleep(1)



