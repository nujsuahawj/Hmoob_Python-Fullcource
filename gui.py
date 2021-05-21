import tkinter as tk
def set_message():
    text=text_imput.get()
    title_label.configure(text=text)
window=tk.Tk()
window.title('nujsua')
window.minsize(width=400, height=300)

title_label = tk.Label(master=window, text='nujsua hawj')
title_label.pack()


text_imput = tk.Entry(master=window)
text_imput.pack()
ok_button = tk.Button(master=window, text='okey', command=set_message)
ok_button.pack()

window.mainloop()