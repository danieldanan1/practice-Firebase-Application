#import tkMessageBox


#tkMessageBox.showinfo('result','blabla')

from Tkinter import *



def response_window(item):
    main = Tk()
    lable=Label(main,text='Results!')
    lable.pack()
    main.title('FireBase Response')
    t=Text(main)
    for x in item:
        t.insert(END, x + '\n')
    t.pack()
    main.mainloop()
    #self.messageVar = Message(main, text = item)
#messageVar.config(bg='lightgreen')
    #self.messageVar.pack( )


