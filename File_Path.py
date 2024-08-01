import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
	dbname='nome_do_seu_banco_de_dados',
	user='estacio',
	password='estacio123',
	host='endereco_da_sua_instancia_rds.amazonaws.com',
	port='5432'
)

cur = conn.cursor()

file_path = '/caminho/para/seu/arquivo'

with open(file_path, 'rb') as f:
	binary_data = f.read()

insert_query = sql.SQL("INSERT INTO projeto_estacio_exemplo (arquivo) VALUES (%s)")
cur.execute(insert_query, (binary_data,))

conn.commit()
cur.close()
conn.close()

