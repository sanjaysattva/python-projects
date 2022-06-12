from time import strftime 
from tkinter import * 

import time
import datetime
import winsound
 
root = Tk()  #creating gui object
root.title('Alarm Clock') 

def setalarm():
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}" #obtainig alarm time
    print(alarmtime)
    if(alarmtime!="::"):
        alarmclock(alarmtime) 

def alarmclock(alarmtime): 
    while True:
        time.sleep(1)
        time_now=datetime.datetime.now().strftime("%H:%M:%S") #obtaining current tie using datetime
        print(time_now) #countdown
        if time_now==alarmtime:
            Wakeup=Label(root, font = ('arial', 20, 'bold'),
            text="Wake up!Wake up!Wake up",bg="DodgerBlue2",fg="white").grid(row=6,columnspan=3) #text label
            print("wake up!")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)  #default beep sound from windows
            break


hrs=StringVar() #variable type
mins=StringVar()
secs=StringVar()

greet=Label(root, font = ('arial', 20, 'bold'),
text="Take a short nap!").grid(row=1,columnspan=3)

hrbtn=Entry(root,textvariable=hrs,width=5,font =('arial', 20, 'bold')) #input button
hrbtn.grid(row=2,column=1)

minbtn=Entry(root,textvariable=mins,
width=5,font = ('arial', 20, 'bold')).grid(row=2,column=2)

secbtn=Entry(root,textvariable=secs,
width=5,font = ('arial', 20, 'bold')).grid(row=2,column=3)

setbtn=Button(root,text="set alarm",command=setalarm,bg="DodgerBlue2",  #submit button , setalarm function called here
fg="white",font = ('arial', 20, 'bold')).grid(row=4,columnspan=3)

timeleft = Label(root,font=('arial', 20, 'bold')) 
timeleft.grid()
  
mainloop() 
