#!/usr/bin/env Python

from tkinter import *
from string import ascii_uppercase

class Main_window(Frame):
    counter = 0
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.grid(pady=20)

    def init_window(self):
        self.master.title("TIC TAC TOE")

        topbar = Menu(self.master)
        self.master.config(menu=topbar)
        file = Menu(topbar)
        file.add_command(label="Exit", command=self.client_exit)
        topbar.add_cascade(label="File", menu=file)

        self.img = PhotoImage(file='data/gifs/img.gif')
        logo = Label(self.master, image=self.img)
        logo.grid(row=0, column=0, pady=10, padx=10)

        entry1label = Label(self.master, text="Enter size (5-10):")
        entry1label.grid(row=1, column=0, padx=10)

        self.entry1 = Entry(self.master)
        self.entry1.config(width=10)
        self.entry1.grid(row=2, column=0)


        self.confirm_img = PhotoImage(file='data/gifs/1.gif')
        entry_button = Button(self.master, text="confirm",
                              padx=2,
                              command=self.size_test)
        entry_button.config(image=self.confirm_img, compound='left')
        entry_button.grid(row=3, column=0)

    def size_test(self):
        error_message = Label(self.master, width=25)
        error_message.grid(row=4, column=0, padx=10)
        try:
            field_size = int(self.entry1.get())
            if field_size not in range(5, 11):
                error_message.configure(text='Size can be from 5x5 up to 10x10.')
                return None
        except ValueError:
            error_message.configure(text='Insert only whole #!')
            return None
        game = Tk()
        play = GameWindow(game, field_size)
        play.mainloop()

    def client_exit(self):
        exit()
        
class GameWindow(Frame):
    
    def __init__(self, field_size, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.field_size = field_size
        self.square_size = 25
        self.playGrid = []      # X = 1 ; O = 0
        self.lastPlayer = 0
        self.game()

    def draw_cross(self, x, y):
        x = (x - 1) * self.square_size
        y = (y - 1) * self.square_size
        self.gridCanvas.create_line(x + 3,
                              y + 3,
                              x + self.square_size - 3,
                              y + self.square_size - 3,
                              fill='#0000ff',
                              width=3)

        self.gridCanvas.create_line(x + self.square_size - 3,
                              y + 3,
                              x + 3,
                              y + self.square_size - 3,
                              fill='#0000ff',
                              width=3)

    def draw_circle(self, x, y):
        x = (x - 1) * self.square_size
        y = (y - 1) * self.square_size
        self.gridCanvas.create_oval(x + 3,
                              y + 3,
                              x + self.square_size -3,
                              y + self.square_size -3,
                              outline='#ff0000',
                              width=3)

    def create_hlabel(self):
        label_width = self.field_size * self.square_size
        hlabel = Canvas(self.master,
                        width=label_width,
                        height=self.square_size)
        for num in range(1, self.field_size +1):
            x = ((num - 1) * self.square_size) + self.square_size / 2
            y = self.square_size / 2
            hlabel.create_text(x, y, text=num)
        return hlabel

    def create_vlabel(self):
        abc = ascii_uppercase
        label_height = self.field_size * self.square_size
        vlabel = Canvas(self.master,
                        width=self.square_size,
                        height=label_height)
        counter = 1
        while not counter > self.field_size:
            x = self.square_size / 2
            y = ((counter - 1) * self.square_size) + self.square_size / 2
            letter = abc[counter - 1]
            vlabel.create_text(x, y, text=letter)
            counter += 1
        return vlabel

    def mouseClick(self, event):
        y = event.x
        x = event.y
        y = y // self.square_size + 1
        x = x // self.square_size
        letterX = ascii_uppercase[x]
        if self.lastPlayer == 0:
            self.draw_cross(x, y)
            self.lastPlayer = 1
        else:
            self.draw_circle(x, y)
            self.lastPlayer = 2
            
    def game(self):
        self.master.title("You are playing size %s x %s" % (self.field_size, self.field_size))


        grid_width = self.field_size * self.square_size
        grid_height = self.field_size * self.square_size
        self.gridCanvas = Canvas(self.master,
                            width=grid_width,
                            height=grid_height)
        self.gridCanvas.grid(row=1, column=1,
                        padx=0, pady=0)

        horizontal_label = self.create_hlabel(self.field_size)
        horizontal_label.grid(row=0, column=1)
        vertical_label = self.create_vlabel(self.field_size)
        vertical_label.grid(row=1, column=0)

        self.gridCanvas.create_rectangle(0, 0, grid_width, grid_height, fill='#ffffff')
        for i in range(1, self.field_size):
            xy = self.square_size * i
            self.gridCanvas.create_line(xy, 0, xy, grid_height, fill="#000000")
            self.gridCanvas.create_line(0, xy, grid_width, xy, fill="#000000")

        self.gridCanvas.bind("<Button-1>", self.mouseClick)




if __name__=='__main__':
    root = Tk()
    TTT = Main_window(root)
    TTT.mainloop()
