import psycopg2
from psycopg2 import Error
import logging

logging.basicConfig(
    filename='model.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

class DataBase:
        conexao = None

        @staticmethod
        def conectar():
                if DataBase.conexao == None:
                        try:
                            DataBase.conexao = psycopg2.connect(
                                   user = 'postgres',
                                   password = 'marcos28',
                                   host = 'localhost',
                                   dbname = 'jplog'

                            )
                            logging.info('SUCESSO: Conexão realizada com sucesso.')
                        except Error as e:
                                DataBase.conexao = None
                                logging.error(f'ERRO: {e}.')
                return DataBase.conexao