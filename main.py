from functions import conectar_bd, cadastrar_usuario, autenticar_usuario

def main():
    conn, cursor = conectar_bd()

    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar usuário")
        print("2. Autenticar usuário")
        print("3. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            cadastrar_usuario(conn, cursor)
        elif escolha == '2':
            autenticar_usuario(conn, cursor)
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    conn.close()

if __name__ == "__main__":
    main()
