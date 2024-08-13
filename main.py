from tkinter import *


def handle_key_events(event=None):
    apply_style()
    reset_timer()


def apply_style(event=None):
    textbox.tag_add('style1', '1.0', 'end')
    textbox.tag_configure("style1", foreground="black", font=("Helvetica", 14, "normal"))


def reset_timer(event=None):
    global time_remaining
    global timer_id

    if timer_id:  # check if a timer already exists
        window.after_cancel(timer_id)  # delete existing timer

    time_remaining = 5
    update_timer()


def update_timer(event=None):
    global time_remaining
    global timer_id

    if time_remaining > 0:
        timer_label.config(text=f"Time Left: {time_remaining} seconds")
        time_remaining -= 1
        timer_id = window.after(1000, update_timer)  # identifies a new timer
    else:
        timer_label.config(text="Time's up!")
        clear_text()


def clear_text():
    textbox.delete("1.0", 'end')


def begin_writing():
    for widgets in window.winfo_children():
        widgets.destroy()

    type_here_label = Label(window, text="Type Here", font=("Helvetica", 20, "normal"))
    type_here_label.place(relx=0.5, rely=0.03, anchor=CENTER)

    global textbox
    textbox = Text(window, height=30, width=70, wrap='word')
    textbox.place(relx=0.5, rely=0.1, anchor=N)
    textbox.bind('<KeyRelease>', handle_key_events)

    global timer_label
    timer_label = Label(window, text="", font=("Helvetica", 14, "normal"))
    timer_label.place(relx=0.5, rely=0.9, anchor=CENTER)

    global time_remaining
    time_remaining = 5

    global timer_id
    timer_id = None



window = Tk()
window.geometry("700x700")
window.title("Disappearing Writing")

title_label = Label(window, text="Disappearing Writing", font=("Helvetica", 50, "normal"))
title_label.place(relx=0.5, rely=0.4, anchor=CENTER)

start_button = Button(window, text="Begin", font=("Helvetica", 25, "normal"), command=begin_writing)
start_button.place(relx=0.5, rely=0.6, anchor=CENTER)

# textbox = Text(window, height=10, width=40)
# textbox.pack(pady=15)
# textbox.tag_configure("style1", foreground="black", font=("Helvetica", 14, "normal"))
# textbox.bind('<KeyRelease>', apply_style)


window.mainloop()
