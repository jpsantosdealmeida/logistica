from Model.database import DataBase,logging,Error
from Model.veiculo import Veiculo

class VeiculoController:
    
    # Inserir um veiculo a tabela Veiculo
    @staticmethod
    def inserir(veiculo: Veiculo):
        conexao = DataBase.conectar()
        try:
            cursor = conexao.cursor()
            consulta = ('INSERT INTO veiculo (placa,modelo,ano,id_motorista) VALUES (%s,%s,%s,%s)')
            valores = (veiculo.placa,veiculo.modelo,veiculo.ano,veiculo.id_motorista)
            cursor.execute(consulta,valores)
            conexao.commit()
            logging.info(f'SUCESSO: Veiculo  {veiculo.placa} inserido.')
            return True
            
        except Error as e:
            logging.error(f'ERRO ao tentar inserir veiculo {veiculo.placa}: {e}.' )
            return e
        
    def deletar(id_veiculo):
        conexao = DataBase.conectar()
        try:
            cursor = conexao.cursor()
            consulta = 'DELETE FROM veiculo WHERE id =(%s)'
            valores = (id_veiculo,)
            cursor.execute(consulta,valores)
            conexao.commit()
            logging.info(f'SUCESSO: Veiculo de id {id_veiculo} deletado.')
            return True    

        except Error as e:
            logging.error(f'ERRO ao tentar deletar veiculo de id {id_veiculo}: {e}.' )
            return e      

    def atualizar(veiculo: Veiculo, id_veiculo):

        conexao = DataBase.conectar()
        campos = []
        valores = []

        if veiculo.placa:
            campos.append('placa=%s')
            valores.append(veiculo.placa)
        if veiculo.modelo:
            campos.append('modelo=%s')
            valores.append(veiculo.modelo)
        if veiculo.ano:
            campos.append('ano=%s')
            valores.append(veiculo.ano)
        if veiculo.id_motorista:
            campos.append('id_motorista=%s')
            valores.append(veiculo.id_motorista)

        try:
            cursor = conexao.cursor()
            consulta = f'UPDATE veiculo SET {" ,".join(campos)} WHERE id = %s'
            valores.append(id_veiculo)
            cursor.execute(consulta,tuple(valores))
            conexao.commit()
            logging.info(f'SUCESSO: Veiculo com id: {id_veiculo} atualizado.' )
            return True                 
        
        except Error as e:
            logging.error(f'ERRO ao tentar atualizar veiculo de id: {id_veiculo}: {e}.' )
            return e               

            