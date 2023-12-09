import sqlite3
import bcrypt
from faker import Faker

faker = Faker()

constants = {
    'MSG_INICIAL': """\n
Escolha uma opção:
1. Cadastrar usuário
2. Autenticar usuário
3. Sair""",
    'PERGUNTA_OPCAO': "\nDigite o número da opção desejada: ",
    'PERGUNTA_USERNAME': "Digite o nome de usuário: ",
    'PERGUNTA_SENHA': "Digite a senha: ",
    'MSG_USUARIO_CADASTRADO': "Usuário cadastrado com sucesso!",
    'MSG_LOGADO': "\nLogin bem-sucedido!",
    'MSG_INFOS_INCORRETAS': "Usuário ou senha incorretos",
}


def gerar_salt_aleatorio():
    return faker.pystr(min_chars=16, max_chars=16)


def conectar_bd():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            salt TEXT
        )
    ''')

    conn.commit()

    return conn, cursor


def cadastrar_usuario(conn, cursor):
    username = input(constants['PERGUNTA_USERNAME'])
    senha = input(constants['PERGUNTA_SENHA'])

    salt = gerar_salt_aleatorio()
    senha_salt = senha + salt
    senha_hash = bcrypt.hashpw(senha_salt.encode(), bcrypt.gensalt())

    cursor.execute('INSERT INTO usuarios (username, password, salt) VALUES (?, ?, ?)', (username, senha_hash, salt))
    conn.commit()

    print(constants['MSG_USUARIO_CADASTRADO'])


def autenticar_usuario(conn, cursor):
    username = input(constants['PERGUNTA_USERNAME'])
    senha = input(constants['PERGUNTA_SENHA'])
    cursor.execute('SELECT * FROM usuarios WHERE username = ?', (username,))

    usuario = cursor.fetchone()

    if usuario:
        senha_salt = senha + usuario[3]
        if bcrypt.checkpw(senha_salt.encode(), usuario[2]):
            print(constants['MSG_LOGADO'])
        else:
            print(constants['MSG_INFOS_INCORRETAS'])
    else:
        print(constants['MSG_INFOS_INCORRETAS'])
