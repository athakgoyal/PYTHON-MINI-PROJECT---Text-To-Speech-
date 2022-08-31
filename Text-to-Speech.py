# So,First start with importing libary
#In this we import tkinter for Standard GUI in python 
#gtts(google text to speech) for making text into audio file.
#playsound for playing the audio file.

from tkinter import *
from gtts import gTTS
from playsound import playsound
##############################################################

root = Tk()     #Initialising the window  
root.geometry("350x300")  #geomatry like height and width of window 
root.resizable(0,0) 
root.configure(bg='sky blue')  # configure to use the attribute of window
root.title("Text_To_Speech")   #title to the window

##############################################################
# lable is used for unchangle text(means heads or text we want to add) or unmodified text
Label(root, text = "Text_To_Speech", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="Athak Goyal", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

# lable but poistion of this is done by place() function
Label(root,text ="Enter Text", font = 'Helvetica 15 bold', bg ='white smoke').place(x=20,y=60)
Msg = StringVar()

# block where we write the text and entry is to take input from user
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)

###############################################################
# main function to convert the text file to audio or speech file
def Text_To_Speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')
    
################################################################
# for exiting form the loop
def Exit():
    root.destroy()
    
###############################################################
#for reseting the text or Msg to an empty String
def Reset():
    Msg.set("")

###############################################################
# defining the button in GUI 
# command is to call the function
Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_To_Speech ,width = '4',bg = 'green').place(x=25,y=140)

Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed').place(x=100 , y = 140)

Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)

#################################################################
# for runing the loop infinite time and calling the interface
root.mainloop()