from tkinter import *
import tool

class GUI:
    def __init__(self):
        '''
        fg = '#f39e26' # Bloomberg orange
        bg = 'black'
        '''
        self.font = ('Arial', 18) # Default font size
        
        self.fg = 'black'
        self.bg = 'white'

        self.width = 700
        self.height = 960

    def start(self):
        self.make_window()
        self.make_gui()
        self.w.mainloop()
    
    def make_window(self):
        # Make and setup the w
        self.w = Tk()
        self.w.geometry('{}x{}'.format(self.width, self.height))
        self.w.configure(bg=self.bg)
        self.w.title('Quoter')
    
    def make_gui(self):
        # Make the header
        header = Label(self.w, text='Quoter', fg=self.fg, bg=self.bg, font=('Arial Bold', 50)) \
            .grid(column=0, row=0)
    
        # Make the input label
        #Label(self.w, text='Symbol: ', fg=self.fg, bg=self.bg, font=self.font) \
        #    .grid(column=0, row=2)
    
        # Make the textbox
        self.ticker_box = Entry(self.w, fg=self.fg, bg=self.bg, font=self.font)
        self.ticker_box.grid(column=0, row=2)
        
        # Make the get quote button
        Button(
            self.w, text='Get Quote',
            fg=self.fg, bg=self.bg,
            font=self.font,
            command=self.get_quote,
        ).grid(column=1, row=2)

    def get_quote(self):
        symbol = self.ticker_box.get()
        q = tool.quote(symbol.upper())
        self.render_quote(q)

    def render_quote(self, q):
        t = Text(self.w, wrap='word', height=42)
        t.grid(column=0, row=3)
        t.insert(END, tool.bformat(q))

