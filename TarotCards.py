from tkinter import *
from tkinter import ttk
from threading import *
import pyttsx3

# Importing required modules
from cv2 import cv2
from pyzbar.pyzbar import decode
#from warnings import filterwarnings
#from Tkinter import *
#filterwarnings('ignore')


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)
engine.setProperty('rate', 150)
# engine.say("Hello, How are you ?")
root = Tk()


count=0
data = ""
feel=""
want=""
fear=""
fordata=""
against=""
outcome=""
#tkinter stuff
def read():
    global data
        # Capture the video from default camera
    capture = cv2.VideoCapture(1)

    print("Escape Key (Esc) to exit...")
    
    recieved_data = None
    global count
    global feel, want, fear, fordata, against, outcome

    while True:
        
        # reading frame from the camera
        _,frame = capture.read()
        # Decoding the QR Code 
        decoded_data = decode(frame)

        try:
            data = decoded_data[0][0]
            if data != recieved_data:
                print(data)
                recieved_data = data
            
                
        except:
            pass
        
        # Showing video.
        cv2.imshow("QR CODE Scanner", frame)

        if(count==0): 
            feelAnsLabel.config(text=data)
            feel=data
        elif(count==1):
            wantAnsLabel.config(text=data)
            want=data
        elif(count==2):
            fearAnsLabel.config(text=data)
            fear=data
        elif(count==3):
            forAnsLabel.config(text=data)
            fordata=data
        elif(count==4):
            againstAnsLabel.config(text=data)
            against=data
        elif(count==5):
            outcomeAnsLabel.config(text=data)
            outcome=data

        #display.config(text=data)

        
        # To exit press Esc Key.
        key = cv2.waitKey(1)
        if key == 27:
            count +=1
            break


    cv2.destroyAllWindows()

def speak(str):
    engine.say(str)
    engine.runAndWait()

# def click():
#     phrase = status.get()
#     speak(phrase)

speakFeelButton = ttk.Button(root, command=lambda: speak(feel), text="Speak")
speakWantButton = ttk.Button(root, command=lambda: speak(want), text="Speak")
speakFearButton = ttk.Button(root, command=lambda: speak(fear), text="Speak")
speakForButton = ttk.Button(root, command=lambda: speak(fordata), text="Speak")
speakAgainstButton = ttk.Button(root, command=lambda: speak(against), text="Speak")
speakOutcomeButton = ttk.Button(root, command=lambda: speak(outcome), text="Speak")
#status = ttk.Entry(root)

#.grid(row=0, column=0, columnspan=4)
scanButton = ttk.Button(root, command=read, text="Scan QR Code Then hit 'esc' key to exit and display text")
display = ttk.Label(root, text="")

#labels to display each card position
feelLabel = ttk.Label(root, text="How you feel about yourself now")
wantLabel = ttk.Label(root, text="What you want at this moment")
fearLabel = ttk.Label(root, text="your fears")
forLabel = ttk.Label(root, text="What's going for you")
againstLabel = ttk.Label(root, text="What's going against you")
outcomeLabel = ttk.Label(root, text="The outcome according to your current situation of the question you asked")

feelAnsLabel = ttk.Label(root, text="")
wantAnsLabel = ttk.Label(root, text="")
fearAnsLabel = ttk.Label(root, text="")
forAnsLabel = ttk.Label(root, text="")
againstAnsLabel = ttk.Label(root, text="")
outcomeAnsLabel = ttk.Label(root, text="")

#status.grid(row=0,column=0)
display.grid(row=0,column=1)
#speakButton.grid(row=0,column=2)
scanButton.grid(row=0,column=2)

feelLabel.grid(row=1, column=0)
wantLabel.grid(row=2, column=0)
fearLabel.grid(row=3, column=0)
forLabel.grid(row=4, column=0)
againstLabel.grid(row=5, column=0)
outcomeLabel.grid(row=6, column=0)

feelAnsLabel.grid(row=1, column=1)
wantAnsLabel.grid(row=2, column=1)
fearAnsLabel.grid(row=3, column=1)
forAnsLabel.grid(row=4, column=1)
againstAnsLabel.grid(row=5, column=1)
outcomeAnsLabel.grid(row=6, column=1) 

speakFeelButton.grid(row=1, column=3)
speakWantButton.grid(row=2, column=3)
speakFearButton.grid(row=3, column=3)
speakForButton.grid(row=4, column=3)
speakAgainstButton.grid(row=5, column=3)
speakOutcomeButton.grid(row=6, column=3)
#.grid(row=0, column=0, columnspan=4)

#.grid(row=1, column=1)

root.mainloop()