from utils import conectar_bd, cadastrar_usuario, autenticar_usuario, constants


def main():
    conn, cursor = conectar_bd()

    while True:
        print(constants['MSG_INICIAL'])

        escolha = input(constants['PERGUNTA_OPCAO'])

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
