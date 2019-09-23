from tkinter import *





class main():
    def __init__(self):
        self.top=Tk()
        Label(self.top, text='Pick what to practice').pack()
        self.phrase=''
        self.userP=''
        self.error=0

        self.start= Frame(self.top)
        self.start.pack()
        self.phrase='how much would could a woodchuck chuck'
        Button(self.start,text='woodchuck',command=lambda:self.phraseGen('how much would could a woodchuck chuck')).pack()
        Button(self.start,text='tounge tied',command=lambda:self.phraseGen('Sally sells sea shells down by the sea shore')).pack()
        self.start.mainloop()




    def phraseGen(self,txt):
        self.phrase=txt
        print(self.phrase)
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
        self.text=Text(self.win, height=25, width=60)
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

    def highlight(self,text):
        wanted=len(self.userP)-1

        text.tag_delete('red')
        

        txtInput=(str(1)+'.'+str(wanted))
        print(txtInput)
        text.tag_add('red',txtInput)
        text.tag_config('red',foreground='red')





main()
