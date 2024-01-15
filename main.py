from tkinter import *
from PIL import ImageTk
import multiplayer
import single_player


class TurtleRace:

    def __init__(self):
        # setting up the main window
        self.root = Tk()
        self.root.title("Turtle Race")
        self.root.geometry('1080x600+100+80')

        # adding a background image
        self.bg_image = ImageTk.PhotoImage(file="img/bg.png")
        self.bg_label = Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0)

        self.welcome = Label(self.root, text="Welcome to Turtle Racing!", font=("san-serif", 16, "bold"), bg="#ccccff",
                             fg="#000066")
        self.welcome.pack(pady=10)

        # Multiplayer or single player ?
        self.choice_frame = Frame(self.root, bg="#b3e6b3")
        self.choice_frame.place(x=480, y=300)
        self.single = Button(self.choice_frame, text="Single Player", bg="lightgrey", command=self.single_play)
        self.single.grid(column=0, row=1, padx=10)
        self.multi = Button(self.choice_frame, text="Multiplayer", bg="lightgrey", command=self.multiplayer)
        self.multi.grid(column=1, row=1, padx=10)
        self.root.mainloop()

    def single_play(self):
        single_player.SinglePlayer()

    def multiplayer(self):
        multiplayer.Multiplayer()


raceObj = TurtleRace()
