import winsound
from tkinter import *
import time
from tkinter import ttk

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

root = Tk()
root.title("MorseTk")
root.geometry("380x180")
e = Entry(root, width=50, borderwidth=5)
e.pack()
e.get()
e.insert (0, "Enter your message: ")

o = Entry (root, width=50, borderwidth=5)
o.pack()
o.insert (0, "Translated message: ")


my_progress = ttk.Progressbar(root, orient=HORIZONTAL,
                              length=300, mode="determinate")
my_progress.pack(pady=20)


def myClick():
    my_progress['value'] = 0
    translated = morse(e.get())
    o.delete(0, END)
    o.insert(0, translated)


def play_coded_message():
    length = len(output)
    my_progress['value'] = 0
    for i in output:
        if i == '.':
            my_progress['value'] += 100 / length
            root.update_idletasks()
            winsound.Beep(1000, 100)  # Beep at 1000 Hz for 100 ms
            time.sleep(0.1)
        elif i == '-':
            my_progress['value'] += 100 / length
            root.update_idletasks()
            winsound.Beep(1000, 600)  # Beep at 1000 Hz for 100 ms
            time.sleep(0.1)
        elif i == ' ':
            my_progress['value'] += 100 / length
            root.update_idletasks()
            pass
    root.update_idletasks()

myButton = Button(root, text="Translate it to Morse!", command=myClick)
myButton.pack()

playsound = Button(root, text="Play it", command=play_coded_message)
playsound.pack()

root.mainloop()
