from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Seven Cruel Hours Of Our Lives")
root.configure(bg="lavender")

g3 = Label(root)
g5 = Label(root)
g10 = Label(root)

class grade3:
    def __init__(self,lan,math):
        self.la=lan
        self.m=math
    def calculate(self):
        tmw = self.la+self.m
        tmw2 = tmw*100
        tmw3 = tmw2/200
        g3["text"]=str(tmw3)
class grade5:
    def __init__(self,lan,math,ss):
        self.la=lan
        self.m=math
        self.sss=ss
    def calculate(self):
        tmw = self.la+self.m+self.sss
        tmw2 = tmw*100
        tmw3 = tmw2/300
        g5["text"]=str(tmw3)
class grade10:
    def __init__(self,lan,math,ss,fl):
        self.la=lan
        self.m=math
        self.sss=ss
        self.fol=fl
    def calculate(self):
        tmw = self.la+self.m+self.fol+self.sss
        tmw2 = tmw*100
        tmw3 = tmw2/400
        g10["text"]=str(tmw3)
def yes():
    global y
    if y=="t":
        gradefor3.calculate()
    y="t"

y="f"
gradefor3=grade3(70,90)
gradefor5=grade5(70,90,80)
gradefor10=grade10(70,90,80,60)
g3.pack()
btn1=Button(root,text="Grade 3",command=yes())
btn1.pack()
g5.pack()
btn2=Button(root,text="Grade 5",command=gradefor5.calculate())
btn2.pack()
g10.pack()
btn3=Button(root,text="Grade 10",command=gradefor10.calculate())
btn3.pack()
root.mainloop()