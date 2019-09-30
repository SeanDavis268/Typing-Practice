from tkinter import *
import os






class main():
    def __init__(self):
        self.top=Tk()
        Label(self.top, text='Pick what to practice').pack()
        self.phrase=''
        self.userP=''
        self.error=0

        self.start= Frame(self.top)
        self.start.pack()
        self.phrase='the phrase didn"t load' #default phrase
        ####file reading#####
        cwd=os.getcwd()
        textFiles = [f for f in os.listdir(cwd) if f.endswith('.txt')]

        #i=-1
        #for each in textFiles:
            #file=open(each,'r')
            #Files2Read.append(file)
            #i+=1
            #Button(self.start, text=each, command=lambda:self.phraseGen(i,textFiles)).pack() #for some reason it always loads the text as the last txt docs name
            #this is likely because when the button is pushed it reads the last each and the txt for the button reads it as its iterated


        Label(self.start, text=textFiles).pack()
        entryBox=Text(self.start,width = '10', height = '1')
        myList=[]
        myList.append(entryBox)
        entryBox.pack()
        widget=Button(self.start,text='click to load file', command=lambda:self.phraseGen(entryBox.get('1.0',END),textFiles))
        widget.pack()

        Button(self.start,text='woodchuck',command=lambda:self.phraseGen('how much would could a woodchuck chuck')).pack()
        Button(self.start,text='tounge tied',command=lambda:self.phraseGen('Sally sells sea shells down by the sea shore')).pack()



        self.start.mainloop()




    def phraseGen(self,txt,container=False):
        cwd=os.getcwd()
        files= [f for f in os.listdir(cwd) if f.endswith('.txt')]
        #print(files)
        print(txt)
        yeet=str(txt[0:-1])
        self.txt=txt
        try:
            #print(container)
             #IT currently won't accept any input as correct
            print(yeet)
            self.file=open(yeet,'rb')

            print('loaded')
            self.txt=self.file.readline()
            self.txt=self.txt.decode('ascii', errors='replace')
            print(self.txt)

        except:
            print('failed')

        self.phrase=self.txt
        #print(self.phrase)
        self.start.destroy()
        self.phase2()

    def phase2(self):
        self.win=Frame(self.top)


        self.phraseLabel=Label(self.win, text=self.phrase)
        self.phraseLabel.pack()

        self.userPhrase=Label(self.win,text=self.userP)
        self.userPhrase.pack()

        #canvas=Canvas(self.win)
        #canvas.pack()
        self.text=Text(self.win, height=25, width=65)
        self.text.insert('end',self.phrase)
        self.text['state']=DISABLED
        self.text.pack()



        self.win.bind('<Key>', lambda event :self.check(event))
        self.win.focus_set()
        self.win.pack()

        #self.win.mainloop()

    def check(self,event):
        temp=str(event.char)
        #print(temp)
        wanted=self.phrase[len(self.userP)]


        if temp==wanted:
            print(temp)
            self.userP=self.userP+temp
            self.highlight(self.text)
        else:
            self.error+=1

        if len(self.phrase)-1==len(self.userP):
            print('########################')
            self.txt=self.file.readline()
            self.txt=self.txt.decode(encoding='ascii')
            self.phrase=self.txt
            #print(self.phrase)
            self.text.config(state=NORMAL)
            self.text.delete('1.0','end')
            self.text.insert('1.0',self.phrase)
            self.text.config(state=DISABLED)


            #self.phrase=  #clear the data
            self.userP=''


    def highlight(self,text):
        wanted=len(self.userP)

        text.tag_delete('red')


        txtInput=(str(1)+'.'+str(wanted))
        print(txtInput)
        text.tag_add('red',txtInput)
        text.tag_config('red',foreground='red')





main()
