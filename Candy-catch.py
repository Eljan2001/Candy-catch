from tkinter import*
import os
import time
import random
menu=Tk()
menu.title('Menu')
menu.geometry('500x500+700+300')
canvas_1=Canvas(menu, width=500, height=500, bg='#000000')
canvas_1.pack()
canvas_1.create_text(245, 50, text='Menu', font=('Times', 40),  fill='blue') 

def onclick():
    menu.destroy()
    
    root=Tk()
    root.title('game')

    canvas=Canvas(root,width=500, height=600, bg='#000000')
    canvas.pack()
        
    canvas.create_text(245, 540, text='Score:', font=('Times', 30), fill='red')
    list1=[]
    canvas.create_rectangle(0,501,500,600,outline='white')
    L3=[0]
    for i in range(100, 400):

        list1.append(i)


    class Fireballs:

        def __init__(self,canvas, sack):

            self.canvas=canvas
            self.sack=sack
            random_choice=random.choice(list1)
            colour_list=['red', 'blue', 'green', 'pink']
            self.id=canvas.create_oval(random_choice, 10,random_choice+15, 25, fill=random.choice(colour_list))
            canvas.tag_lower(self.id)
            self.id2=canvas.create_text(320, 540, text=L3[0], font=('Times', 30), fill='red')
        def draw(self):
            self.canvas.move(self.id, 0, 3)

        def eternal_loop(self):
            pos=self.canvas.coords(self.id)
            sack_pos=self.canvas.coords(self.sack.id3)
            sack_pos2=self.canvas.coords(self.sack.id2)
            if pos[3]>=500:
                canvas.delete(self.id)
                random_choice=random.choice(list1)
                colour_list=['red', 'blue', 'green', 'pink']
                self.id=canvas.create_oval(random_choice, 10,random_choice+15, 25, fill=random.choice(colour_list))
                canvas.tag_lower(self.id)
                L3[0]-=10
                canvas.delete(self.id2)
                self.id2=canvas.create_text(320, 540, text=L3[0], font=('Times', 30), fill='red')
            if pos[3]>=sack_pos[1] and pos[1]<=sack_pos2[1]:
                if pos[2]>=sack_pos[0] and pos[2]<=sack_pos[2]:
                    canvas.delete(self.id)
                    canvas.delete(self.id2)
                    L3[0]+=10
                    self.id2=canvas.create_text(320, 540, text=L3[0], font=('Times', 30), fill='red')
                    random_choice=random.choice(list1)
                    colour_list=['red', 'blue', 'green', 'pink']
                    self.id=canvas.create_oval(random_choice, 10,random_choice+15, 25, fill=random.choice(colour_list))
                    canvas.tag_lower(self.id)
                    
    class Sack:

        def __init__(self, canvas):
            self.canvas=canvas
            self.id=canvas.create_rectangle(200,400, 300, 450, fill='#476042')
            self.id2=canvas.create_oval(230,340, 270, 350, outline='#476042', fill='black')
            self.id3=canvas.create_rectangle(230,345, 270, 401, outline='#476042',  fill='#476042')
            self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
            self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
            self.x=0
            self.y=0
            canvas.tag_raise(self.id)
            canvas.tag_raise(self.id2)
        def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            self.canvas.move(self.id2, self.x, self.y)
            self.canvas.move(self.id3, self.x, self.y)
            pos=self.canvas.coords(self.id)
            

            if pos[0]<=0:
                self.x=3

            if pos[2]>=self.canvas.winfo_width():
                self.x=-3

        def turn_left(self, evt):

            self.x=-3
        def turn_right(self, evt):

            self.x=3
    sack=Sack(canvas)
    fireballs=Fireballs(canvas, sack)

    while 1:
        if L3[0]!=-100:
            fireballs.draw()
            fireballs.eternal_loop()
            sack.draw()
            root.update()
            root.update_idletasks()
            time.sleep(0.01)
        if L3[0]==-100:
            root.destroy()
            root1=Tk()
            root1.geometry('500x500+700+300')
            canvas1=Canvas(root1, width=500, height=500)
            canvas1.pack()
            canvas1.create_text(245,100,text='Game Over', font=('Times', 30))
            canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))
            Score=canvas1.create_text(400,150,text=L3[0], font=('Times', 30))

            def restart():
                root1.destroy()
                os.startfile(r'C:\Users\elcan\Desktop/custom game2.py')

            btn=Button(root1, text='Restart',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
            btn.place(x=80, y=240)
            root1.mainloop()
        if L3[0]==200:
            root.destroy()
            root1=Tk()
            root1.geometry('500x500+700+300')
            canvas1=Canvas(root1, width=500, height=500)
            canvas1.pack()
            canvas1.create_text(245,100,text='Success', font=('Times', 30))
            canvas1.create_text(245,150,text='Your Score is:', font=('Times', 30))
            Score=canvas1.create_text(400,150,text=L3[0], font=('Times', 30))

            def restart():
                root1.destroy()
                os.startfile(r'C:\Users\elcan\Desktop/custom game2.py')

            btn=Button(root1, text='Menu',font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=restart)
            btn.place(x=80, y=240)
            root1.mainloop()
    root.mainloop()
       
    

def onclick1():
    menu.destroy()
    tutorial=Tk()
    tutorial.title('Tutorial')
    tutorial.geometry('500x500+700+300')
    canvas4=Canvas(tutorial, width=500, height=500, bg='#000000')
    canvas4.pack()
    canvas4.create_text(245, 40,text='Tutorial', font=('Times', 40), fill='blue')
    canvas4.create_text(245,140,text='←  button to turn left', font=('Times', 25), fill='white')
    canvas4.create_text(245,240,text='→  button to turn right', font=('Times', 25), fill='white')

    def onclick2():
        tutorial.destroy()
        os.startfile(r'C:\Users\elcan\Desktop/custom game2.py')

    btn5=Button(tutorial, text='Back', font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=onclick2)
    btn5.place(x=70, y=270)
    tutorial.mainloop()

def onclick30():
    menu.destroy()

btn1=Button(menu, text='Play', font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=onclick)
btn1.place(x=80, y=100)
btn2=Button(menu, text='Tutorial', font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=onclick1)
btn2.place(x=80, y=240)
btn2=Button(menu, text='Quit', font=('Times', 15), bg='#ffcc00', fg='#000000', width=30, height=3, state='normal', command=onclick30)
btn2.place(x=80, y=380)
menu.update()
time.sleep(0.01)
menu.mainloop()

