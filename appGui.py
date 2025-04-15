import tkinter

window = tkinter.Tk()
window.geometry("400x400")
name_var = tkinter.StringVar()


def change_name():
  greeting_name.configure(text="Hello " + name_var.get())


greeting_name = tkinter.Label(window, text="Hello", font=("Arial", 18), padx=10, pady=10)
greeting_name.pack()

name = tkinter.Entry(window, font=("Arial", 16), textvariable=name_var)
name.pack(padx=5, ipady=5)

change_name_btn = tkinter.Button(window, text="Change Name", font=("Arial", 16), command=change_name)
change_name_btn.pack(padx=5, pady=5)

window.mainloop()
