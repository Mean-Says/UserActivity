
# GitHub User Activity Tracker

Este projeto é um rastreador de atividades de usuários do GitHub inspirado no presente em https://roadmap.sh/projects/github-user-activity , permitindo que você consulte as interações recentes de um usuário específico na plataforma. O projeto foi desenvolvido em Python e utiliza a API do GitHub para coletar dados sobre eventos de usuário.

## Funcionalidades

- Rastreia e exibe o número de eventos que um usuário realizou, como:
  - Criação de repositórios
  - Forks de repositórios
  - Estrela em repositórios
  - Comentários em problemas e pull requests
  - E outros eventos de atividade

## Como Usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu_usuario/github-user-activity-tracker.git
   cd github-user-activity-tracker
   ```

2. **Instale as dependências:**

   Certifique-se de que você tenha o Python e o `requests` instalados. Você pode instalar as dependências necessárias com:

   ```bash
   pip install requests
   ```

3. **Execute o programa:**

   Execute o programa na linha de comando:

   ```bash
   python seu_script.py
   ```

   Substitua `seu_script.py` pelo nome do arquivo que contém seu código.

4. **Interaja com o CLI:**

   No prompt do CLI, digite o nome de usuário do GitHub que você deseja rastrear:

   ```
   github-activity -> Mean-says
   ```

   O programa irá buscar os eventos do usuário e exibir os resultados.

## Exemplo de Uso

Após inserir um nome de usuário, você verá uma saída como:

```
- 3 times created a repo in repo_name.
- 2 times pushed to a repo in repo_name.
- 1 times started watching a repo.
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```


