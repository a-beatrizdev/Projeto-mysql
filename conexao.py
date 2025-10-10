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
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="faculdade"
        )
        cursor = conexao.cursor() 
        print("Conexão estabelecida")
        return conexao, cursor 
    except Exception as erro:
        print(f"Erro de conexão: {erro}") 
        return None, None
    
