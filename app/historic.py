import tkinter


def add_historic(historic):
    global historic_screen
    historic_screen.append(historic)


def show_historic(text, screen, window):
    if text.get('active') != 'HISTORIC:':
        screen.set((text.get('active')).split(' =')[0])
        window.destroy()


def open_historic(screen):
    window = tkinter.Toplevel()
    window.geometry('300x290')
    window.resizable(width=False, height=False)

    scrollbar_y = tkinter.Scrollbar(window, orient='vertical')
    scrollbar_y.pack(side="right", fill="y")

    scrollbar_x = tkinter.Scrollbar(window, orient='horizontal')
    scrollbar_x.pack(side="bottom", fill="x")

    text = tkinter.Listbox(window, yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set,
                           font='Arial 15', width=300, justify='center')

    global historic_screen
    for item in historic_screen:
        text.insert("end", item)

    text.pack(fill="y")

    scrollbar_y.config(command=text.yview)
    scrollbar_x.config(command=text.xview)

    tkinter.Button(window, font='Arial 15', text='RETURN', command=lambda: show_historic(text, screen, window)).pack()


historic_screen = ['HISTORIC:']
