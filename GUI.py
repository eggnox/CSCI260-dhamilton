import tkinter as tk

def button_clicked():
    global outputArea
    global txtId
    """This function is called when the button is pressed."""
    #print("Button was clicked!")
    outputArea.delete(1.0,tk.END)
    outputArea.insert(tk.END,"Button was Clicked\n"+txtId.get(1.0,tk.END))

def showLocations():
    global outputArea
    global selected
    #print("Data would be here")
    outputArea.delete(1.0,tk.END)
    outputArea.insert(tk.END,"Data would be here\n"+selected.get())

# Create the main window
root = tk.Tk()
root.title("Button Example")
root.geometry("300x600") # Set window size
root.grid_columnconfigure(0, weight=1, uniform='col')
root.grid_columnconfigure(1, weight=1, uniform='col')

# Create a button widget
# The 'command' argument links the button to the 'button_clicked' function
button = tk.Button(root, text="Click Me!", command=button_clicked)
showButton=tk.Button(root, text="Show Locations", command=showLocations )
outputArea = tk.Text(root, height=10, width=40)
labelId = tk.Label(root,text="Input Id")
txtId = tk.Text(root, height=1)

items = ["-","Karl","Was","Here"]
#var = tk.StringVar()
#var.set(items)
label2Id = tk.Label(root,text="Drop Down Demo")
selected=tk.StringVar(value="-")
lb=tk.OptionMenu(root,selected , *items)

# Pack the button into the window
# 'pack()' is a simple geometry manager to place widgets
#button.pack(pady=2) # Add some vertical padding
#showButton.pack(pady=2)
#outputArea.pack(pady=2)
#labelId.pack(pady=2)
#txtId.pack(pady=2)
#label2Id.pack(pady=2)
#lb.pack(pady=2)
button.grid(row=0,column=0)
showButton.grid(row=0,column=1)
outputArea.grid(row=1,column=0,columnspan=2,sticky="ew")
labelId.grid(row=2,column=0)
txtId.grid(row=2,column=1)
label2Id.grid(row=3,column=0)
lb.grid(row=3,column=1,stick="ew")

# Start the Tkinter event loop
root.mainloop()