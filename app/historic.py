import tkinter

historic_screen = ['HISTORIC']


class Historic:
    def __init__(self):
        global historic_screen
        self.historic_screen = historic_screen

    def add_historic(self, historic):
        self.historic_screen.append(historic)

    @staticmethod
    def show_historic(text, screen, window):
        if text.get('active') != 'HISTORIC:':
            screen.set((text.get('active')).split(' =')[0])
            window.destroy()

    def open_historic(self, screen):
        window = tkinter.Toplevel()
        window.geometry('300x290')
        window.resizable(width=False, height=False)

        scrollbar_y = tkinter.Scrollbar(window, orient='vertical')
        scrollbar_y.pack(side="right", fill="y")

        scrollbar_x = tkinter.Scrollbar(window, orient='horizontal')
        scrollbar_x.pack(side="bottom", fill="x")

        text = tkinter.Listbox(window, yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set,
                               font='Arial 15', width=300, justify='center')

        for item in self.historic_screen:
            text.insert("end", item)

        text.pack(fill="y")

        scrollbar_y.config(command=text.yview)
        scrollbar_x.config(command=text.xview)

        btn_show_historic = tkinter.Button(window, font='Arial 15', text='RETURN')
        btn_show_historic['command'] = lambda: self.show_historic(text, screen, window)
        btn_show_historic.pack()
