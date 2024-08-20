import sqlite3

conexao = sqlite3.connect("bancoF")
cursor = conexao.cursor()

cursor.execute(
    "CREATE TABLE Autores(autor_id INT, nome VARCHAR(100), nacionalidade VARCHAR(50));"
)

cursor.execute(
    """CREATE TABLE Editoras(editora_id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100) NOT NULL);"""
)

cursor.execute(
    "CREATE TABLE Livros (livro_id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, editora_id INTEGER,max_renovacoes INTEGER, FOREIGN KEY (editora_id) REFERENCES Editoras(editora_id));"
)

cursor.execute(
    "CREATE TABLE Exemplares (exemplar_id INTEGER PRIMARY KEY AUTOINCREMENT, livro_id INTEGER, codigo VACHAR(50), disponivel BOOLEAN DEFAULT 1, FOREIGN KEY (livro_id) REFERENCES Livros(livro_id));"
)

cursor.execute(
    "CREATE TABLE Usuarios (usuario_id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100) NOT NULL, telefone VACHAR(15), nacionalidade VARCHAR(50));"
)
cursor.execute(
    """
CREATE TABLE Emprestimos (
    emprestimo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    exemplar_id INTEGER,
    data_emprestimo DATE,
    data_devolucao DATE,
    estado TEXT,
    renovacoes INTEGER DEFAULT 0,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id),
    FOREIGN KEY (exemplar_id) REFERENCES Exemplares(exemplar_id)
);
"""
)

cursor.execute(
    """
CREATE TABLE Livro_Autores (
    livro_id INTEGER,
    autor_id INTEGER,
    PRIMARY KEY (livro_id, autor_id),
    FOREIGN KEY (livro_id) REFERENCES Livros(livro_id),
    FOREIGN KEY (autor_id) REFERENCES Autores(autor_id)
);
"""
)

conexao.commit()
conexao.close

# cursor.execute(
#     "INSERT INTO produtos(id, nome, endereco, email) VALUES (1, 'Dani', 'bromelia', 'dani@gmail.com');"
# )
# cursor.execute(
#     "INSERT INTO produtos(id, nome, endereco, email) VALUES (2, 'Frank', 'Por Ali', 'Frank@gmail.com');"
# )
# cursor.execute(
#     "INSERT INTO produtos(id, nome, endereco, email) VALUES (3, 'Valdemar', 'Ali Perto', 'Val@gmail.com');"
# )
# cursor.execute(
#     "INSERT INTO produtos(id, nome, endereco, email) VALUES (4, 'Fabio', 'flor', 'Fabio@gmail.com');"
# )
# cursor.execute(
#     "INSERT INTO produtos(id, nome, endereco, email) VALUES (5, 'Maria', 'rosas', 'Maria@gmail.com');"
# )
# cursor.execute("DELETE FROM usuario where id=1") deleta dados inseridos na tabela
# dado = cursor.execute("SELECT * FROM produtos")
# ORDER BY DESC
# dado = cursor.execute(
#     "SELECT * FROM produtos ORDER BY nome "
# )  # ordena na ordem alfabetica
# dado = cursor.execute("SELECT * FROM produtos ORDER BY nome DESC")   ordena descresente

# LIMIT E DISTINCT
# dado = cursor.execute("SELECT * FROM produtos LIMIT 3")

# GROUP BY E HAVING
# dado = cursor.execute("SELECT nome FROM produtos GROUP BY nome")
# dado = cursor.execute("SELECT nome FROM produtos GROUP BY nome HAVING id > 3")

# JOIN´s
# for produtos in dado:
#     print(produtos)
# cursor.execute('UPDATE usuario SET endereco="Minha Rua" WHERE nome="Valdemar"')

# para ocorre tudo certo conexão com banco de dado sqlite tem entra na pasta roda a python conexaoC.py
