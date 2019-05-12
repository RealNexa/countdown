import datetime
import time
import os

#insert the date under you want to count to.
yearGoal = 2019 #Year
monthGoal = 6   #Month
dayGoal = 4     #Day
hourGoal = 0   #Hour
minuteGoal = 0 #Minute
secondGoal = 0   #Second

startup = True

first  = datetime.datetime
fnow = first.now()

def update():
    isDay = False
    today = datetime.date.today()
    dt  = datetime.datetime
    now = dt.now()

    daysAndTime = str(dt(yearGoal, monthGoal, dayGoal, hourGoal, minuteGoal, secondGoal) - dt(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute, second=now.second))

    if "day" in daysAndTime:
        days = daysAndTime.split()[0]
        hours = daysAndTime.split()[2].split(":")[0]
        minutes = daysAndTime.split()[2].split(":")[1]
        seconds = daysAndTime.split()[2].split(":")[2]
    else: 
        days = 0
        hours = daysAndTime.split(":")[0]
        minutes = daysAndTime.split(":")[1]
        seconds = daysAndTime.split(":")[2]
        
    totalseconds = int(seconds) + int(minutes) * 60 + int(hours) * 60 * 60 + int(days) * 24 * 60 * 60
    
    if startup:
        return totalseconds

    totalminutes = totalseconds / 60

    totalhours = totalminutes / 60

    procentage = 100 * (1-(totalseconds/startValue))


    return "Date: " + str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) + "\nCounting to: " + str(yearGoal) + "-" + str(monthGoal) + "-" + str(dayGoal) + " " + str(hourGoal).zfill(2) + ":" + str(minuteGoal).zfill(2) + ":" + str(secondGoal).zfill(2) + "\n\nTime Left: " + str(days) + ":" + str(hours) + ":" + str(minutes) + ":" + str(seconds) + "\nWeeks Left: " + str((((int(totalseconds)/60)/24)/7)/60) + "\nTotal Hours: " + str(int(totalhours)) + "\nTotal Minutes: " + str(int(totalminutes)) + "\nTotal Seconds: " + str(int(totalseconds)) + "\n\nPercent" + "(" + str(fnow.year) + "-" + str(fnow.month) + "-" + str(fnow.day) + "): \n" + str(procentage) + "%"


    
while True:
    if startup:
        startValue = update()
        startup = False
    os.system("clear")
    print(update())
    time.sleep(1)
    

