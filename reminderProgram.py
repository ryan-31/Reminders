import time 
from win10toast import ToastNotifier

def createRem():
    month = input("Enter the Month in Numerical Terms (e.g. for January, enter 01 For November, enter 11):")
    day = input("Enter the Day of the reminder (e.g. 12):")
    rem = input("Enter the reminder:")
    fullRem = month+day + " " + rem
    with open('reminders.txt', mode = 'w') as f:
        f.write('\n'+fullRem+'\n')
    print("Reminder Created: "+rem)
 

def checkRem():
    date = time.strftime('%m%d')
    remFile = open('reminders.txt', 'r')
    global remToday
    remToday = 0
    rems = 0
    for line in remFile:
        if date in line:
            remToday=+1
            line = line.split(' ')
            rems = 1
            remToday = str(remToday)
            toaster = ToastNotifier()
            toaster.show_toast("Today's Reminders", "You have "+remToday+" reminders today: "+line[1])
    if rems == 0:
        toaster = ToastNotifier()
        toaster.show_toast("All Clear!", "You have no reminders today.")   

checkRem()
remToday = str(remToday)
print("You have " + remToday +" new reminders today.")

choice = int(input("Press (1) to create a new reminder"))

if choice == 1:
    createRem()


