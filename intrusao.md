#### Teste de SQL Injection Aprofundado

Para assegurar a robustez do sistema contra ataques de SQL Injection, conduzimos uma série de testes manuais. Estes testes visam identificar potenciais falhas de segurança ao processar entradas maliciosas no script CLI.

##### Métodos de Teste Detalhados:

1. **Inserção Direta de Strings de SQL Injection**:
   - Executamos `main.py` e selecionamos a opção de cadastro ou autenticação de usuário.
   - Inserimos strings maliciosas típicas de SQL Injection, como `' OR '1'='1`, `' OR '1'='1' --`, `%a%`, em campos de nome de usuário ou senha.
   - Observamos e registramos o comportamento do sistema, buscando acesso não autorizado ou comportamentos inesperados que indiquem possíveis vulnerabilidades.

2. **Teste com Entradas Maliciosas Específicas**:
   - Além das entradas comuns de SQL Injection, testamos strings que exploram particularidades do SQLite, como `' UNION SELECT * FROM usuarios --`.
   - Avaliamos como essas entradas afetam o sistema, procurando por sinais de execução de comandos SQL não intencionais.

3. **Resultados**:
    - O sistema demonstrou resistência a ataques de SQL Injection, graças à implementação de consultas parametrizadas (`cursor.execute('SELECT * FROM usuarios WHERE username = ?', (username,))`), que ajudam a prevenir a interpretação de entradas maliciosas como comandos SQL.

---

    #### Teste de Resistência de Hashes de Senha contra Rainbow Tables

Para avaliar a segurança dos hashes de senha armazenados no banco de dados, propomos a implementação de testes usando Rainbow Tables. Este teste verificará a resistência dos hashes gerados pelo sistema contra ataques de decodificação por Rainbow Tables.

##### Planejamento do Teste com Rainbow Tables:

1. **Criação de uma Rainbow Table para Teste**:
   - Desenvolveremos uma Rainbow Table contendo hashes comuns e seus correspondentes valores de texto claro.
   - Esta tabela será usada para tentar encontrar correspondências com os hashes armazenados no banco de dados.

2. **Teste de Correspondência de Hash**:
   - Compararemos os hashes de senha armazenados no banco de dados com os hashes na Rainbow Table.
   - Um hash que corresponda a um valor na Rainbow Table pode indicar uma vulnerabilidade.

3. **Avaliação**:
   - Percebemos que mesmo dois usuários com a mesma senha terão hashes diferentes, devido ao uso de um salt aleatório.

---

#### Teste de Resistência de Hashes de Senha contra Rainbow Tables

Para avaliar a segurança dos hashes de senha armazenados no banco de dados, realizamos testes usando Rainbow Tables. Este teste visa verificar a resistência dos hashes gerados pelo sistema contra ataques de decodificação por Rainbow Tables.

##### Planejamento do Teste com Rainbow Tables:

1. **Criação de uma Rainbow Table para Teste**:
   - Desenvolvemos uma Rainbow Table contendo hashes comuns e seus correspondentes valores de texto claro.
   - Esta tabela foi usada para tentar encontrar correspondências com os hashes armazenados no banco de dados.

2. **Teste de Correspondência de Hash**:
   - Comparamos os hashes de senha armazenados no banco de dados com os hashes na Rainbow Table.
   - Um hash que corresponda a um valor na Rainbow Table indicaria uma vulnerabilidade.

3. **Implementação de Salt Aleatório e Resultados**:
   - Implementamos um sistema de geração de salt aleatório e concatenação deste salt com as senhas antes da aplicação do hash.
   - Observamos que mesmo dois usuários com a mesma senha geram hashes diferentes, validando a eficácia do salting.
   - Concluímos que o sistema é resistente contra ataques de decodificação de senha usando Rainbow Tables devido ao uso de salting.

---
