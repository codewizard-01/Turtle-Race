from tkinter import *

class Result:
    def __init__(self, winner, loser):
        self.root = Tk()
        self.root.geometry("720x450")
        self.root.title("Bets' Result")

        self.result = Label(text="Result")
        self.result.pack()
        for i in winner:
            self.winner1 = Label(text=f"{i}")
            self.winner1.pack()

        for i in loser:
            self.loser = Label(text=f"{i}")
            self.loser.pack()

        self.root.mainloop()

