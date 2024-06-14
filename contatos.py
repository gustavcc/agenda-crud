import os
from colorama import Fore
import tkinter as ttk
from db import AgendaDB
#teste

class Contatos():
    
    banco = AgendaDB()
    
    __slots__ = ['__nome','__sobreNome','__telefone','__email']
    
    def __init__ (self,nome,sobreNome,telefone,email):
        self.setNome(nome)
        self.setSobreNome(sobreNome)
        self.setTelefone(telefone)
        self.setEmail(email)
    
    def getNome(self):
        return self.__nome
    def getSonbreNome(self):
        return self.__sobreNome
    def getTelefone(self):
        return self.__telefone
    def getEmail(self):
        return self.__email
    
    def setNome(self, novoNome):
        # print(Fore.BLACK, 'opa', Fore.RESET)
        if novoNome=='' or novoNome==' ' or not novoNome:
            self.__nome = 'Vazio'
        else:
            self.__nome = novoNome
    
    def setSobreNome(self, novoSobreNome):
        if novoSobreNome=='' or novoSobreNome==' ' or not novoSobreNome:
            self.__sobreNome = 'Vazio'
        else:
            self.__sobreNome = novoSobreNome
    
    def setTelefone(self, novoTelefone):
        try:
            if novoTelefone=='' or novoTelefone==' ' or len(novoTelefone)<10 or len(novoTelefone)>11 or self.contemLetras(novoTelefone) or self.contemCaracteresEspeciais(novoTelefone):
                self.__telefone = 'Telefone inválido'
            else:
                self.__telefone = novoTelefone
        except ValueError: 
            self.__telefone = 'Telefone Inválido 111'
    
    def setEmail(self, novoEmail):
        if novoEmail=='' or not novoEmail or novoEmail==' ' or not '.com' in novoEmail or not '@' in novoEmail:
            self.__email = 'Email inválido'
        else:
            self.__email = novoEmail
    
    def contemLetras(self, str):
        for letter in str:
            if 'a'<= letter <= 'z' or 'A'<= letter <= 'Z':
                return True
        return False
    
    def contemCaracteresEspeciais(self, str):
        especial = '!@#$%¨&*?:;'
        for e in especial:
            if e in str:
                return True 
                break
        return False
