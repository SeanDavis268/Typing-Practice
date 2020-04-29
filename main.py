from tkinter import *
import os
import time





class main():
    """This class is the first window when the program is ran. It checks
       the current directory for txt documents and displays them. They can then
       be selected by entering their names into the entry box."""
    def __init__(self):
        self.top = Tk()
        self.startLabel = Label(self.top, text = "Pick what to practice. Type in the desired file name in the textBox", font=12)
        self.startLabel.pack()

        self.phrase = ''
        self.userP = ''
        self.error = 0

        #option variables

        self.fontSizeOp=IntVar()

        self.start = Frame(self.top)
        self.start.pack()
        self.phrase = 'the phrase didn"t load' #default phrase
        ####file reading#####
        cwd = os.getcwd()
        textFiles = [f for f in os.listdir(cwd) if f.endswith('.txt')]
        progressFiles = textFiles #saves reading the directory twice

        textFiles = [f for f in textFiles if  f[0:6] != "zFsavE"] #this ignores the progress Files

        self.progressFiles = [ f for f in progressFiles if f[0:6] == "zFsavE" ]
        #####progressFiles reading and organizing
        self.prettyProgress=""
        for each in self.progressFiles:
            throwAway=open(each,"r")
            throwAway=throwAway.read()

            self.prettyProgress=self.prettyProgress +throwAway+ ", "

        #########################################

        prettyFiles = textFiles[0]

        for each in textFiles[1:]:
            prettyFiles = prettyFiles + ", " + each

        print(prettyFiles)

        Label(self.start, text="Saved Progress: "+self.prettyProgress, font=10).pack()

        Label(self.start, text = "Start a new txt file: " +prettyFiles, font=10).pack()
        Label(self.start,text = "Enter the desired file name with extention in the text box Below.", font=12).pack()
        Label(self.start, text = "The '?' after the extension tells the program what line to start on ", font=12).pack()

        entryBox = Text(self.start,width = '12', height = '1')
        myList = []
        myList.append(entryBox)
        entryBox.pack()
        widget = Button(self.start,text='click to load file', command=lambda:self.phraseGen(entryBox.get('1.0',END),textFiles))
        widget.pack()

        #Button(self.start,text = 'woodchuck',command = lambda:self.phraseGen('how much would could a woodchuck chuck')).pack()
        #Button(self.start,text = 'tounge tied',command = lambda:self.phraseGen('Sally sells sea shells down by the sea shore')).pack()
        Button(self.start, text="options", command=lambda:self.optionsMenu()).pack()



        self.start.mainloop()


    def optionsMenu(self):
        """ opens new window with entry boxes for options. can be canceled and can confirm the users choices. either results in
            control being brought back to the main window. main window is frozen for these times """
        opWindow=Tk()
        Label(opWindow,text="Font Size").pack()
        font12=Radiobutton(opWindow,text='12', variable= self.fontSizeOp,value=12, command=lambda: self.fontSizeOp.set(12))
        font16=Radiobutton(opWindow,text='16',variable= self.fontSizeOp, value=16, command=lambda: self.fontSizeOp.set(16))
        print(self.fontSizeOp.get())   #where i left off. font var doesnt change bc of the button
        font12.pack()
        font16.pack()








    def phraseGen(self,txt,container=False):

        """This method takes the txt doc and attempts to read its first line
           It reads the doc as ascii to avoid characters not on the keyboard.
           After it starts phase2()."""
        cwd = os.getcwd()
        files = [f for f in os.listdir(cwd) if f.endswith('.txt')]
        #print(files)
        print(txt)
        yeet = str(txt[0:-1]) #removes newline character
        self.txt = txt

        splitter=yeet.split("?") #splits on the ? seperater for line number
        splitter.append(0) #prevents list index errors
        yeet=splitter[0] #grabs the file name

        self.fileTitle=yeet
        self.desiredLine=int(splitter[1]) #grabs the desired line, 0 if not specified
        desiredLineCounter=self.desiredLine


        try:

            print(yeet)
            self.file = open(yeet,'rb')
            #####
            self.file2 = open(yeet,'rb') #allows display of next line
            print('loaded')

            while desiredLineCounter>=0:
                self.txt = self.file.readline()
                #######
                self.txt2 = self.file2.readline()
                self.txt2 = self.file2.readline() #done twice so it reads the nextline
                desiredLineCounter-=1


            self.txt = self.txt.decode(encoding = 'ascii', errors = 'ignore')
            print(self.txt)
            ####
            self.txt2 = self.txt2.decode(encoding = 'ascii', errors = 'ignore')

            self.phrase = self.txt

            self.startLabel.destroy()
            self.start.destroy()

            self.phase2()

        except:
            print('failed')



    def phase2(self):
        """This is the window where the the text from the doc is displayed.
           It grabs key inputs and checks them with check()"""
        print(self.fontSizeOp.get())
        self.win = Frame(self.top)
        self.minutes = 0
        self.seconds = 0
        #self.startTime = time.strftime("%H:%M:%S")
        #self.startTime=self.startTime[3:]#tracks minutes and seconds
        #self.Sminutes=self.startTime[:2]
        #self.Sseconds=self.startTime[3:]


        self.currentFile = Label(self.win,text = self.fileTitle)
        self.currentFile.pack()

        self.phraseLabel = Label(self.win, text ="Your current line is "+ str(self.desiredLine))
        self.phraseLabel.pack() #this displays the line number


        self.text=Text(self.win, height = 3, width = 95)
        self.text.insert('end',self.phrase)
        self.text['state'] = DISABLED
        self.text.config(font=("Arial",self.fontSizeOp.get())) #i changed it here
        self.text.pack()

        self.text2=Text(self.win, height = 3, width = 95)
        self.text2.insert('end',self.txt2)
        self.text2['state'] = DISABLED
        self.text2.pack()

        self.timer = Label(self.win, text = "0")
        self.timer.pack()

        self.saveButton=Button(self.win, text="Save Progress", command=lambda:self.saveProgress())
        self.saveButton.pack()

        self.backButton=Button(self.win, text="Return to selection", command=lambda:self.returnSel())
        self.backButton.pack()



        self.win.bind('<Key>', lambda event :self.check(event))
        self.win.focus_set()
        self.win.pack()

        self.updateClock()
        self.win.mainloop()


    def saveProgress(self):
        print(self.fileTitle)
        print(self.desiredLine)
        saveFile= open("zFsavE" +str(self.fileTitle), "w+")  #zFsave differentiats it from other files
        saveFile.write(str(self.fileTitle)+ "?" +str(self.desiredLine))
        #^this will be displayed so the user can remember where they left off

    def returnSel(self):
        print('returning to Selection')
        try:
            self.top.destroy()
        except:
            print("this shouldn't appear")
        main()



    def updateClock(self):
        """ I realised after creating the code below it was unnecesarrily
           elaborate and instead implemented a simple counter  """
        #now = time.strftime("%H:%M:%S")
        #now=now[3:]
        #Nminutes=now[:2]
        #Nseconds=now[3:]
        #elapsedMin=int(Nminutes)-int(self.Sminutes)
        #elapsedSec=int(Nseconds)-int(self.Sseconds)
        #elapsedTime=str(elapsedMin)+":"+str(elapsedSec)
        #print(elapsedTime)
        self.seconds += 1

        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
        totalTime = str(self.minutes) + ":" + str(self.seconds)
        self.timer.configure(text = totalTime)
        self.win.after(1000, self.updateClock)


    def check(self,event):
        """This method checks the users input to the desired key in the txt.
            If the key is correct it calls highlight(). If not it records an
            error. It also calls for the next line to be read from the file if
            the current line is finished."""

        temp = str(event.char)
        #print(temp)
        wanted = self.phrase[len(self.userP)]
        try: #when a blank line is loaded oneAhead causes an error
            oneAhead = self.phrase[len(self.userP)+1] #this is to highlight spaces
        except:
            pass
        if temp == wanted:
            print(temp)
            self.userP = self.userP + temp
            if oneAhead == " ":
                self.highlight(self.text,True)
            else:
                self.highlight(self.text)
        else:
            self.error += 1

        if len(self.phrase) - 1 == len(self.userP):
            self.nextLine()

    def nextLine(self):
        print('########################')
        spaces = 0
        self.txt = self.file.readline()
        print(self.txt)
        self.txt = self.txt.decode(encoding = 'ascii', errors = 'ignore')
        ####
        self.txt2 = self.file2.readline()
        print(self.txt2)
        self.txt2 = self.txt2.decode(encoding = 'ascii', errors = 'ignore')

        if len(self.txt.strip()) == 0 : #skips blank lines
            print('skipped')
            self.nextLine()
        while self.txt[spaces] == ' ': #removes spaces from the start of the line
            spaces += 1
        print(spaces)
        self.phrase = self.txt[spaces:]
        """
        attempt=[]
        for each in self.phrase:
            if each.isalpha() or each.isnumeric():
                attempt.append(each)
        print(attempt)  This could possibly be used if reading errors persist
        """

        self.text.config(state = NORMAL)
        self.text.delete('1.0','end')
        self.text.insert('1.0',self.phrase)
        self.text.config(state = DISABLED)

        self.text2.config(state = NORMAL)
        self.text2.delete('1.0','end')
        self.text2.insert('1.0',self.txt2)
        self.text2.config(state = DISABLED)

        self.desiredLine+=1#desiredLine doubles as a counter
        self.phraseLabel.configure(text=str(self.desiredLine))


        #self.phrase=  #clear the data
        self.userP = ''


    def highlight(self,text,space = False):
        """ This simply highlights the desired character."""
        wanted = len(self.userP)

        text.tag_delete('red')
        text.tag_delete('redBack')

        txtInput = (str(1) + '.' + str(wanted))
        print(txtInput)
        if space == True:

            text.tag_add('redBack',txtInput)
            text.tag_config('redBack',background = 'red')
        text.tag_add('red',txtInput)
        text.tag_config('red',foreground = 'red')

main()
