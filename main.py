import winsound
from tkinter import *
import time


def morse(message):
    global output
    morze_alphabet = (
        " .- ", " -... ", " -.-. ", " -.. ", " . ", " ..-. ", " --. ", " .... ", " .. ", " .--- ", " -.- ", " .-.. ",
        " -- ",
        " -. ",
        " --- ", " .--. ", " --.- ", " .-. ", " ... ", " - ", " ..- ", " ...- ", " .-- ", " -..- ", " -.-- ", " --.. ",
        " / ")
    alphabet = (
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z", " ")
    a = []
    splited = list(message.lower())
    for letters in range(len(splited)):
        a.append(morze_alphabet[alphabet.index(splited[letters])])
        output = ''.join(a)
    return output

def sound(message):
    for i in message:
        if i == '.':
            winsound.Beep(1000, 100)  # Beep at 1000 Hz for 100 ms
            time.sleep(0.1)
        elif i == '-':
            winsound.Beep(1000, 600)  # Beep at 1000 Hz for 100 ms
            time.sleep(0.1)
        elif i == ' ':
            pass



root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.get()
e.insert (0, "Enter your message: ")



def myClick():
    translated = morse(e.get())
    myLabel = Label(root, text=translated)
    myLabel.pack()


def play_coded_message():
    sound(output)




myButton = Button(root, text="Translate it to morse!", command=myClick)
myButton.pack()


playsound = Button(root, text="Play it", command=play_coded_message)
playsound.pack()




root.mainloop()
