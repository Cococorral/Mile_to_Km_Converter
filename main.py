from tkinter import *

def mile_to_km():
    val = speed.get()
    km = float(val) * 1.61
    solution_l.config(text=km)



#Window
window = Tk()
window.title("Mile to Km converter")
window.minsize(width=500, height=300)

#Labels
miles_l = Label(text="Miles", font=("Arial", 24, "bold"))
miles_l.grid(column=2, row=0)

km_l = Label(text="Km", font=("Arial", 24, "bold"))
km_l.grid(column=2, row=1)

equal_to_l = Label(text="is equal to", font=("Arial", 24, "bold"))
equal_to_l.grid(column=0, row=1)

solution_l = Label(text="0", font=("Arial", 24, "bold"))
solution_l.grid(column=1, row=1)

#Entry
speed = Entry()
speed.grid(column=1, row=0)


#Button
action = Button(text="Convert", command=mile_to_km)
action.grid(column=1, row=2)






window.mainloop()
