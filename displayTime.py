import datetime
import time
import os

yearGoal = 2019
monthGoal = 6
dayGoal = 4


def update():
    today = datetime.date.today()
    dt  = datetime.datetime
    now = dt.now()
    #insert the date under V here V you want to count to.
    daysAndTime = str(dt(yearGoal, monthGoal, dayGoal) - dt(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute, second=now.second)).split()

    days = daysAndTime[0]

    theThree = daysAndTime[2].split(":")

    hours = theThree[0]
    minutes = theThree[1]
    seconds = theThree[2]

    totalseconds = int(seconds) + int(minutes) * 60 + int(hours) * 60 * 60 + int(days) * 24 * 60 * 60

    totalminutes = totalseconds / 60

    totalhours = totalminutes / 60

    procentage = 100 * (1-(totalseconds/3039900))
   

    
    return "Countdown Timer created by Ulf Olsen\n¤-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-¤\nCurrent time: {}\nCurrent date: {} - {} - {}\n\nCounting down to: {} - {} - {} \n\nTimeleft: {} : {} : {} : {}\nTotal Weeks {} \nTotal Hours: {} \nTotal Minutes: {} \nTotal Seconds: {} \nPercent(From 19-04-29): {}%".format(time.strftime('%H:%M:%S',time.localtime()), today.year, today.month, today.day, yearGoal, monthGoal, dayGoal, days, hours, minutes, seconds,(((int(totalseconds)/60)/24)/7)/60 ,int(totalhours), int(totalminutes), totalseconds, procentage)

while True:
    
    x = update()
    os.system("clear")
    print(x)
    time.sleep(1)



