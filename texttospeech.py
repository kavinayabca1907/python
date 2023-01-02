from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pyttsx3

sapi =pyttsx3.init()
rate = sapi.getProperty('rate')
sapi.setProperty('rate', 125)

class TextToSpeech:

    def __init__(self,root):
        self.root =root
        blank_space = " "
        self.root.title(202 * blank_space + "Phyton Text to speech")
        self.root.resizable(width =False, height=False)
        self.root.geometry("1360x700+0+0")

        MainFrame = Frame(self.root, bd=10, width = 1350, height = 700, relief=RIDGE, bg="cadetblue")
        MainFrame.grid()
        TitleFrames = Frame(MainFrame, bd=7, width = 1320, height = 100, relief=RIDGE)
        TitleFrames.grid(row=0,column =0)

        TitleFrames = Frame(TitleFrames, bd=7, width = 1320, height = 100,padx=180, relief=RIDGE, bg="cadetblue")
        TitleFrames.grid(row=0,column =0, padx=8)

        TextFrame = Frame(MainFrame, bd=10, width = 1340, height = 480, relief=RIDGE, bg="cadetblue")
        TextFrame.grid(row=1,column =0)

        LeftFrame = Frame(TextFrame, bd=10, width = 1000, height = 480, relief=RIDGE)
        LeftFrame.grid(row=0,column =0)

        ButtonFrame = Frame(TextFrame, bd=10, width = 320, height = 480, relief=RIDGE)
        ButtonFrame.grid(row=0,column =1)

        #=============================================================================================
        self.lblTitle=Label(TitleFrames,font=('arial', 50, 'bold'),text= "Text To Speech", bd=7,bg="cadetblue")
        self.lblTitle.grid(row=0 ,column=0, padx=222)
        #=============================================================================================
        def TextSapi():
            TextInput = txtEnterText.get("1.0", "end-1c")
            sapi.say(TextInput)
            sapi.runAndWait()
        def ChangeVoice():
            TextInput = txtEnterText.get("1.0", "end-1c")
            voices = sapi.getProperty('voices')
            for voice in voices:
                sapi.setProperty('voice', voice.id)
                sapi.say(TextInput)
            sapi.runAndWait()
        def SpeechRate():
            sapi.say("Hello Everyone!")
            sapi.say('My current speaking rate is' + str(rate))
            sapi.runAndWait()
            sapi.stop()
        def iExit():
            sapi.say('Confirm if you want to exit')
            sapi.runAndWait()
            iExit = tkinter.messagebox.askyesno("Text to Speech", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        #=============================================================================================
        txtEnterText = Text(LeftFrame, height =8, width=30,
                            bg="yellow",font=('Courier', 40, 'bold') )
        txtEnterText.grid(row =0, column=0)
        #=============================================================================================
        self.btnReadText=Button(ButtonFrame, pady=1, bd=4, font=('arial', 30, 'bold'), padx=25, width=11, height=2
            , text="Read Text", command = TextSapi).grid(row=0,column=0, padx=2)

        self.btnSpeechRate=Button(ButtonFrame, pady=1, bd=4, font=('arial', 30, 'bold'), padx=25, width=11, height=2
        , text="SpeechRate",command=SpeechRate).grid(row=1,column=0, padx=2)

        self.btnChangeVoice=Button(ButtonFrame, pady=1, bd=4, font=('arial', 30, 'bold'), padx=25, width=11, height=2
        , text="Change Voice",command=ChangeVoice).grid(row=2,column=0, padx=2)

        self.btnExit=Button(ButtonFrame, pady=1, bd=4, font=('arial', 30, 'bold'), padx=25, width=11, height=2
        , text="Exit", command=iExit).grid(row=3,column=0, padx=2)


        #=============================================================================================
        
 
sapi.say("Text To Speech in Python, Enter sentence for sapi to read. Thank you")
sapi.runAndWait()



if __name__=='__main__':
    root = Tk()
    application = TextToSpeech(root)
    root.mainloop()
