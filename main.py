from frame import Frame
import tkinter as tk
from tkinter.filedialog import askopenfilename

def main():
    tk.Tk().withdraw() 
    file_path = askopenfilename()

    frame = Frame(file_path)

main()