import os
from colorama import Fore
import tkinter as ttk
from db import AgendaDB


class Contatos():
    banco = AgendaDB()
    
    __slots__ = ['__nome','__sobreNome','__telefone','__email']
    
    def __init__ (self,nome,sobreNome,telefone,email):
        self.setNome(nome)
        self.setSobreNome(sobreNome)
        self.setTelefone(telefone)
        self.setEmail(email)
        self.erro = ttk.Tk()
    
    def getNome(self):
        return self.__nome
    def getSonbreNome(self):
        return self.__sobreNome
    def getTelefone(self):
        return self.__telefone
    def getEmail(self):
        return self.__email
    
    def setNome(self, novoNome):
            while True:
                if novoNome=='' or novoNome==' ':
                    print(self.linha)
                    novoNome = input('\nNome inválido.\nInsira um novo\n: ').strip()
                else:
                    break
            self.__nome = novoNome
    
    def setSobreNome(self, novoSobreNome):
            while True:
                if novoSobreNome=='' or novoSobreNome==' ':
                    print(self.linha)
                    novoSobreNome = input('\nNome inválido.\nInsira um novo\n: ').strip()
                else:
                    break
            self.__nome = novoSobreNome
    
    def setTelefone(self, novoTelefone):
            while True:
                try:
                    novoTelefone==float(novoTelefone)
                    if novoTelefone=='' or novoTelefone==' ' or float(novoTelefone)<0 or float(novoTelefone)==0:
                        print(self.linha)
                        novoTelefone = float(input('\nTelefone inválido.\nInsira um novo\n: ').strip())
                    else:
                        break
                except ValueError: 
                    print(self.linha)
                    novoTelefone = input('\nTelefone inválido.\nInsira um novo\n: ').strip()
                    continue
            self.__telefone = novoTelefone
    
    def setEmail(self, novoEmail):
            while True:
                try:
                    novoEmail==float(novoEmail)
                    if novoEmail=='' or novoEmail==' ' or float(novoEmail)<0 or float(novoEmail)==0:
                        print(self.linha)
                        novoEmail = float(input('\nEmail inválido.\nInsira um novo\n: ').strip())
                    else:
                        break
                except ValueError: 
                    print(self.linha)
                    novoEmail = input('\nEmail inválido.\nInsira um novo\n: ').strip()
                    continue
            self.__email = novoEmail