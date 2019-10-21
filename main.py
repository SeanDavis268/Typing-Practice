from tkinter import *
import os
import time





class main():
    """This class is the first window when the program is ran. It checks
       the current directory for txt documents and displays them. They can then
       be selected by entering their names into the entry box."""
    def __init__(self):
        self.top = Tk()
        self.startLabel=Label(self.top, text = "Pick what to practice. Type in the desired file name in the textBox")
        self.startLabel.pack()

        self.phrase = ''
        self.userP = ''
        self.error = 0

        self.start = Frame(self.top)
        self.start.pack()
        self.phrase = 'the phrase didn"t load' #default phrase
        ####file reading#####
        cwd = os.getcwd()
        textFiles = [f for f in os.listdir(cwd) if f.endswith('.txt')]

        prettyFiles=textFiles[0]

        for each in textFiles[1:]:
            prettyFiles=prettyFiles+", "+ each

        print(prettyFiles)

        Label(self.start, text = prettyFiles).pack()
        entryBox = Text(self.start,width = '12', height = '1')
        myList = []
        myList.append(entryBox)
        entryBox.pack()
        widget = Button(self.start,text='click to load file', command=lambda:self.phraseGen(entryBox.get('1.0',END),textFiles))
        widget.pack()

        Button(self.start,text = 'woodchuck',command = lambda:self.phraseGen('how much would could a woodchuck chuck')).pack()
        Button(self.start,text = 'tounge tied',command = lambda:self.phraseGen('Sally sells sea shells down by the sea shore')).pack()



        self.start.mainloop()




    def phraseGen(self,txt,container=False):
        """This method takes the txt doc and attempts to read its first line
           It reads the doc as ascii to avoid characters not on the keyboard.
           After it starts phase2()."""
        cwd = os.getcwd()
        files = [f for f in os.listdir(cwd) if f.endswith('.txt')]
        #print(files)
        print(txt)
        yeet = str(txt[0:-1])
        self.txt = txt
        try:
            #print(container)
             #IT currently won't accept any input as correct
            print(yeet)
            self.file = open(yeet,'rb')
            #####
            self.file2=open(yeet,'rb') #allows display of next line
            print('loaded')
            self.txt = self.file.readline()
            #######
            self.txt2= self.file2.readline()
            self.txt2= self.file2.readline()

            self.txt = self.txt.decode(encoding ='ascii', errors = 'ignore')
            print(self.txt)
            ####
            self.txt2 = self.txt2.decode(encoding ='ascii', errors = 'ignore')


        except:
            print('failed')

        self.phrase = self.txt
        #print(self.phrase)
        self.startLabel.destroy()
        self.start.destroy()

        self.phase2()

    def phase2(self):
        """This is the window where the the text from the doc is displayed.
           It grabs key inputs and checks them with check()"""

        self.win = Frame(self.top)
        self.minutes=0
        self.seconds=0
        #self.startTime = time.strftime("%H:%M:%S")
        #self.startTime=self.startTime[3:]#tracks minutes and seconds
        #self.Sminutes=self.startTime[:2]
        #self.Sseconds=self.startTime[3:]


        self.phraseLabel = Label(self.win, text = self.phrase)
        self.phraseLabel.pack()

        self.userPhrase=Label(self.win,text = self.userP)
        self.userPhrase.pack()


        self.text=Text(self.win, height = 3, width = 95)
        self.text.insert('end',self.phrase)
        self.text['state'] = DISABLED
        self.text.pack()

        self.text2=Text(self.win, height = 3, width = 95)
        self.text2.insert('end',self.txt2)
        self.text2['state'] = DISABLED
        self.text2.pack()

        self.timer=Label(self.win, text="0")
        self.timer.pack()



        self.win.bind('<Key>', lambda event :self.check(event))
        self.win.focus_set()
        self.win.pack()

        self.updateClock()
        self.win.mainloop()

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
        self.seconds+=1

        if self.seconds>=60:
            self.seconds=0
            self.minutes+=1
        totalTime=str(self.minutes)+":"+str(self.seconds)
        self.timer.configure(text=totalTime) 
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
            oneAhead=self.phrase[len(self.userP)+1] #this is to highlight spaces
        except:
            pass
        if temp == wanted:
            print(temp)
            self.userP = self.userP + temp
            if oneAhead== " ":
                self.highlight(self.text,True)
            else:
                self.highlight(self.text)
        else:
            self.error += 1

        if len(self.phrase) - 1 == len(self.userP):
            self.nextLine()

    def nextLine(self):
        print('########################')
        spaces=0
        self.txt = self.file.readline()
        print(self.txt)
        self.txt = self.txt.decode(encoding = 'ascii', errors='ignore')
        ####
        self.txt2 = self.file2.readline()
        print(self.txt2)
        self.txt2 = self.txt2.decode(encoding = 'ascii', errors='ignore')

        if len(self.txt.strip()) == 0 : #skips blank lines
            print('skipped')
            self.nextLine()
        while self.txt[spaces]==' ': #removes spaces from the start of the line
            spaces+=1
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


        #self.phrase=  #clear the data
        self.userP = ''


    def highlight(self,text,space=False):
        """ This simply highlights the desired character."""
        wanted = len(self.userP)

        text.tag_delete('red')
        text.tag_delete('redBack')

        txtInput = (str(1) + '.' + str(wanted))
        print(txtInput)
        if space==True:

            text.tag_add('redBack',txtInput)
            text.tag_config('redBack',background = 'red')
        text.tag_add('red',txtInput)
        text.tag_config('red',foreground = 'red')

main()
