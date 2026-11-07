import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "pdptest.ui")

class PdptestWidget(tk.Frame):
    def select(self):
	    self.fileloc = filedialog.askopenfilename(initialdir="/home/vishu/Downloads",
                                            title = "Select the database",
                                            )


    def __init__(self, master=None, **kw):
        super(PdptestWidget, self).__init__(master, **kw)
        self.heading = tk.Label(self)
        self.heading.configure(font='{ubuntu} 20 {bold underline}', text='Welcome to PDP Sales Analysis!')
        self.heading.place(anchor='center', relx='0.5', rely='0.1', x='0', y='0')
        self.dbsel = tk.Label(self)
        self.dbsel.configure(font='{ubuntu} 12 {}', text='Enter Database File Path: ')
        self.dbsel.place(anchor='w', relx='0.1', rely='0.5', x='0', y='0')
        self.fileloctext = tk.Entry(self)
        _text_ = '''DataBaseFilePath'''
        self.fileloctext.delete('0', 'end')
        self.fileloctext.insert('0', _text_)
        self.fileloctext.place(anchor='w', relx='0.415', rely='0.5', width='450', x='0', y='0')
        self.browsebtn = tk.Button(self)
        self.browsebtn.configure(text='Browse')
        self.browsebtn.place(anchor='nw', height='50', relx='0.5', rely='0.6', width='150', x='0', y='0')
        self.browsebtn.configure(command=self.select)
        self.filelocsubmit = tk.Button(self)
        self.filelocsubmit.configure(text='Enter')
        self.filelocsubmit.place(anchor='nw', height='50', relx='0.73', rely='0.6', width='150', x='0', y='0')

    
if __name__ == '__main__':
    root = tk.Tk()
    widget = PdptestWidget(root)
    widget.pack(expand=True, fill='both')
    root.mainloop()

