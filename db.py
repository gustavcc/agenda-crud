import sqlite3
from colorama import Fore

class AgendaDB():
    def __init__(self):
        self.connection = None
    
    def connect(self):
        try:
            self.connection = sqlite3.connect('agenda.sqlite')
            print(Fore.GREEN+'Conexão estabelacida com sucesso!'+Fore.RESET)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(Fore.RED,'Erro na conexão do banco: ',e,Fore.RESET)
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
            print(Fore.GREEN+'Conexão encerrada com sucesso!'+Fore.RESET)
        else:
            print(Fore.RED+'Não há conexão estabelecida!'+Fore.RESET)
    
    def criarTabelaDB(self):
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
        except sqlite3.Error as e:
            print(Fore.RED,'Erro ao criar tabela: ',e,Fore.RESET)
        finally:
            self.disconnect()
    
    def inserirContatoDB(self, lista):
        try:
            self.connect()
            querry = '''INSERT INTO Contatos (nome, sobreNome, telefone, email)
                            VALUES (?,?,?,?);'''
            self.cursor.execute(querry,(lista))
            self.connection.commit()
            print(Fore.GREEN+'\nContato inserido!\n'+Fore.RESET)
        except sqlite3.Error as e:
            print(Fore.RED,'Erro ao inserir contato: ',e,Fore.RESET)
        finally:
            self.disconnect()
        
    def editarContatoDB(self, id,nome,sobreNome,telefone,email):
        try:
            self.connect()
            querry = '''UPDATE Contatos SET nome=?,sobreNome=?,telefone=?,email=? WHERE id=?;'''
            self.cursor.execute(querry,(nome,sobreNome,telefone,email,id))
            self.connection.commit()
            print(Fore.GREEN+'\nContato editado!\n'+Fore.RESET)
        except sqlite3.Error as e:
            print(Fore.RED,'Erro ao editar contato: ',e,Fore.RESET)
        finally:
            self.disconnect()
    
    def excluirContatoDB(self,id):
        try:
            self.connect()
            querry = '''DELETE FROM Contatos WHERE id=?;'''
            self.cursor.execute(querry,(id,))
            self.connection.commit()
            print(Fore.GREEN+'\nContato excluido!\n'+Fore.RESET)
        except sqlite3.Error as e:
            print(Fore.RED,'Erro ao excluir contato: ',e,Fore.RESET)
        finally:
            self.disconnect()
    
    def mostrarContatosDB(self):
        listaContatos = []
        try:
            self.connect()
            querry = '''SELECT * FROM Contatos;'''
            self.cursor.execute(querry)
            contatos = self.cursor.fetchall()
            for contato in contatos:
                listaContatos.append(contato)
            return listaContatos
        except sqlite3.Error as e:
            print(Fore.RED,'Erro ao mostrar contatos: ',e,Fore.RESET)
        finally:
            self.disconnect()
    
    def selectContatoDB(self,id):
        try:
            self.connect()
            querry = '''SELECT * FROM Contatos WHERE id=?;'''
            self.cursor.execute(querry,(id,))
            contato = self.cursor.fetchall()
            return contato[0]
        except sqlite3.Error as e:
            print(Fore.RED,'Erro ao selecionar contato: ',e,Fore.RESET)
        finally:
            self.disconnect()
    
    def existeContatoDB(self, email, telefone):
        try:
            self.connect()
            querry = '''SELECT * FROM Contatos WHERE email=? OR telefone=?;'''
            self.cursor.execute(querry, (email, telefone))
            contatos = self.cursor.fetchall()
            existe = False
            if len(contatos)>0:
                existe = True
            return existe
        except sqlite3.Error as e:
            print(Fore.RED,'\nNão existe contatos: ',e,Fore.RESET)
        finally:
            self.disconnect()

# if __name__ == '__main__':
#     db = AgendaDB()
#     if db.existeContatoDB('g@email.com','999999999'):
#         print('tem')
#     else:
#         print('n tem')