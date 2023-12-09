import bcrypt
from utils import conectar_bd, gerar_salt_aleatorio


def usuario_existe(cursor, username):
    cursor.execute('SELECT COUNT(*) FROM usuarios WHERE username = ?', (username,))
    return cursor.fetchone()[0] > 0


def inserir_usuarios_com_mesma_senha(conn, cursor, senha, quantidade=5):
    for i in range(quantidade):
        username = f"usuario{i}"

        if not usuario_existe(cursor, username):
            salt = gerar_salt_aleatorio()
            senha_salt = senha + salt
            senha_hash = bcrypt.hashpw(senha_salt.encode(), bcrypt.gensalt())

            cursor.execute('INSERT INTO usuarios (username, password, salt) VALUES (?, ?, ?)', (username, senha_hash, salt))
            print(f"Usuário '{username}' cadastrado com sucesso.")
        else:
            print(f"Usuário '{username}' já existe. Pulando para o próximo...")

    conn.commit()


def recuperar_hashes_e_salts(cursor):
    cursor.execute('SELECT username, password, salt FROM usuarios')
    return cursor.fetchall()


def verificar_senhas_iguais_com_hashes_diferentes(hashes_salts, senha):
    for username, hash, salt in hashes_salts:
        senha_salt = senha + salt
        if bcrypt.checkpw(senha_salt.encode(), hash):
            print(f"Usuário {username} tem a senha {senha} com um hash único.")
        else:
            print(f"Usuário {username} não tem a senha {senha}.")


def main():
    conn, cursor = conectar_bd()

    senha_teste = "senha123"
    inserir_usuarios_com_mesma_senha(conn, cursor, senha_teste)

    hashes_salts = recuperar_hashes_e_salts(cursor)
    verificar_senhas_iguais_com_hashes_diferentes(hashes_salts, senha_teste)

    conn.close()


if __name__ == "__main__":
    main()
