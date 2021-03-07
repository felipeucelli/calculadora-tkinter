# -*- coding: utf-8 -*-

# @autor: Felipe Ucelli
# @github: github.com/felipeucelli

# Built-in
import tkinter

historic_screen = ['HISTORIC:']


class Historic:
    """
    Classe responsável por gerar o histórico das operações aritméticas
    """

    def __init__(self):
        global historic_screen
        self.historic_screen = historic_screen
        self.config = ''

    def add_historic(self, historic):
        """
        Responsável por adicionar as operações aritméticas na lista 'historic_screen'
        :param historic: Valor a ser adicionado ao histórico
        :return:
        """
        self.historic_screen.append(historic)

    @staticmethod
    def show_historic(text, screen, window):
        """
        Responsável por retornar o valor selecionado para o input
        :param text: Listbox do histórico
        :param screen: input
        :param window: TopLevel do histórico
        :return:
        """
        if text.get('active') != 'HISTORIC:':
            screen.set((text.get('active')).split(' =')[0])
            window.destroy()

    def open_historic(self, screen, config):
        """
        Instânciação da interface do histórico
        :param config: Configuração e temas
        :param screen: input
        :return:
        """
        self.config = config
        window = tkinter.Toplevel()
        window.geometry('310x305')
        window.resizable(width=False, height=False)
        window['bg'] = self.config['root']['bg']

        # Instânciação do scrollbar vertical
        scrollbar_y = tkinter.Scrollbar(window, orient='vertical')
        scrollbar_y.pack(side="right", fill="y")

        # Instânciação do scrollbar horizontal
        scrollbar_x = tkinter.Scrollbar(window, orient='horizontal')
        scrollbar_x.pack(side="bottom", fill="x")

        # Instânciação do Listbox do histórico
        text = tkinter.Listbox(window, cnf=[self.config['listbox_historic']],
                               yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # Adiciona os itens da lista 'historic_screen' no Listbox
        for item in self.historic_screen:
            text.insert("end", item)

        text.pack(fill="y")

        scrollbar_y.config(command=text.yview)
        scrollbar_x.config(command=text.xview)

        # Instânciação do botão de retorno para o input
        btn_show_historic = tkinter.Button(window, self.config['btn_return_historic'])

        # Evento do botão de retorno
        btn_show_historic['command'] = lambda: self.show_historic(text, screen, window)

        # Distribuição do botão de retorno com o gerenciador de layout grid()
        btn_show_historic.pack()
