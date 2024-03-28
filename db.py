import sqlite3
from colorama import Fore

#*----- cennection .db -----*#
class AgendaConn():
    def __init__(self,path):
        self.path = path
        self.connection = None
    
    def connect(self):
        try:
            #*---- set connection ----*#
            self.connection = sqlite3.connect(self.path)
            print(Fore.GREEN+'Conexão estabelacida com sucesso!'+Fore.RESET)
            # return self.connection
        except sqlite3.Error as e:
            print(Fore.RED,'Erro na conexão do banco: ',e,Fore.RESET)
    
    def discnnect(self):
        if self.connection:
            self.connection.close()
            print(Fore.GREEN+'Conexão encerrada com sucesso!'+Fore.RESET)
        else:
            print(Fore.RED+'Não há conexão estabelecida!'+Fore.RESET)

#*---- execute querry in .db ----*#
class AgendaQuerry():
    def __init__(self,db_connection):
        self.db_connection = db_connection
    
    #*---- create, delete and update ----*#
    def querryCUD(self, sqlQuerry):
        try:
            #*---- set cursor that go crete a pointer taht for each line in querry to add in .db ----*#
            cursor = self.db_connection.cursor()
            cursor.execute(sqlQuerry)
            self.db_connection.commit()
        except sqlite3.Error as e:
            print(Fore.RED,'Erro na requisição do banco: ',e,Fore.RESET)
        #*---- excute anyway ----*#
        finally:
            print(Fore.GREEN+'Querry executada com sucesso!'+Fore.RESET)
    
    def querrySearch(self, sqlQuerry):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(sqlQuerry)
            #*---- get all registers in .db ----*#
            result = cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(Fore.RED+"Erro na busca de dados do banco: ",e,Fore.RESET)

#*---- execute test main ----*#
# if __name__ == '__main__':
#     db = AgendaConn('agenda.db')
#     db.connect()
    
#     insertSQL = f'''INSERT INTO Contatos (nome, sobreNome, telefone, email)
#                     VALUES ('Gustavo', 'Cardoso', '(77)98650782', 'gustavo@email.com')'''
    
#     deleteSQL = f'''DELETE FROM Contatos WHERE id > 0'''

#     updateSQL = f'''UPDATE Contatos SET nome='Maria', email='maria@email.com' WHERE id=6'''

#     querry = AgendaQuerry(db.connection)
#     querry.querryCUD(updateSQL)

#     db.discnnect()