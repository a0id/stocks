from tkinter import *
from tool import quote

class GUI:
    def __init__(self):
        '''
        fg = '#f39e26' # Bloomberg orange
        bg = 'black'
        '''
        self.font = ('Arial', 18) # Default font size
        
        self.fg = 'black'
        self.bg = 'white'

    def start(self):
        self.make_window()
        self.make_gui()
        self.w.mainloop()
    
    def make_window(self):
        # Make and setup the w
        self.w = Tk()
        self.w.geometry('640x960')
        self.w.configure(bg=self.bg)
        self.w.title('Quoter')
    
    def make_gui(self):
        # Make the header
        header = Label(self.w, text='Quoter', fg=self.fg, bg=self.bg, font=('Arial Bold', 50)) \
            .grid(column=0, row=0)
    
        # Make the input label
        Label(self.w, text='Symbol: ', fg=self.fg, bg=self.bg, font=self.font) \
            .grid(column=0, row=2)
    
        # Make the textbox
        self.ticker_box = Entry(self.w, fg=self.fg, bg=self.bg, font=self.font)
        self.ticker_box.grid(column=1, row=2)
        
        # Make the get quote button
        Button(
            self.w, text='Get Quote',
            fg=self.fg, bg=self.bg,
            font=self.font,
            command=self.get_quote,
        ).grid(column=2, row=2)

    def get_quote(self):
        symbol = self.ticker_box.get()
        q = quote(symbol.upper())
        print(q)

gui = GUI()
gui.start()

