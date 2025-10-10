import mysql.connector
from dotenv import load_dotenv
import os
# pip install dotenv
# pip install mysql-connector-python 

#Carregar as variáveis de ambiente (.env)
load_dotenv()

def conectar():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cursor = conexao.cursor() 
        print("Conexão estabelecida")
        return conexao, cursor 
    except Exception as erro:
        print(f"Erro de conexão: {erro}") 
        return None, None

    

