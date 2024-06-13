from tkinter import *
import tkinter as tk
from tkinter import ttk
from db import AgendaDB
from contatos import Contatos

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
    
    banco = AgendaDB()
    
    def __init__(self, main):
        
        #*----- main frames -----*#
        self.frame_cima = Frame(main, width=310, height=50, bg=color6)
        self.frame_cima.grid(row=0, column=0)
        
        self.frame_baixo = Frame(main, width=310, height=420, bg=color1)
        self.frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)
        
        self.frame_direita = Frame(main, width=760, height=470, bg=color1)
        self.frame_direita.grid(row=0, column=1, pady=1, padx=1, rowspan=2, sticky=NSEW)
        
        #*----- labels e inputs -----*#
        self.app_title = Label(self.frame_cima, text='Agenda de Contatos', anchor=NW, fg=color1, bg=color6, relief='flat', font='Ive 15 bold')
        self.app_title.place(x=10, y=10)
        
        self.l_nome = Label(self.frame_baixo, text='Nome*', anchor=NW, fg=color4, bg=color1, relief='flat', font='Ive 12 bold')
        self.l_nome.place(x=10, y=10)
        self.e_nome = Entry(self.frame_baixo, width=45, justify='left', relief='solid')
        self.e_nome.place(x=15, y=40)
        
        self.l_sobreNome = Label(self.frame_baixo, text='Sobre Nome*', anchor=NW, fg=color4, bg=color1, relief='flat', font='Ive 12 bold')
        self.l_sobreNome.place(x=10, y=60)
        self.e_sobreNome = Entry(self.frame_baixo, width=45, justify='left', relief='solid')
        self.e_sobreNome.place(x=15, y=90)
        
        self.l_email = Label(self.frame_baixo, text='Email*', anchor=NW, fg=color4, bg=color1, relief='flat', font='Ive 12 bold')
        self.l_email.place(x=10, y=110)
        self.e_email = Entry(self.frame_baixo, width=45, justify='left', relief='solid')
        self.e_email.place(x=15, y=140)
        
        self.l_telefone = Label(self.frame_baixo, text='Telefone*', anchor=NW, fg=color4, bg=color1, relief='flat', font='Ive 12 bold')
        self.l_telefone.place(x=10, y=160)
        self.e_telefone = Entry(self.frame_baixo, width=45, justify='left', relief='solid')
        self.e_telefone.place(x=15, y=190)
        
        #*----- botões -----*#
        self.b_inserir = Button(self.frame_baixo, text='Inserir', width=10, anchor=CENTER, fg=color1, bg=color2, relief='raised', overrelief='ridge', font='Ive 10 bold', command = self.inserirContato)
        self.b_inserir.place(x=15, y=370)
        
        self.b_editar = Button(self.frame_baixo, text='Editar', width=10, anchor=CENTER, fg=color1, bg=color6, relief='raised', overrelief='ridge', font='Ive 10 bold', command = self.editarContato)
        self.b_editar.place(x=110, y=370)
        
        self.b_excluir = Button(self.frame_baixo, text='Excluir', width=10, anchor=CENTER, fg=color1, bg=color7, relief='raised', overrelief='ridge', font='Ive 10 bold', command = self.excluirContato)
        self.b_excluir.place(x=205, y=370)
    
    def inserirContato(self):
        if self.verificarEntrysInserir():
            contatoInsert = [self.e_nome.get(),self.e_sobreNome.get(),self.e_telefone.get(),self.e_email.get()]
            self.banco.inserirContatoDB(contatoInsert)
            
            cadastro = tk.Tk()
            cadastro.title('Cadastro')
            aviso = Label(cadastro, text="Contato cadastrado com sucesso!", foreground='green')
            aviso.grid(row=0, column=0, padx=20, pady=20)
            
            self.e_nome.delete(0, "end")
            self.e_sobreNome.delete(0, "end")
            self.e_email.delete(0, "end")
            self.e_telefone.delete(0, "end")
            
            self.mostrarContatos()
    
    def editarContato(self):
        pass
    
    def excluirContato(self):
        pass
    
    def verificarEntrysInserir(self):
        contato = Contatos(self.e_nome.get(), self.e_sobreNome.get(),self.e_telefone.get(),self.e_email.get())
        
        if self.banco.existeContatoDB(contato.getEmail(), contato.getTelefone()) or contato.getNome() == 'Vazio' or contato.getSonbreNome() == 'Vazio' or contato.getTelefone() == 'Telefone inválido' or contato.getEmail() == 'Email inválido':
            erro = tk.Tk()
            erro.title('Erro ao Inserir Contato')
            if contato.getNome() == 'Vazio' or contato.getSonbreNome() == 'Vazio':
                aviso1 = Label(erro, text='Algum campo está vazio! Preencha Todos os campos!', foreground='red')
                aviso1.grid(row=0, column=0, padx=20, pady=20)
            
            if contato.getTelefone() == 'Telefone inválido': 
                aviso3 = Label(erro, text='Telefone inválido!', foreground='red')
                aviso3.grid(row=2, column=0, padx=100, pady=20)
            if contato.getEmail() == 'Email inválido':
                aviso2 = Label(erro, text='Email inválido!', foreground='red')
                aviso2.grid(row=1, column=0, padx=100, pady=20)
            if self.banco.existeContatoDB(contato.getEmail(), contato.getTelefone()):
                aviso4 = Label(erro, text='Email ou telefone já existe!', foreground='red')
                aviso4.grid(row=3, column=0, padx=70, pady=20)
            return False
        return True
    
    #*----- frame direita / TreeView / lista de contatos-----*#
    def mostrarContatos(self):
        listaContatos = self.banco.mostrarContatosDB()

        # lista cabeçalho
        tabela_header = ['ID', 'Nome', 'Sobre Nome', 'Telefone', 'Email']
        
        # criando a tabela
        treeview = ttk.Treeview(self.frame_direita, selectmode='extended', columns=tabela_header, show='headings')
        # criando o scroll lateral
        yscroll = ttk.Scrollbar(self.frame_direita, orient='vertical', command=treeview.yview)
        # criando o scroll de baixo
        xscroll = ttk.Scrollbar(self.frame_direita, orient='horizontal', command=treeview.xview)
        
        # aplicando os scrolls
        treeview.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
        
        # posições da tabela no frame direito
        treeview.grid(column=0, row=0, sticky='nsew')
        # scroll da vertical
        yscroll.grid(column=1, row=0, sticky='ns')
        # scroll da horizontal
        xscroll.grid(column=0, row=1, sticky='ew')
        
        self.frame_direita.grid_rowconfigure(0, weight=12)
        
        # configurando header e posição do texto dentro (nort-west (norte e oeste))
        header = ['nw','nw','nw','nw','nw']
        w = [50,170,170,190,170]
        n=0
        
        # loop para ajustar a tabela, junto com o cabeçalho e o tamanho de cada coluna 
        for col in tabela_header:
            treeview.heading(col, text=col.title(), anchor=CENTER)
            treeview.column(col, width=w[n], anchor=header[n])
            n+=1
        
        # pega os contatos da lista e adiciona na tabela / TreeView
        for contato in listaContatos:
            treeview.insert('', 'end', values=contato)
    
agenda = Agenda(main)
agenda.mostrarContatos()
main.mainloop()