import tkinter as tk # lib for สร้าง Desktop App

def set_massage():
    text=text_input.get()
    title_label.configure(text=text)

window = tk.Tk() 
window.title('App PY') # ชื่อ window
window.minsize(width=400,height=400) # window ขนาดตำ่สุด

title_label = tk.Label(master=window,text='love love') # สร้าง label text
title_label.pack() # use label

text_input=tk.Entry(master=window) # สร้างช่อง input text
text_input.pack()

ok_btn=tk.Button(master=window,text='enter',command=set_massage) # สร้าง button
ok_btn.pack()

window.mainloop() # ให้ app run


