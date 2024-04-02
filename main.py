from tkinter import *
from tkinter import ttk

#*----- cores -----*#
color0 = "#f0f3f5"  # Preta
color1 = "#feffff"  # branca
color2 = "#4fa882"  # verde
color3 = "#38576b"  # valor
color4 = "#403d3d"   # letra preto
color5 = "#e06636"   # - profit
color6 = "#038cfc"   # azul
color7 = "#ef5350"   # vermelha
color8 = "#263238"   # + verde
color9 = "#e9edf5"   # sky blue
color10 = "#ff8c00"   # laranja

#*----- create janela -----*#
main = Tk()
main.title('Agenda de Contatos')
main.geometry('1080x470')
main.configure(background=color9)
main.resizable(width=FALSE, height=FALSE)

class Agenda():
    def __init__(self, main):
        
        #*----- frames -----*#
        frame_cima = Frame(main, width=310, height=50, bg=color10)
        frame_cima.grid(row=0, column=0)
        
        frame_baixo = Frame(main, width=310, height=420, bg=color1)
        frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)
        
        frame_direita = Frame(main, width=760, height=470, bg=color1)
        frame_direita.grid(row=0, column=1, pady=1, padx=1, rowspan=2, sticky=NSEW)
        
        #*----- textos e inputs -----*#
        app_title = Label(frame_cima, text='Agenda de Contatos', anchor=NW, fg=color1, bg=color10, relief='flat', font='Ive 15 bold')
        app_title.place(x=10, y=10)
        
        l_nome = Label(frame_baixo, text='Nome*', anchor=NW, fg=color4, bg=color1, relief='flat', font='Ive 12 bold')
        l_nome.place(x=10, y=10)
        e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
        e_nome.place(x=15, y=40)
        
        l_sobreNome = Label(frame_baixo, text='Sobre Nome*', anchor=NW, fg=color4, bg=color1, relief='flat', font='Ive 12 bold')
        l_sobreNome.place(x=10, y=60)
        e_sobreNome = Entry(frame_baixo, width=45, justify='left', relief='solid')
        e_sobreNome.place(x=15, y=90)
        
        l_email = Label(frame_baixo, text='Email*', anchor=NW, fg=color4, bg=color1, relief='flat', font='Ive 12 bold')
        l_email.place(x=10, y=110)
        e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
        e_email.place(x=15, y=140)
        
        l_telefone = Label(frame_baixo, text='Telefone*', anchor=NW, fg=color4, bg=color1, relief='flat', font='Ive 12 bold')
        l_telefone.place(x=10, y=160)
        e_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
        e_telefone.place(x=15, y=190)
        
        #*----- botões -----*#
        b_inserir = Button(frame_baixo, text='Inserir', width=10, anchor=CENTER, fg=color1, bg=color2, relief='raised', overrelief='ridge', font='Ive 10 bold')
        b_inserir.place(x=15, y=370)
        
        b_editar = Button(frame_baixo, text='Editar', width=10, anchor=CENTER, fg=color1, bg=color6, relief='raised', overrelief='ridge', font='Ive 10 bold')
        b_editar.place(x=110, y=370)
        
        b_excluir = Button(frame_baixo, text='Excluir', width=10, anchor=CENTER, fg=color1, bg=color7, relief='raised', overrelief='ridge', font='Ive 10 bold')
        b_excluir.place(x=205, y=370)
        
        #*----- frame direita / TreeView -----*#
        contatos = [[1,'João', 'da Silva', 'joao@email.com', 123456789],
                    [2,'João', 'da Silva', 'joao@email.com', 123456789],
                    [3,'João', 'da Silva', 'joao@email.com', 123456789],]

        # lista cabeçalho
        tabela_header = ['ID', 'Nome', 'Sobre Nome', 'Email', 'Telefone']
        
        # criando a tabela
        treeview = ttk.Treeview(frame_direita, selectmode='extended', columns=tabela_header, show='headings')
        # criando o scroll lateral
        yscroll = ttk.Scrollbar(frame_direita, orient='vertical', command=treeview.yview)
        # criando o scroll de baixo
        xscroll = ttk.Scrollbar(frame_direita, orient='horizontal', command=treeview.xview)
        
        # aplicando os scrolls
        treeview.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        
        # posições da tabela no frame direito
        treeview.grid(column=0, row=0, sticky='nsew')
        # scroll da vertical
        yscroll.grid(column=1, row=0, sticky='ns')
        # scroll da horizontal
        xscroll.grid(column=0, row=1, sticky='ew')
        
        frame_direita.grid_rowconfigure(0, weight=12)
        
        # configurando header e posição do texto dentro (nort-west (norte e oeste))
        header = ['nw','nw','nw','nw','nw']
        w = [30,170,170,170,170]
        n=0
        
        # loop para ajustar a tabela, junto com o cabeçalho e e o tamalho de cada coluna 
        for col in tabela_header:
            treeview.heading(col, text=col.title(), anchor=CENTER)
            treeview.column(col, width=w[n], anchor=header[n])
            n+=1
        
        # pega os contatos da lista e adiciona na tabela / TreeView
        for contato in contatos:
            treeview.insert('', 'end', values=contato)

agenda = Agenda(main)

main.mainloop()