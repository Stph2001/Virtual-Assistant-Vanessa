import threading
from tkinter import *
from speaking import speak
import os
from voice import Speech_Recognition
import pygame

pygame.mixer.init()
pygame.mixer.music.load("sound.mp3")

def user(ans):
    textF.delete(0, END)
    textF.insert(0, ans)
    query = textF.get()
    msgs.insert(END, "you : " + query+ "\n")
    textF.delete(0, END)
    msgs.yview(END)

def botAnswer(ans):
    speak(ans)
    msgs.insert(END, "bot : " + ans + '\n')
    textF.delete(0, END)
    msgs.yview(END)

def ask_from_bot():
    userText = textF.get()
    user(userText)

def on_closing():
    os._exit(0)

main = Tk()
main.geometry("500x650")
main.title("My Chatbot")
img = PhotoImage(file="bot1.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)
main.protocol("WM_DELETE_WINDOW", on_closing)

frame = Frame(main)
sc = Scrollbar(frame)
msgs = Text(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
# creating text field
textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)
btn = Button(main, text="Send", font=("Verdana", 20), command=ask_from_bot)
btn.pack()
# creating a function
def enter_function(event):
    btn.invoke()
# going to bind main window with enter key...
main.bind('<Return>', enter_function)

t1 = threading.Thread(target=Speech_Recognition)
t1.start()
main.mainloop()

    

