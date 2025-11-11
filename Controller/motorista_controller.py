from Model.database import DataBase,logging,Error
from Model.motorista import Motorista

class MotoristaController:

    @staticmethod
    def inserir(motorista: Motorista):
        conexao = DataBase.conectar()
        try:
            cursor = conexao.cursor()
            consulta = 'INSERT INTO motorista (nome,cpf,telefone,cnh) VALUES (%s,%s,%s,%s)'
            valores = (motorista.nome,motorista.cpf,motorista.telefone,motorista.cnh)
            cursor.execute(consulta,valores)
            conexao.commit()
            logging.info(f'SUCESSO: Motorista {motorista.nome} inserido.')
            return True
            
        except Error as e:
            logging.error(f'ERRO ao tentar inserir veiculo {motorista.nome}: {e}.' )
            return e
        
    def deletar(id_motorista):
        conexao = DataBase.conectar()
        try:
            cursor = conexao.cursor()
            consulta = 'DELETE FROM motorista WHERE id = (%s)'
            valores = (id_motorista,)
            cursor.execute(consulta,valores)
            conexao.commit()
            logging.info(f'SUCESSO: Motorista de id {id_motorista} deletado.')
            return True    

        except Error as e:
            logging.error(f'ERRO ao tentar deletar motorista de id {id_motorista}: {e}.' )
            return e
        
    def atualizar(motorista: Motorista, id_motorista):

        conexao = DataBase.conectar()
        campos = []
        valores = []

        if motorista.nome:
            campos.append('nome=%s')
            valores.append(motorista.nome)
        if motorista.cpf:
            campos.append('cpf=%s')
            valores.append(motorista.cpf)
        if motorista.telefone:
            campos.append('telefone=%s')
            valores.append(motorista.telefone)
        if motorista.cnh:
            campos.append('cnh=%s')
            valores.append(motorista.cnh)

        try:
            cursor = conexao.cursor()
            consulta = f'UPDATE motorista SET {" ,".join(campos)} WHERE id = %s'
            valores.append(id_motorista)
            cursor.execute(consulta,tuple(valores))
            conexao.commit()
            logging.info(f'SUCESSO: Motorista com id: {id_motorista} atualizado.' )
            return True                 
        
        except Error as e:
            logging.error(f'ERRO ao tentar atualizar motorista de id: {id_motorista}: {e}.' )
            return e        
            