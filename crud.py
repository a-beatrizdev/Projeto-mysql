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
            return []
        finally:
            cursor.close()
            conexao.close()


def atualizar_idade(id_aluno, nova_idade):
     conexao, cursor = conectar()
     if conexao:
        try:
             cursor.execute(
                "UPDATE alunos SET idade = %s WHERE id = %s",
                (nova_idade, id_aluno)
            )
             conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar o aluno: {erro}")
        finally:
            cursor.close()
            conexao.close()


def deletar_alunos(id_aluno):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM alunos WHERE id = %s", 
                (id_aluno,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar o aluno: {erro}")
        finally:
            cursor.close()
            conexao.close()








            


   








