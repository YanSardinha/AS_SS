import sqlite3
import bcrypt

def conectar_bd():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    conn.commit()

    return conn, cursor

def cadastrar_usuario(conn, cursor):
    username = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

    cursor.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, senha_hash))
    conn.commit()
    print("Usuário cadastrado com sucesso!")

def autenticar_usuario(conn, cursor):
    username = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    cursor.execute('SELECT * FROM usuarios WHERE username = ?', (username,))
    usuario = cursor.fetchone()

    if usuario and bcrypt.checkpw(senha.encode(), usuario[2]):
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

