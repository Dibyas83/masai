
import tkinter as tk
from tkinter import ttk

#tk._test()
root = tk.Tk()
root.title("simp app")

def add_to_list(event = None):  # to type on the test entry  then click on add btn so that it appears on list box
    text = entry.get() #to grab the test and saved to text
    if text: # so that it doesnot print blank lines when clicked without typing
        text_list.insert(tk.END, text) # adds text value to end of list  at the end of the curr content of widget
        entry.delete(0, tk.END) # erases curr text from beg to end,so that new entry can be made

root.columnconfigure(0,weight=1) # to resize root window when expanded
root.columnconfigure(1,weight=3) # col on right expands more
root.rowconfigure(0,weight=1)

frame = ttk.Frame(root) # root is the parent window
#frame = tk.Frame(root) # root is the parent window
frame.grid(row=0,column=0,sticky="nsew",padx=5,pady=5) # added to app,frame is added to root window,sticky will make the frame stick to root window when expanded
#frame is a container for widgets ,widgets will be added to this frame instead of root window
# but we dontwant everything to expand ,like buttons
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

entry = ttk.Entry(frame) # using themed ttinker (inbuilt)
#entry = tk.Entry(frame)
entry.grid(row=0,column=0,sticky="ew") # it will grow sideways not vertically

# entry.bind("<Return>", lambda event: add_to_list()) # return at end of text will prompt event
entry.bind("<Return>", add_to_list) # return at end of text will prompt event

entry_btn = ttk.Button(frame,text="Add",command=add_to_list)
entry_btn.grid(row=0,column=1)

text_list = tk.Listbox(frame) # frame as parent window . listbox doesnt acceptk ttk
text_list.grid(row=1, column=0,columnspan=2,sticky="nsew")
"""
def om_click():
    lbl.config(text="button clicked !")

lbl = tk.Label(root, text="label 1")
lbl.grid(row=0, column=0)
# keyboard event to make entry without clicking add ,by ising bind method in entry wizard,this is event handling
print(lbl.config().keys())
btn = tk.Button(root, text="butn 1", command=om_click)
btn.grid(row=0, column=1)
"""
frame2 = ttk.Frame(root) # root is the parent window
frame2.grid(row=0,column=0,sticky="nsew",padx=5,pady=5) # added to app,frame is added to root window,sticky will make the frame stick to root window when expanded
#frame is a container for widgets ,widgets will be added to this frame instead of root window
# but we dontwant everything to expand ,like buttons
frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(1, weight=1)

entry = ttk.Entry(frame2)
entry.grid(row=0,column=0,sticky="ew") # it will grow sideways not vertically

# entry.bind("<Return>", lambda event: add_to_list()) # return at end of text will prompt event
entry.bind("<Return>", add_to_list) # return at end of text will prompt event

entry_btn = ttk.Button(frame2,text="Add",command=add_to_list)
entry_btn.grid(row=0,column=1)

text_list = tk.Listbox(frame2) # frame as parent window
text_list.grid(row=1, column=0,columnspan=2,sticky="nsew")
root.mainloop()

"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Simple App")


def add_to_list(event=None):
    text = entry.get()
    if text:
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

entry = ttk.Entry(frame)
entry.grid(row=0, column=0, sticky="ew")

entry.bind("<Return>", add_to_list)

entry_btn = ttk.Button(frame, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=1)

text_list = tk.Listbox(frame)
text_list.grid(row=1, column=0, columnspan=2, sticky="nsew")

frame2 = tk.Frame(root)
frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(1, weight=1)

entry = tk.Entry(frame2)
entry.grid(row=0, column=0, sticky="ew")

entry.bind("<Return>", add_to_list)

entry_btn = tk.Button(frame2, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=1)

text_list = tk.Listbox(frame2)
text_list.grid(row=1, column=0, columnspan=2, sticky="nsew")

root.mainloop()
"""









