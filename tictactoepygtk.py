import tkinter
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("500x500")
root.title("Tik Tac Toe V1.0 - by Israel Kinfu ")

label = tk.Label(root, text="Tik Tac Toe V1.0 ", font=('Arial', 18))
label.pack(padx=10, pady=10)

label = tk.Label(root, text="By: Israel Kinfu ", font=('Arial', 12))
label.pack()

label = tk.Label(root, text="using Tkinter", font=('Arial', 12))
label.pack()

# frm = ttk.Frame(root, padding=10)
# label = tk.Label(root, text="Hello World!", font=('Arial', 12))
# label.button(text="Quit", command=root.destroy)
# label.pack()

# button = tk.Button(root, text="X", font=('Arial', 20))
# button.pack(padx=5, pady=5)

# button = tk.Button(root, text="O", font=('Arial', 20))
# button.pack(padx=5, pady=5)
#
# button = tk.Button(root, text="X", font=('Arial', 20))
# button.pack(padx=5, pady=5)

ButtonFrame = tk.Frame(root)
ButtonFrame.columnconfigure(0, weight=1)
ButtonFrame.columnconfigure(1, weight=1)
ButtonFrame.columnconfigure(2, weight=1)

flag = True


def buttonpress(button):
    # label1 = tk.Label(root, text="Button Pressed", font=('Arial', 12))
    # label1.pack(padx=5, pady=10)
    # button1a = tk.Button(ButtonFrame, text="X", font=('Arial', 30))
    # button1a.grid(row=0, column=0, sticky=tk.W + tk.E)
    
    button.configure(text="X", font=('Arial', 30))

    
    # global flag
    # if not flag:
    #     button1a.configure(text=" ", font=('Arial', 30))
    # else:
    #     button1a.configure(text="O", font=('Arial', 30))
    #     print(flag)
    #     flag = False
    # button1a.configure(text="O", font=('Arial', 30))


button1a = tk.Button(ButtonFrame, text=" ", width=3, font=('Arial', 30), command=lambda:buttonpress(button1a))
button1a.grid(row=0, column=0, sticky=tk.W + tk.E)

button1b = tk.Button(ButtonFrame, text=" ", width=3, font=('Arial', 30), command=lambda:buttonpress(button1b))
button1b.grid(row=0, column=1, sticky=tk.W + tk.E)

button1c = tk.Button(ButtonFrame, text=" ", width=3, font=('Arial', 30), command=lambda:buttonpress(button1c))
button1c.grid(row=0, column=2, sticky=tk.W + tk.E)

button2a = tk.Button(ButtonFrame, text=" ", width=3, font=('Arial', 30), command=lambda:buttonpress(button2a))
button2a.grid(row=1, column=0, sticky=tk.W + tk.E)

button2b = tk.Button(ButtonFrame, text=" ", width=3, font=('Arial', 30), command=lambda:buttonpress(button2b))
button2b.grid(row=1, column=1, sticky=tk.W + tk.E)

button2c = tk.Button(ButtonFrame, text=" ", width=3, font=('Arial', 30), command=lambda:buttonpress(button2c))
button2c.grid(row=1, column=2, sticky=tk.W + tk.E)

button3a = tk.Button(ButtonFrame, text=" ", width=3, font=('Arial', 30), command=lambda:buttonpress(button3a))
button3a.grid(row=2, column=0, sticky=tk.W + tk.E)

button3b = tk.Button(ButtonFrame, text=" ", width=3, font=('Arial', 30), command=lambda:buttonpress(button3b))
button3b.grid(row=2, column=1, sticky=tk.W + tk.E)

button3c = tk.Button(ButtonFrame, text=" ", width=3, font=('Arial', 30), command=lambda:buttonpress(button3c))
button3c.grid(row=2, column=2, sticky=tk.W + tk.E)

ButtonFrame.pack(padx=20, pady=20)
root.mainloop()


