import sqlite3
conexao = sqlite3.connect('escola')
cursor = conexao.cursor()

conexao.commit()
conexao.close