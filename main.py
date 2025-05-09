import tkinter as tk
from tkinter import *
from functools import partial

import pages.home as home
import pages.grid as grid
import pages.filters as filt_
import pages.song as song_
import pages.random as random
import pages.spotify as spotify

class app:
    
    # Initialization
    def __init__(self, window):
        self.window = window
        self.window.geometry("1280x1024")
        self.home()


    # Initialize each page
    def page_swap(self, *args, **kwargs):
        for i in self.window.winfo_children():
            i.destroy()
        self.page = Frame(self.window, width=1280, height=1024,)
        self.page.pack()


    ### PAGES ###

    def home(self):
        self.page_swap()
        home.home(self)

    def grid(self, filters, sort_method):
        self.page_swap()
        grid.grid(self,filters,sort_method)

    def filt(self):
        self.page_swap()
        filt_.filt(self)

    def song_page(self, song):
        self.page_swap()
        song_.song_page(self,song)

    def random(self):
        self.page_swap()
        random.random(self)

    def spotify(self):
        self.page_swap()
        spotify.spotify(self)


# Run tkinter Program
program = tk.Tk()
app(program)
program.mainloop()