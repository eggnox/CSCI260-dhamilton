import tkinter as tk

def button_clicked():
    global outputArea
    global txtID

    #print("Button was clicked!")
    outputArea.delete(1.0,tk.END)
    outputArea.insert(tk.END,"button was clicked")

def showLocation():
    global outputArea
    global txtID
    print("Data would be here")
    outputArea.delete(1.0,tk.END)
    outputArea.insert(tk.END,"Button was clicked")

root = tk.Tk()
root.title("Button Example")
root.geometry("300x600")

button = tk.Button(root, text="Click Me!", command=button_clicked)
showButton = tk.Button(root,text="show Location", command = showLocation)
outputArea = tk.Text(root, height = 10, width=40)
labelID = tk.Label(root,text = "inputId")
txtID = tk.Text(root)

items = ["karl","was","here"]
var = tk.StringVar()
var.set(items)
lb = tk.Listbox(root,listvariable=var)
tk.Listbox(root,listvariable=var).grid()

button.pack(pady=50)
showButton.pack(pady=20)
outputArea.pack(pady=2)
labelID.pack(pady=2)
txtID.pack(pady=2)
label2Id(pady=2)
lb.pack(pady=2)


root.mainloop()