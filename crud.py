from conexao import conectar


def inserir_aluno(nome_aluno, idade_aluno):
    conexao, cursor = conectar() 
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO alunos (nome, idade) VALUES (%s, %s)",
                (nome_aluno, idade_aluno)  
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao tentar inserir aluno: {erro}")
        finally:
            cursor.close()
            conexao.close()


def listar_alunos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM alunos ORDER BY id"            
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar os alunos: {erro}")
        finally:
            cursor.close()
            conexao.close()







