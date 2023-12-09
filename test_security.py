import sqlite3
import bcrypt
from utils import conectar_bd
import time


def testar_sql_injection(cursor):
    payloads = ["' OR '1'='1'", "' OR '1'='1' --", "%a%"]

    print("\nTeste de SQL Injection:")
    for payload in payloads:
        try:
            cursor.execute(f"SELECT * FROM usuarios WHERE username = ?", (payload,))
            resultado = cursor.fetchall()

            if resultado:
                print(f"Payload '{payload}' resultou em uma correspondência - possível SQL Injection.")
            else:
                print(f"Payload '{payload}' não resultou em correspondências - sem SQL Injection.")
        except sqlite3.Error as e:
            print(f"Falha no teste de SQL Injection para payload '{payload}': {e}")


def testar_forca_bruta(cursor):
    usuario_teste = 'usuario0'

    print("\nTeste de Força Bruta:")
    
    start_time = time.time()
    
    for tentativa in range(10000):
        senha_teste = f'senha{tentativa}'
        cursor.execute('SELECT * FROM usuarios WHERE username = ?', (usuario_teste,))
        usuario = cursor.fetchone()

        if usuario and bcrypt.checkpw((senha_teste + usuario[3]).encode(), usuario[2]):
            end_time = time.time()
            tempo_decorrido = end_time - start_time
            print(f"Força Bruta bem-sucedida! Usuário: {usuario_teste}, Senha: {senha_teste}")
            print(f"Tempo decorrido: {tempo_decorrido:.2f} segundos")
            break
    else:
        print("Força Bruta sem sucesso. Senha não encontrada.")


if __name__ == "__main__":
    conn, cursor = conectar_bd()

    testar_sql_injection(cursor)
    testar_forca_bruta(cursor)

    conn.close()
