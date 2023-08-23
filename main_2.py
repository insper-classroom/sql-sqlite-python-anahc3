import sqlite3
from db.db_utils import *

create_table('db/database_alunos.db', 'Estudantes', ['Nome', 'Curso', 'AnodeIngresso'])
consult('db/database_alunos.db', 'Estudantes')