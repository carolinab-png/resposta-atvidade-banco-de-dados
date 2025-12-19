1. Resposta: c. A chave primária deve identificar unicamente cada linha de uma tabela.

2. Resposta: b. A análise de requisitos permite compreender o que o banco precisa representar e as regras de negócio.

3. Resposta: d. O SGBD NÃO é responsável por decidir sozinho o modelo conceitual do banco.

4. Resposta: b. O sistema apresentaria erro, pois a chave primária deve ser única.

5. Entidades e Atributos (Cenário Empresa):

    Funcionário: ID_Funcionario (PK), Nome, CPF.

    Departamento: ID_Depto (PK), Nome_Depto.

    Projeto: ID_Projeto (PK), Nome_Projeto.

6. Chaves Primárias:

    Tabela Cliente: id_cliente é a PK.

    Tabela Pedido: id_pedido é a PK.

    Explicação: São PKs porque identificam registros exclusivos. O id_cliente na tabela Pedido cria uma relação entre as duas (Chave Estrangeira).

7. Sistema de Reservas de Hotel

    Requisitos Funcionais (O que faz): 1. Realizar reserva; 2. Cancelar reserva; 3. Consultar disponibilidade de quartos; 4. Cadastrar hóspedes; 5. Emitir nota fiscal; 6. Gerenciar check-in; 7. Gerenciar check-out; 8. Listar histórico de hospedagem.

    Requisitos Não Funcionais (Como se comporta): 1. O sistema deve ser acessível via web; 2. O tempo de resposta deve ser inferior a 2 segundos; 3. Backups diários automáticos; 4. Criptografia de dados sensíveis; 5. Interface responsiva para mobile.

8. Resposta: a. Nenhum produto poderá ter o mesmo código.

9. Resposta: b. O modelo conceitual descreve a realidade do negócio; o lógico traduz isso para tabelas.

10. Resposta: c. Modelagem conceitual.

11. Resposta: c. Garante maior integridade, segurança e consistência das informações.

12. Entidade: Cliente

    Atributos Sugeridos: id_cliente (Chave Primária), nome, cpf, telefone, endereço.

Entidade: Produto

    Atributos Sugeridos: codigo_produto (Chave Primária), nome, preço, quantidade_estoque.

Entidade: Venda

    Atributos Sugeridos: id_venda (Chave Primária), data_venda, id_cliente (Chave Estrangeira para identificar quem comprou)

13. Representação Relacional (Saúde)

    PACIENTE (id_paciente, nome, telefone)

    MEDICO (id_medico, nome, especialidade)

    CONSULTA (id_consulta, data, id_paciente, id_medico)

14. **Cenário:** Sistema de Rede Social

* **Requisitos Funcionais:**
    1. Permite postagens.
    2. Permite seguir usuários.
* **Requisitos Não Funcionas:**
    1. Criptografia de dados.
    2. Alta disponibilidade.
* **Modelo de Dados:**
    * **Entidade:** Usuário (id, nome, email).

15. a) Por que uma boa modelagem de dados facilita a implementação e manutenção?

   Uma boa modelagem funciona como a planta de uma casa. Se você planeja bem onde cada informação deve ficar antes de começar a construir (codificar), evita erros de lógica que exigiriam refazer todo o trabalho depois. Isso torna o sistema mais organizado, fácil de entender por outros programadores e permite que novas funcionalidades sejam adicionadas sem "quebrar" o que já existe.

b) Como um SGBD ajuda a evitar erros humanos e problemas de redundância?

     O SGBD (Sistema de Gerenciamento de Banco de Dados) atua como um fiscal rigoroso. Ele evita erros humanos através de regras de integridade (como impedir que um campo de data receba um texto) e garante que chaves primárias nunca sejam repetidas. Quanto à redundância, ele ajuda a organizar os dados para que a mesma informação não precise ser escrita em vários lugares diferentes; em vez de repetir os dados do cliente em cada venda, o SGBD usa apenas o ID do cliente para conectar as tabelas.

16. Resposta: a. A chave primária é uma combinação única de valores que identifica cada registro de uma tabela.

17. Resposta: b. "Produto" é uma entidade e os demais (código, nome, preço, etc.) são atributos.

18. Resposta: b. Levantar e entender o que o sistema deve armazenar e como deve funcionar.

19. Situação-Problema (Loja de Roupas)

    Entidades: Cliente, Produto e Venda.

    Atributos:

        Cliente: codigo_cliente (PK), nome, telefone, endereço.

        Produto: codigo_produto (PK), nome, preço.

        Venda: numero_venda (PK), data_venda, codigo_cliente (FK).

    Representação Relacional:

        CLIENTE (<u>codigo_cliente</u>, nome, telefone, endereço)

        PRODUTO (<u>codigo_produto</u>, nome, preço)

        VENDA (<u>numero_venda</u>, data_venda, codigo_cliente)