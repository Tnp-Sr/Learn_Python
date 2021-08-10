import tkinter as tk

def show_Mutiply():
    num = 0
    try:
        num = int(num_input.get())
        if num == 0:
            raise Exception()
    except:
        output_label.configure(text='ชีวิตมัน 0 เปล่า')
        return
    
    output = ''
    for i in range(1,13):
        output += str(num) + ' x ' + str(i) + ' = ' + str(num*i) + '\n'
    
    output_label.configure(text=output)

window = tk.Tk()
window.title('สูตรคูณ')
window.minsize(width=400,height=400)

title_label=tk.Label(master=window,text='สูตรคูณ',width=20)
title_label.pack(pady=10) # pady - เว้นแนวตั้ง , padx - เว้นแนวนอน

num_input=tk.Entry(master=window)
num_input.pack()

btn=tk.Button(master=window,text='enter num',command=show_Mutiply,width=10)
btn.pack(pady=5)

output_label=tk.Label(master=window)
output_label.pack(pady=10)


window.mainloop()



