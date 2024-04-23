from __main__ import *
import sys

try:
    from tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

fo1=open("recipt.txt","r")
list1=fo1.readlines()

del list1[1]
del list1[2]
del list1[3]
del list1[4]
del list1[5]
list1[0]=list1[0][:-1]
list1[1]=list1[1][:-1]
list1[2]=list1[2][:-1]
list1[3]=list1[3][:-1]
list1[4]=list1[4][:-1]


font10 = "-family {Georgia} -size 15 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"

p='''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@  @        FAIRMONT DUBAI       @  @@@@@@@@@@@@@
@@@@@@@@@@@@@  @        DUBAI SEA VIEW          @  @@@@@@@@@@@@@
@@@@@@@@@@@@@  @  SERVING GUEST SINCE    @  @@@@@@@@@@@@@
@@@@@@@@@@@@@  @    #######2015#######   @  @@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@
@
@          NAME:-                  %s
@
@          ADDRESS:-            %s
@
@          MOBILE NO:-       %s
@
@          YOUR TOTAL BILL IS Rs:-        %s
@
@          YOUR ROOM NUMBER IS:-     %s
@
@    
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
     
     
'''%(list1[0],list1[1],list1[2],list1[4],list1[3])

class recipt:
    def __init__(self):
        root=Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#d9d9d9'

        root.geometry("800x800")
        root.title("recipt")
        root.configure(background="#DEB887")

        self.Label1 = Label(root)
        self.Label1.configure(background="#FFEFDB")
        self.Label1.place(relx=0, rely=0, height=800, width=800)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(font=font10)
        self.Label1.configure(text=p)
        self.Label1.configure(anchor=N)
        self.Label1.configure(wraplength=1000)
        self.Label1.configure(justify =LEFT)
        self.Label1.configure(width=582)

        '''self.Button1 = Button(root)
        self.Button1.place(relx=0.91, rely=0.05, height=33, width=43)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#ffffff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''#PRINT''')
        #self.Button1.configure(command=chk_name)

        root.mainloop()

if __name__ == '__main__':
    recipt1=recipt()