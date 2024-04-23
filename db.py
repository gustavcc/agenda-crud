import sqlite3
from colorama import Fore

#*----- cennection .db -----*#
<<<<<<< HEAD
class ConnAgenda():
=======
class ConnectDB():
>>>>>>> 9563ffdaae6133f4af37c9b8056838dcd03f2a2b
    def __init__(self,path):
        self.connection = None
<<<<<<< HEAD
        self.path = path
    
    def connect(self):
        # while (not '.db' in self.path):
        if '.db' in self.path:
            try:
                self.connection = sqlite3.connect(self.path)
                print(Fore.GREEN+'Conexão estabelacida com sucesso!'+Fore.RESET)
                self.cursor = self.connection.cursor()
            except sqlite3.Error as e:
                print(Fore.RED,'Erro na conexão do banco: ',e,Fore.RESET)
        else:
            print(Fore.RED,'Esse banco de dados não existe!',Fore.RESET)
=======
        try:
            #*---- set connection ----*#
            self.connection = sqlite3.connect(self.path)
            print(Fore.GREEN+'Conexão estabelacida com sucesso!'+Fore.RESET)
            # return self.connection
        except sqlite3.Error as e:
            print(Fore.RED,'Erro na conexão do banco: ',e,Fore.RESET)
        self.connection.close() 
>>>>>>> 9563ffdaae6133f4af37c9b8056838dcd03f2a2b
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
            print(Fore.GREEN+'Conexão encerrada com sucesso!'+Fore.RESET)
        else:
            print(Fore.RED+'Não há conexão estabelecida!'+Fore.RESET)
<<<<<<< HEAD
    
    def criarTabela(self):
        try: 
            self.connect()
            querry = f'''CREATE TABLE IF NOT EXISTS Contatos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(45) NOT NULL,
                sobreNome VARCHAR(100) NOT NULL,
                telefone VARCHAR(20) NOT NULL,
                email VARCHAR(100) NOT NULL
            );'''
            self.cursor.execute(querry)
            print(Fore.GREEN+'\nTabela criada!\n'+Fore.RESET)
            self.disconnect()
=======
    #*---- create, delete and update ----*#
    def create(self,):
        
    def querryCUD(self, sqlQuerry):
        try:
            #*---- set cursor that go crete a pointer taht for each line in querry to add in .db ----*#
            cursor = self.connection.cursor()
            cursor.execute(sqlQuerry)
            self.connection.commit()
>>>>>>> 9563ffdaae6133f4af37c9b8056838dcd03f2a2b
        except sqlite3.Error as e:
            print(Fore.RED,'Erro ao criar tabela: ',e,Fore.RESET)
    
    def inserirContato(self, nome,sobreNome,telefone,email):
        try:
            self.connect()
            querry = '''INSERT INTO Contatos (nome, sobreNome, telefone, email)
                            VALUES (?,?,?,?);'''
            self.cursor.execute(querry,(nome,sobreNome,telefone,email))
            self.connection.commit()
            print(Fore.GREEN+'\nContato inserido!\n'+Fore.RESET)
            self.disconnect()
        except sqlite3.Error as e:
            print(Fore.RED,'Erro ao inserir registro: ',e,Fore.RESET)
        
    def editarContato(self, id,nome,sobreNome,telefone,email):
        try:
            self.connect()
            querry = '''UPDATE Contatos SET nome=?,sobreNome=?,telefone=?,email=? WHERE id=?;'''
            self.cursor.execute(querry,(nome,sobreNome,telefone,email,id))
            self.connection.commit()
            print(Fore.GREEN+'\nContato editado!\n'+Fore.RESET)
            self.disconnect()
        except sqlite3.Error as e:
            print(Fore.RED,'Erro ao editar registro: ',e,Fore.RESET)
            
    def excluirContato(self,id):
        try:
            self.connect()
            querry = '''DELETE FROM Contatos WHERE id=?;'''
            self.cursor.execute(querry,(id,))
            self.connection.commit()
            print(Fore.GREEN+'\nContato excluido!\n'+Fore.RESET)
            self.disconnect()
        except sqlite3.Error as e:
            print(Fore.RED,'Erro ao editar registro: ',e,Fore.RESET)
    def mostrarContatos(self):
        try:
            self.connect()
            querry = '''SELECT * FROM Contatos;'''
            self.cursor.execute(querry)
            contatos = self.cursor.fetchall()
            for contato in contatos:
                print(contato)
            self.disconnect()
        except sqlite3.Error as e:
            print(Fore.RED,'Erro ao editar registro: ',e,Fore.RESET)



#*---- execute test main ----*#
<<<<<<< HEAD
if __name__ == '__main__':
    db = ConnAgenda('agenda.db')
    db.criarTabela()
    db.excluirContato(2)
=======
# if __name__ == '__main__':
#     db = ConnectAgenda('agenda.db')
#     db.connect()
    
#     insertSQL = f'''INSERT INTO Contatos (nome, sobreNome, telefone, email)
#                     VALUES ('Gustavo', 'Cardoso', '(77)98650782', 'gustavo@email.com')'''
    
#     deleteSQL = f'''DELETE FROM Contatos WHERE id > 0'''

#     updateSQL = f'''UPDATE Contatos SET nome='Maria', email='maria@email.com' WHERE id=6'''

#     querry = AgendaQuerry(db.connection)
#     querry.querryCUD(updateSQL)

#     db.discnnect()
>>>>>>> 9563ffdaae6133f4af37c9b8056838dcd03f2a2b
