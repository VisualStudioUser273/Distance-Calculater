from tkinter import*
window=Tk()
window.geometry('600x600')
window.title('Distance Calculater')
window.config(background='maroon')


def calculate():
    speed=float(speed_e.get())
    time=float(time_e.get())
    output=(time*speed)
    output_l.config(text=str(output))
title_l=Label(window,text='Distance Calculater')
ins_l=Label(window,text='Imput the speed,time')
speed_e=Entry(window,width='30')
time_e=Entry(window,width='30')
output_l=Label(window,width='40',height='10')
go_b=Button(window,width='10',command=calculate)

title_l.pack()
ins_l.pack(pady=10)
speed_e.pack()
time_e.pack()
output_l.pack(pady=50)
go_b.pack()



window.mainloop()