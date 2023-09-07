import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}

try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("tamil words and english meaning.csv")
    original_data.drop("Number", inplace=True, axis=1)
    df = original_data.to_dict(orient="records")
else:
    df = data.to_dict(orient="records")


def word():
    global current_word, flip_timer
    window.after_cancel(id=flip_timer)
    current_word = random.choice(df)
    canvas.itemconfig(title, text="Tamil", fill="black")
    canvas.itemconfig(random_word, text=current_word["Tamil"], fill="black")
    canvas.itemconfig(old_image, image=card_front_img)
    flip_timer = window.after(ms=3000, func=to_english)


def to_english():
    canvas.itemconfig(old_image, image=card_back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(random_word, text=current_word["in English"], fill="white")


def update():
    df.remove(current_word)
    print(len(df))
    after_del = pd.DataFrame(df)
    after_del.to_csv("words_to_learn.csv", index=False)
    word()


window = tkinter.Tk()
window.title("Flash Card Game")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(ms=3000, func=to_english)

canvas = tkinter.Canvas(width=800, height=526)
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")
old_image = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="", font=("ariel", 40, "italic"), fill="black")
random_word = canvas.create_text(400, 263, text="", font=("ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=word)
wrong_button.grid(row=1, column=0)

right_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=update)
right_button.grid(row=1, column=1)

word()

window.mainloop()

