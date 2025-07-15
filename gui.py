from tkinter import *
import random
from tkinter import messagebox
root = Tk()
root.config(bg="red")
root.geometry("600x400")
root.title("Rock, Paper, Scissors!")
def rockclick():
    aichoices = ["Rock", "Paper", "Scissors"]
    aifinalchoice = random.choice(aichoices)
    if aifinalchoice == "Scissors":
       messagebox.showinfo("You Won", "You won, The AI chose Scissors...")
    elif aifinalchoice == "Paper":
       messagebox.showinfo("You Lost", "You lost, The AI chose Paper...")
    else:
       messagebox.showinfo("You Won", "It's a tie, The AI chose Rock...")
def paperclick():
    aichoices = ["Rock", "Paper", "Scissors"]
    aifinalchoice = random.choice(aichoices)
    if aifinalchoice == "Scissors":
       messagebox.showinfo("You Lost", "You lost, The AI chose Scissors...")
    elif aifinalchoice == "Rock":
       messagebox.showinfo("You Won", "You won, The AI chose Rock...")
    else:
       messagebox.showinfo("You Won", "It's a tie, The AI chose Paper...")
def scissorsclick():
    aichoices = ["Rock", "Paper", "Scissors"]
    aifinalchoice = random.choice(aichoices)
    if aifinalchoice == "Paper":
       messagebox.showinfo("You Won", "You won, The AI chose Paper...")
    elif aifinalchoice == "Rock":
       messagebox.showinfo("You Lost", "You lost, The AI chose Rock...")
    else:
       messagebox.showinfo("You Won", "It's a tie, The AI chose Scissors...")

label1 = Label(fg="blue", font="Helvetica 20 bold", text = "Play either Rock Paper or Scissors")
label1.pack()
rockbutton = Button(fg="black", bg="gray", text="Rock", height=10, width=15, font="Times 20 bold", command=rockclick)
rockbutton.place(x=200, y=30)
paperbutton = Button(fg="black", bg="white", text="Paper", height=10, width=15, font="Times 20 bold", command=paperclick)
paperbutton.config(bg="red")
paperbutton.place(x=20, y=210)
scissorsbutton = Button(fg="white", bg="red", text="Scissors", height=10, width=15, font="Times 20 bold", command=scissorsclick)
scissorsbutton.place(x=200, y=210)


root.mainloop()