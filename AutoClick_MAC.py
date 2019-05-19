import Tkinter                          #Import Tkinter module
from Tkinter import *                   #Import all Tkinter functions
import tkMessageBox as messagebox       #Allows for message to display when closing gui
from pynput.mouse import Button,Controller
import random                           #For random cursor location generation
from time import sleep                  #create delays using sleep function from time module
mouseclicks = 0                         #Show total number of mouse clicks
exitcount=0                             #Gui "quit window" activated
suspend=0
i=1
randx=randy=randclick=leftb=rightb=topb=botb=f=xcord=ycord=begin=0
#Control mouse events    
mouse = Controller()
#Gui messagebox "quit window"
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        GH.destroy()
    return suspend
#message box when user selects 'About us'
def About_Us():							    
    messagebox.showinfo("About RuneClick", "Release Version 1.0\nCopyright 2018 Austin Parkes. All rights reserved.\n") 
    return

def How_to_use():
    messagebox.showinfo("How to Use", """Select an area on your computer screen that you want the cursor to randomly click in.
Interval between clicks is 3-5 seconds at random.
    
1. Select the pixel dimensions you want in the entry boxes below
2. Your cursor's pixel location is shown below the "begin" box to help
3. Click begin when you have your dimensions selected

Hint: Pixel values increase from left to right, increase from top to bottom.""")
             
#Loop keeps gui open (EVENT LOOP!!! Gui needs an event loop to wait on widget inputs aka "Cbutton")                
def eventloop():     
      GH.mainloop()                                                 
#Obtain cursor coordinates until begin is pressed
def getcurs():
#pt is tuple - 1st element is x coord - 2nd element is y coord
    pt = mouse.position
    xcord = pt[0]
    ycord = pt[1]
#Display cursor coordinates in a label    
    Label(GH, text = ('X:',xcord,'Y:',ycord),fg = 'red').grid(row=7,column=1)        
#UPDATE cursor location every 50 ms
    GH.after(50,getcurs)                                                             
    return
#define our cursor integers we will be using to store cursor coordinates
    
#Autoclick Loop
def autoclick():
   while True:
    global randx,randy,left,right,top,bot,suspend
    global mouseclicks,randclick,i,xcord,ycord
#disable 'begin' button once it has been pressed once
    Tkinter.Button(text="Click to begin",fg="black",bg = "white",state = DISABLED).grid(row=5,column=1)
#change user entry into integer for left,right,top,bot     
    left = int(leftb.get())                             
    right = int(rightb.get())
    top = int(topb.get())
    bot = int(botb.get())   
    mouseclicks+=1
#mouse x coordinate between left and right user entry
    randx = random.randint(left,right)
#mouse y coordinate between top and bottom user entry
    randy = random.randint(top,bot)
#click in random interval from 2-5 seconds 
    randclick = random.randint(2000,6000)
#print number of times mouse clicks
    print(mouseclicks)    			        
#Set mouse position
    mouse.position = (randx,randy)
#left mouse click (pressed down and up)
    mouse.click(Button.left, 1)               
#CALLBACK to run autoclicker at same time as GUI --> FIRST ARGUMENT IN MILLISECONDS    
    GH.after(randclick,autoclick)                       
    return xcord,ycord,begin
#Main - GUI Interface 
#end loop when user exits through messagebox
while exitcount < 1: 					            
#GH is master GUI window    
    GH = Tk()                                                     
    GH.geometry("310x200+100+100")                                
    GH.iconbitmap(r'C:\Python27\DLLs\favicon.ico')
    GH.title("RuneClick")
#monitor mouse events
    getcurs()                                                     
#Menu_bar
    main_menubar = Menu(GH)					    
    GH.config(menu = main_menubar)				   	   
#'tearoff = 0' gets rid of unwanted dashed line in submenu    
    sub_menu = Menu(main_menubar, tearoff = 0)		    
    main_menubar.add_cascade(label='Help', menu=sub_menu)	    
    sub_menu.add_command(label="About Us", command = About_Us)     
    sub_menu.add_command(label="How to Use", command = How_to_use)
#GUI Text Boxes		
    Label(GH, text="Enter Dimensions Below").grid(row=0,column=1)   
    Label(GH, text="168").grid(row=1,column=2)
    Label(GH, text="245").grid(row=2,column=2)
    Label(GH, text="135").grid(row=3,column=2)
    Label(GH, text="150").grid(row=4,column=2)
    Label(GH, text="Example Below").grid(row=0,column=2)
    Label(GH, text="LeftBoundary").grid(row=1)                      
    Label(GH, text="RightBoundary").grid(row=2)                     
    Label(GH, text="TopBoundary").grid(row=3)                      
    Label(GH, text="BotBoundary").grid(row=4)                       
#Right adjusted (anchor = 'east')      
    Label(GH, text="(x , y):", anchor = 'e').grid(row=7)             
#Entry Boxes (User Input)
    leftb = Entry(GH)                                               
    rightb = Entry(GH)                                              
    topb = Entry(GH)                                               
    botb = Entry(GH)                                               
    leftb.grid(row=1,column=1)                                      
    rightb.grid(row=2,column=1)                                     
    topb.grid(row=3,column=1)                                       
    botb.grid(row=4,column=1)                                       
#Push Button Widget -> Calls 'autoclick' function
    Tkinter.Button(text="Click to begin",fg="black",bg = "white",command = autoclick).grid(row=5,column=1)
#Allow "quit window" display to open
    GH.protocol("WM_DELETE_WINDOW",on_closing)                  
#Allow "quit window" display to open
    exitcount+=1                                                     
    GH.mainloop()

#--------^End user interface (GUI)^-----------------------------------------------------------------------------------------------^

#Implemented CALLBACK feature to run GUI alongside autoclicker program -- (Alternative to threading)

#Future Implementation
        #--Add button widget that allows click and drag
	#--Add an exit option that allows user to exit program through the escape key
	#--Make program a standalone application on Mac (py2app) and Windows machines
        #--Suspend autoclicking program when "exit" messagebox appears **

    
