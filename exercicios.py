import sqlite3
conexao = sqlite3.connect('sql')
cursor = conexao.cursor()

# QUESTÃO 1 - Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto)
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(50));')

# QUESTÃO 2 - Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Bárbara Gomes", 32, "Biologia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Natália Moreira", 23, "Educação Física")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Amanda Silva", 27, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Suzane Pereira", 33, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Viviane Jardim", 22, "Enfermagem")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "Caroline Fernandes", 25, "Letras")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(7, "Daniele Lima", 19, "Medicina")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(8, "Helena Rocha", 29, "Química")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(9, "Carla Mendonça", 56, "Psicologia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(10, "Maria Mello", 18, "Ciência da Computação")')

#QUESTÃO 3 - Consultas Básicas - Escreva consultas SQL para realizar as seguintes tarefas:

print("Questão 3a: Selecionar todos os registros da tabela alunos.")
tresa = cursor.execute('SELECT * FROM alunos')
for aluno in tresa:
    print(aluno)

print("Questão 3b: Selecionar o nome e a idade dos alunos com mais de 20 anos.")
tresb = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
for aluno in tresb:
    print(aluno)

print("Questão 3c: Selecionar os alunos do curso de Engenharia em ordem alfabética.")
tresc = cursor.execute('SELECT * FROM alunos WHERE curso IS "Engenharia" ORDER BY nome')
for aluno in tresc:
    print(aluno)

print("Questão 3d: Contar o número de alunos da tabela.")
tresd = cursor.execute('SELECT COUNT(*) FROM alunos')
for aluno in tresd:
    print(aluno)

#QUESTÃO 4 - Atualização e remoção

# Questão 4a: Atualize a idade de um aluno específico na tabela
cursor.execute('UPDATE alunos SET idade=66 WHERE nome="Carla Mendonça"')

# Questão 4a: Remova um aluno pelo seu ID
cursor.execute('DELETE FROM alunos WHERE id=7')

# QUESTÃO 5 - Criar uma Tabela e Inserir Dados - Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
cursor.execute('CREATE TABLE clientes(id INT NOT NULL PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Alexandra Cardoso", 45, 226.90)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "Priscila Brandão", 24, 1080.73)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Valquíria Prates", 33, 123.50)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "Livia Linhares", 48, 385.70)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, "Rosana Machado", 51, 850.32)')

# Questão 6: Consultas e Funções Agregadas - Escreva consultas SQL para realizar as seguintes tarefas:

# Questão 6a: Selecione o nome e a idade dos clientes com idade superior a 30 anos.
print("Questão 6a: Selecione o nome e a idade dos clientes com idade superior a 30 anos.")
seisa = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')
for cliente in seisa:
    print(cliente)

# Questão 6b: Calcule o saldo médio dos clientes.
print("Questão 6b: Calcule o saldo médio dos clientes.")
seisb = cursor.execute('SELECT AVG(saldo) AS saldo_media FROM clientes')
for cliente in seisb:
    print(cliente)

# Questão 6c: Encontre o cliente com o saldo máximo.
print("Questão 6c: Encontre o cliente com o saldo máximo.")
seisc = cursor.execute('SELECT MAX(saldo) AS saldo_maximo FROM clientes')
for cliente in seisc:
    print(cliente)

# Questão 6d: Conte quantos clientes têm saldo acima de 1000.
print("Questão 6d: Conte quantos clientes têm saldo acima de 1000.")
seisd = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo>1000')
for cliente in seisd:
    print(cliente)

# Questão 7: Atualização e Remoção com Condições

# Questão 7a: Atualize o saldo de um cliente específico
cursor.execute('UPDATE clientes SET saldo=1320.49 WHERE nome="Valquíria Prates"')

# Questão 7b: Remova um cliente pelo seu ID
cursor.execute('DELETE FROM clientes WHERE id=4')

# Questão 8: Junção de Tabelas - Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
cursor.execute('CREATE TABLE compras(id INT NOT NULL PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor REAL, CONSTRAINT fk_clicom FOREIGN KEY (cliente_id) REFERENCES clientes (id));')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(001, 2, "Natura Ilía Secreto Deo Parfum", 169.90)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(002, 5, "Lily Creme Acetinado Hidratante Desodorante Corporal 250g", 116.90)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(003, 1, "SIÀGE Combo Pro Cronology (4 itens)", 172.97)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(004, 2, "MAC HIDRATANTE LABIAL GLOW PLAY LIP BALM", 143.00)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(005, 3, "Espuma Cremosa de Limpeza Effaclar Reequilibrante La Roche-Posay 100g", 59.79)')

print("Questão 8: Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.")
oito = cursor.execute('SELECT nome, produto, valor from clientes FULL JOIN compras ON clientes.id =  compras.cliente_id WHERE nome = "Priscila Brandão"')
for compra in oito:
    print(compra)


conexao.commit()
conexao.close