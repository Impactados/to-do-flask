import utils

def execute_sql_file():
    # Conecte-se ao banco de dados
    file_path = 'app/database/db.sql'
    conn = utils.connect_database()

    if conn is None:
        print("Não foi possível conectar ao banco de dados.")
        return [False, "Erro de conexão com o banco de dados."]

    cursor = conn.cursor()

    # Leia o arquivo SQL
    with open(file_path, 'r') as file:
        sql_script = file.read()

    # Execute o script SQL
    try:
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        conn.commit()
        print("Script SQL executado com sucesso.")
    except Exception as e:
        conn.rollback()
        return [False, f"Erro ao executar o script SQL: {e}"]
    finally:
        cursor.close()
        conn.close()
    
    return [True, 'Banco de dados configurado com sucesso!']

