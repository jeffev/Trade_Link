# Trade_Link

## Visão Geral

Este projeto tem como objetivo criar uma plataforma para traders registrarem suas operações financeiras (trades) e fornecer um dashboard para análise do desempenho. A plataforma permitirá que os traders cadastrem informações detalhadas sobre cada trade, como ativos negociados, datas, preços de entrada/saída e outros dados relevantes.

O dashboard integrado oferecerá recursos visuais para ajudar os traders a avaliarem seu desempenho ao longo do tempo, identificando padrões, tendências e áreas de melhoria.

## Estrutura do Projeto

### Backend

O backend está localizado no diretório `/backend` e é responsável pela lógica de negócios, gerenciamento de dados, e comunicação entre o frontend e qualquer banco de dados utilizado.

- `/pages`: Contém módulos Python para diferentes páginas da aplicação, como registro de trades e dashboard.
- `/callbacks`: Módulos Python para as callbacks utilizadas para atualizar dinamicamente o conteúdo com base nas interações do usuário.
- `/entities`: Módulos Python para representar as entidades principais do sistema, como os próprios trades.

### Frontend

O frontend está dividido nos diretórios `/frontend/assets` e `/frontend/templates`.

- `/assets`: Contém arquivos estáticos, como CSS, imagens e JavaScript.
- `/templates`: Armazena os arquivos HTML correspondentes a cada página da aplicação.

## Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.

2. Instale as dependências necessárias executando o seguinte comando no terminal:

    ```bash
    pip install -r requirements.txt
    ```

3. Navegue até o diretório `/backend` e execute o arquivo `server.py` para iniciar o servidor:

    ```bash
    cd backend
    python server.py
    ```

4. Abra um navegador e acesse `http://127.0.0.1:8050/` para acessar a aplicação.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou enviar pull requests para este projeto.
