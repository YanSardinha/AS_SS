### Teste de SQL Injection

Para garantir a segurança contra ataques de SQL Injection, realizamos testes automatizados utilizando o script `test_security`. Estes testes visam identificar falhas de segurança ao processar entradas maliciosas.

#### Métodos de Teste Detalhados:

1. **Teste Automatizado com Strings Maliciosas**:
   - Utilizamos o método `testar_sql_injection` para inserir automaticamente strings típicas de SQL Injection, como `' OR '1'='1'`, `' OR '1'='1' --`, `%a%`.
   - O sistema é verificado quanto a acessos não autorizados ou comportamentos anormais que possam indicar vulnerabilidades.
   - Os resultados demonstram resistência a ataques de SQL Injection, devido ao uso de consultas parametrizadas.

2. **Avaliação da Segurança Contra SQL Injection**:
   - O uso de consultas parametrizadas (`cursor.execute('SELECT * FROM usuarios WHERE username = ?', (username,))`) previne a execução de entradas maliciosas como comandos SQL.

---

### Teste de Força Bruta em Autenticação

Utilizamos o método `testar_forca_bruta` no script `test_security` para avaliar a resistência do sistema a ataques de força bruta.

#### Métodos de Teste de Força Bruta:

1. **Teste Automatizado de Tentativas de Login**:
   - Realizamos tentativas automáticas de login usando uma gama de senhas para um usuário de teste.
   - Medimos o tempo necessário para quebrar a senha, avaliando a eficácia das medidas de segurança contra força bruta.

2. **Resultados e Avaliação**:
   - O sistema demonstra uma resistência adequada contra tentativas de força bruta (30 segundos para uma senha de 8 caracteres).

---

### Teste de Resistência de Hashes de Senha contra Rainbow Tables

Para avaliar a segurança dos hashes de senha, o script `test_hashs` foi utilizado para realizar testes de resistência contra ataques de Rainbow Tables.

#### Planejamento e Execução:

1. **Implementação de Salt Aleatório**:
   - Implementamos um sistema de geração de salt aleatório, concatenando este salt com as senhas antes da aplicação do hash.
   - Inserimos múltiplos usuários com a mesma senha para avaliar a eficácia do salting.

2. **Verificação de Hashes Únicos para Senhas Iguais**:
   - Verificamos se usuários com senhas idênticas possuem hashes diferentes.
   - Concluímos que a geração de salt aleatório garante hashes únicos, mesmo para senhas iguais.

3. **Resistência Contra Rainbow Tables**:
   - Através da verificação, constatamos que o sistema é resistente a ataques de decodificação de senha usando Rainbow Tables, graças ao uso de salting.
