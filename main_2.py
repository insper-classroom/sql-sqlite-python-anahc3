import sqlite3
from db.db_utils import *

caminho_db = 'db/database_alunos.db'
nome_tabela = 'Estudantes'
colunas = ['Nome', 'Curso', 'AnodeIngresso']

create_table(caminho_db, nome_tabela, colunas)

estudantes = [
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022)
]

insert(caminho_db, nome_tabela, estudantes)

consult(caminho_db, nome_tabela)

delete(caminho_db, nome_tabela, 'Nome', 'Ana Silva')

consult(caminho_db, nome_tabela)

update(caminho_db, nome_tabela, 1, {'Nome': "Alicia", 'Curso': 'Computação', 'AnodeIngresso': 2019})

consult(caminho_db, nome_tabela)
