from tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename

def write_to_file(data):
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    file_name = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(file_name)
    file = open(file_name,"w") 
    file.write(data)
    file.close() 
