import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "pdptest.ui")

class PdptestApp:
    def __init__(self, master=None):
        # build ui
        self.introframe = tk.Frame(master)
        self.heading = tk.Label(self.introframe)
        self.heading.configure(font='{ubuntu} 20 {bold underline}', text='Welcome to PDP Sales Analysis!')
        self.heading.place(anchor='center', relx='0.5', rely='0.1', x='0', y='0')
        self.dbsel = tk.Label(self.introframe)
        self.dbsel.configure(font='{ubuntu} 12 {}', text='Enter Database File Path: ')
        self.dbsel.place(anchor='w', relx='0.1', rely='0.5', x='0', y='0')
        self.fileloctext = tk.Entry(self.introframe)
        _text_ = '''DataBaseFilePath'''
        self.fileloctext.delete('0', 'end')
        self.fileloctext.insert('0', _text_)
        self.fileloctext.place(anchor='w', relx='0.415', rely='0.5', width='450', x='0', y='0')
        self.browsebtn = tk.Button(self.introframe)
        self.browsebtn.configure(text='Browse')
        self.browsebtn.place(anchor='nw', height='50', relx='0.5', rely='0.6', width='150', x='0', y='0')
        self.filelocsubmit = tk.Button(self.introframe)
        self.filelocsubmit.configure(text='Enter')
        self.filelocsubmit.place(anchor='nw', height='50', relx='0.73', rely='0.6', width='150', x='0', y='0')
        self.introframe.configure(height='450', width='800')
        self.introframe.pack(side='top')

        # Main widget
        self.mainwindow = self.introframe
    

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = PdptestApp(root)
    app.run()

