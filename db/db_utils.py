import sqlite3

def create_table(caminho_db, nome_tabela, colunas):
    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()

    colunas_str = ", ".join(colunas)

    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {nome_tabela} (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        {colunas_str}
    );
    """)

    conn.commit()
    conn.close()

def insert(caminho_db, lista_tuplas, nome_tabela, colunas):
    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()

    cursor.executemany(f"""
    INSERT INTO {nome_tabela} ({', '.join(colunas)})
    VALUES (?, ?, ?, ?);
    """, {lista_tuplas})

    conn.commit()
    conn.close()

def consult(caminho_db, nome_tabela):
    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {nome_tabela}")

    conn.commit()

    print(cursor.fetchall())
    
    conn.close()

def delete(caminho_db, nome_tabela, condicao, elemento):
    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM {nome_tabela} WHERE {condicao} = ?", (f"{elemento}",))

    conn.commit()
    conn.close()

def update(caminho_db, nome_tabela, id_registro, novos_valores):
    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()

    colunas_valores = ", ".join([f"{coluna} = ?" for coluna in novos_valores.keys()])
    valores = tuple(novos_valores.values())

    query = f"""
    UPDATE {nome_tabela}
    SET {colunas_valores}
    WHERE ID = ?
    """

    cursor.execute(query, valores + (id_registro,))
    
    conn.commit()
    conn.close()