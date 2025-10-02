import tkinter as tk

def button_clicked():
    
    #print("Button was clicked!")
    outputArea.insert(tk.END,"button was clicked")

def showLocation():
    global outputArea
    print("Data would be here")
    outputArea.delete(1.0,Tk.END)
    outputArea.insert(1.0,"Data would be here")

root = tk.Tk()
root.title("Button Example")
root.geometry("300x400")

button = tk.Button(root, text="Click Me!", command=button_clicked)
showButton = tk.Button(root,text="show Location", command = showLocation)
outputArea = tk.Text(root, height = 10, width=40)
labelID = tk.Label(root, "inputId")
txtID = tk.Text(root)

button.pack(pady=50)
showButton.pack(pady=20)
outputArea.pack(pady=2)
labelID.pack(pady=2)
txtID.pack(pady=2)
root.mainloop()