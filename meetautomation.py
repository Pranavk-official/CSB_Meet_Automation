import webbrowser #openwebbrowser
from datetime import datetime
import time
import pyautogui #controls keyboard and mouse



#Out of class hours- code---------------------------------------------------------------------

def noclasstime():
	now=datetime.now()
	if now.strftime("%H%M%S")<"085500" or now.strftime("%H%M%S")>"120000":
		print("There are no class at this time. Please start the bot after 08:55 AM")
		time.sleep(5)
		quit()


#Out of class code end-------------------------------------------------------------------------

#Idle time code-------------------------------------------------------------------------

def idletime():
	join() #Supposed to be after meet links! But this serves the purpose!
	print("Program going idle until next class")
	time.sleep(1320)
	print("Injecting auto exit-code with delimiter as 37 (if atleast 37 participants leave the meet you will also leave")
	pyautogui.hotkey('ctrl','shift','j')
	# Js code will check for the no of participants every 5 sec.
	injection = """
		setInterval( () => {
			if(parseInt(document.getElementsByClassName("wnPUne")[0].innerHTML) < 30)
				console.log("exiting meet");
				document.getElementsByClassName("U26fgb")[2].click();
			}, 5000);
	"""
	pyautogui.write(injection)
	pyautogui.hotkey("enter")
	pyautogui.hotkey('ctrl','shift','j')
	time.sleep(1320)
	print("This class has ended checking for availability of next class")
	lineseprator()
	return


#Print Line to seprate code-------------------------------------------------------------------------
def lineseprator():
	print("------------------------------------------------------------------")

#Print Line to seprate code-------------------------------------------------------------------------
def endclass():
	print("Classes have ended for today.Have a good day")
	quit()


# Join Class Code-------------------------------------------------------------------------

def join():
	time.sleep(10)
	pyautogui.hotkey('ctrl','d') #mutes mic
	pyautogui.hotkey('ctrl','e') #Camera Off
	joinnowbutton()#Activates and Clicks the join now button.joinnowbutton() function is below this

def joinnowbutton():
    time.sleep(2)   
    pyautogui.hotkey('ctrl','shift','j')
    time.sleep(2)
    classid='document.getElementsByClassName("l4V7wb Fxmcue")[0].click()'	
    pyautogui.write(classid)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrl','shift','j')

# SUbjects and Subject Code-------------------------------------------------------------------
def co():
	linkco="https://meet.google.com/lookup/aolfeufjmu?authuser="+str(authuser)
	webbrowser.open_new(linkco)
	print("Entering Computer Organization and Architecture By Neethurose Ma'am")
	idletime()

def dbms():
	linkco="https://meet.google.com/lookup/azgifmyjyd?authuser="+str(authuser)
	webbrowser.open_new(linkco)
	print("Entering Database Management System By Bineesh Sir")
	idletime()

def gt():
	linkco="https://meet.google.com/lookup/e3tiprllzc?authuser="+str(authuser)
	webbrowser.open_new(linkco)
	print("Entering Graph Theory By Mr.Rich K J")
	idletime()

def de():
	linkco="https://meet.google.com/lookup/ffstfa2lcp?authuser="+str(authuser)
	webbrowser.open_new(linkco)
	print("Entering Design Engineering By Aswathy Ma'am")
	idletime()

def os():
	linkco="https://meet.google.com/lookup/dhm4f26j4d?authuser="+str(authuser)
	webbrowser.open_new(linkco)
	print("Entering Operating System Design By Reshma Ma'am")
	idletime()

def coi():
	linkco="https://meet.google.com/lookup/fjjbq3u2lk?authuser="+str(authuser)
	webbrowser.open_new(linkco)
	print("Entering Constitution of India by Ms.Shamin E Varkey")
	idletime()




#The time function in timetable---------------------------------------
def classtime(hr1,hr2,hr3,hr4):
	now=datetime.now()
	noclasstime()
	if "085501"<now.strftime("%H%M%S")<"125000":
		while True:
			now=datetime.now()
			#hour1
			if "090000"<=now.strftime("%H%M%S")<"090500":
				#print(datetime.today().weekday()+" - Hour 1")
				hr1()
			#hour2
			if "100000"<=now.strftime("%H%M%S")<"100500":
				#print(datetime.today().weekday()+" - Hour 2")
				hr2()
			#break
			if now.strftime("%H%M%S")=="095000" or now.strftime("%H%M%S")=="105000" or now.strftime("%H%M%S")=="115000" or now.strftime("%H%M%S")=="125000":
				print("Break for 10 min - Program idle for 10 minutes")
				print("Do not turn off the PC , if turning off, restart the program before next class")
				time.sleep(500)
			#hour3
			if "110000"<=now.strftime("%H%M%S")<"110500":
				#print(datetime.today().weekday()+" - Hour 3")
				hr3()
			#hour4
			if "120000"<=now.strftime("%H%M%S")<"120500":
				#print(datetime.today().weekday()+" - Hour 4")
				hr4()
				endclass()


# Driver programming checking time and joining class--------------------------------------	

def timetable():
	

#Monday-----------------------------------------------------------

	if(datetime.today().weekday()==0):
		classtime(dbms,co,gt,de)

#Tuesday-----------------------------------------------------------

	if(datetime.today().weekday()==1):
		classtime(os,gt,de,co)

#Wednesday-----------------------------------------------------------

	if(datetime.today().weekday()==2):
		classtime(co,os,dbms,gt)

#Thursday-----------------------------------------------------------

	if(datetime.today().weekday()==3):
		classtime(os,coi,co,dbms)

#Friday-----------------------------------------------------------

	if(datetime.today().weekday()==4):
		classtime(gt,os,dbms,coi)
#Saturday and Sunday----------------------------------------------
	else:
		print("No Classes on Saturday and Sunday")
		quit()



# Bot Banner
if __name__ == "__main__":
	print("""
 ________  ________  ________          _____ ______   _______   _______  _________   
|\   ____\|\   ____\|\   __  \        |\   _ \  _   \|\  ___ \ |\  ___ \|\___   ___\ 
\ \  \___|\ \  \___|\ \  \|\ /_       \ \  \\\__\ \  \ \   __/|\ \   __/\|___ \  \_| 
 \ \  \    \ \_____  \ \   __  \       \ \  \\|__| \  \ \  \_|/_\ \  \_|/__  \ \  \  
  \ \  \____\|____|\  \ \  \|\  \       \ \  \    \ \  \ \  \_|\ \ \  \_|\ \  \ \  \ 
   \ \_______\____\_\  \ \_______\       \ \__\    \ \__\ \_______\ \_______\  \ \__\
    \|_______|\_________\|_______|        \|__|     \|__|\|_______|\|_______|   \|__|
             \|_________|                                                            
                                                                                     
                                                                                     
 ________  ________  _________                                                       
|\   __  \|\   __  \|\___   ___\                                                     
\ \  \|\ /\ \  \|\  \|___ \  \_|                                                     
 \ \   __  \ \  \\\  \   \ \  \                                                      
  \ \  \|\  \ \  \\\  \   \ \  \                                                     
   \ \_______\ \_______\   \ \__\                                                    
    \|_______|\|_______|    \|__|                                                    
                                                                                     
                                                                                     
                                               
                                                                
 Dev:"https://github.com/TheAmalShibu"
 Contributer:"https://github.com/Pranavk-official"
 Contributer:"https://github.com/sidharthpunathil"
 Starting the bot.............. 

 ***********************************************
 This BOT is created for S4 CSB Students - JECC
 ***********************************************   
    
 Instructions
 -------------
 1. If you see multiple error messages during the bot's operation , Dont worry the bot is working fine. Bug removal is on the way.
 2. Do not engage with the meeet window while joining a new class is in progress :)
          
"""
    )
	print("Enter Authuser Count : ")
	authuser=input() #Authuser Number
	lineseprator()
	print("!!!!!! BOT IS WORKING DO NOT CLOSE THE WINDOW/TERMINAL !!!!!!! ") 
	lineseprator()
	meet=timetable()

