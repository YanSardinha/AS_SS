# Projeto de Segurança de Sistemas - Testes de Segurança em um Banco local

Este projeto foi desenvolvido pelos alunos [Marco Antônio](https://github.com/Tchez) e [Yan Sardinha](https://github.com/YanSardinha) como parte da avaliação semestral da disciplina de Segurança de Sistemas na ULBRA Palmas, Universidade Luterana do Brasil.

## Descrição dos Arquivos

1. **.gitignore**: Arquivo que lista os arquivos e diretórios a serem ignorados pelo sistema de controle de versão Git.

2. **intrusao.md**: Contém informações detalhadas sobre os testes de intrusão que foram realizados durante o desenvolvimento do projeto. [Clique aqui para visualizar o intrusao.md](./intrusao.md).

3. **main.py**: Arquivo principal do projeto, responsável pela interação com o usuário para cadastro e login.

4. **requirements.txt**: Lista as bibliotecas utilizadas no projeto, juntamente com suas versões. Pode ser utilizado para instalar as dependências necessárias.

5. **test_hashs.py**: Automatiza os testes de verificação para garantir que a mesma senha gere hashes diferentes.

6. **test_security.py**: Automatiza testes de segurança, incluindo verificações de SQL injection e força bruta.

7. **utils.py**: Implementa funções relacionadas ao banco de dados.

## Executando o Projeto

Para executar o projeto, certifique-se de ter as dependências instaladas. Utilize o seguinte comando:

```bash
pip install -r requirements.txt
```

Em seguida, execute o arquivo main.py para interagir com o sistema.

Notas Adicionais

- Certifique-se de revisar o arquivo intrusao.md para obter detalhes sobre os testes de intrusão realizados.
  
- Este projeto foi desenvolvido como parte da avaliação semestral da disciplina de Segurança de Sistemas na ULBRA Palmas.
