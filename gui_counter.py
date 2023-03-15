#import tkinter
import tkinter as tk

#make function which count chars in string
def counter(event):
    event = input.get()
    label.config(text = f"There are {len(event)} elements")

#make main window
window = tk.Tk()
window.geometry("400x300")
window.title("Counter")
window.config(bg="#68D1BC")

#make box for user to write
input = tk.Entry(window, bd=3, bg="#3C93B0", font=("Aerial", 12), fg="white", justify="center")
input.place(relx=0.5, rely=0.3, anchor="center")

#make label with text
label = tk.Label(window, text="Write something and see the length", bg="#91E4D3")
label.place(relx=0.5, rely=0.4, anchor="center")

#bind function
input.bind("<Enter>", counter)

window.mainloop()
