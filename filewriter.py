from tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def write_to_file(data):
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    file_name = asksaveasfilename() # show an "Open" dialog box and return the path to the selected file
    print(file_name)
    file = open(file_name + ".json","w") 
    file.write(data)
    file.close() 
