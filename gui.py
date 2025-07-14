from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("Rock, Paper, Scissors!")

label1 = Label(fg="black", font="Helvetica 20 bold", text = "Play either Rock Paper or Scissors")
label1.pack()
rockbutton = Button(fg="black", bg="gray", text="Rock", height=10, width=15, font="Times 20 bold")
rockbutton.place(x=200, y=30)
paperbutton = Button(fg="black", bg="lightgray", text="Paper", height=10, width=15, font="Times 20 bold")
paperbutton.config(bg="red")
paperbutton.place(x=20, y=210)
scissorsbutton = Button(fg="black", bg="gray", text="Scissors", height=10, width=15, font="Times 20 bold")
scissorsbutton.place(x=200, y=210)
label2 = Label(bg="black", fg="white", text="The AI chose: ", font="Times 15 ")
label2.place(x=400, y=50)

root.mainloop()