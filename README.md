# MedMaps - Sistema de Gerenciamento Hospitalar

## Links
* Youtube: https://youtu.be/jlZIxhjhJiQ

## Descrição do Problema

A superlotação hospitalar é um problema comum causado pela imprevisibilidade na demanda por serviços de saúde, levando a picos repentinos de pacientes que sobrecarregam os recursos disponíveis. Isso resulta em uma distribuição inadequada de leitos e congestionamento nas áreas de atendimento, impactando negativamente a qualidade e eficiência do cuidado médico.

## Solução Proposta

O MedMaps é um sistema inovador que oferece aos usuários a capacidade de verificar a lotação de hospitais em tempo real dentro de um raio específico. Utilizando tecnologias de geolocalização, o sistema fornece informações detalhadas sobre disponibilidade de leitos, ocupação e tempo de espera. Isso capacita os usuários a tomarem decisões informadas sobre cuidados de saúde emergenciais ou planejados, contribuindo para uma gestão mais eficiente dos serviços hospitalares.

## Estrutura do Projeto

O projeto é composto por dois arquivos principais:

* `main_files.py`: Responsável pela interação com o usuário, validação de login, e execução do programa com base nas funções definidas em `funcoes_files.py`.

* `funcoes.py`: Contém uma série de funções para manipulação de dados, autenticação de usuários, interação com arquivos JSON, e operações relacionadas à manipulação de informações de hospitais.

E dois arquivos auxiliares:

* `dados.json`: Armazena as informações sobre os hospitais, como nome, tempo de espera, lotação, distância e qual convênio pertence a cada hospital.

* `usuario.json`: Contém as credenciais necessárias para efetuar o login ao tentar entrar como funcionário, simulando um sistema de segurança no projeto.


## Organização das Funcionalidades

* <b>Autenticação de Usuário:</b>

    * A função `fazer_login(file_name)` valida as credenciais do usuário.

* <b>Manipulação de Dados:</b>

    * Funções como `load_data_from_json(file_name)` e `save_data_to_json(data, file_name)` são responsáveis por carregar e salvar dados em arquivos JSON, permitindo a persistência de informações.

* <b>Gerenciamento de Hospitais:</b>

    * Funcionalidades como `ver_hospitais(file_name)`, `add_hosp(file_name)`, `edit_info(file_name)`, e `delete_hosp(file_name)` lidam com a manipulação, adição, edição e exclusão de informações relacionadas aos hospitais.


## Funcionalidades

### `fazer_login(file_name)`
Realiza a autenticação do usuário para acesso ao sistema.

### `load_data_from_json(file_name)`
Carrega dados de um arquivo JSON.

### `save_data_to_json(data, file_name)`
Salva dados em um arquivo JSON.

### `forca_opcao(msg, lista)`
Valida a entrada do usuário com base em uma lista de opções.

### `acha_menor(lista)`
Encontra o menor elemento em uma lista.

### `recomendacao(convenio, file_name)`
Fornece recomendação de hospital com base no convênio do usuário.

### `ver_hospitais(file_name)`
Mostra informações sobre os hospitais disponíveis.

### `add_hosp(file_name)`
Adiciona informações de um novo hospital.

### `edit_info(file_name)`
Permite editar informações de um hospital existente.

### `delete_hosp(file_name)`
Remove informações de um hospital.

## Instruções de Uso

1. Clonar o repositório.
2. Criar o projeto no PyCharm.
3. Adicionar os arquivos no projeto do PyCharm.
4. Executar o programa.

## Requisitos

- Python 3.9.
- IDE Pycharm.

## Dependências

- Biblioteca JSON.

## Tecnologias Utilizadas

- Python.
- JSON.

## Colaboradores

- Natan Eguchi dos Santos - RM98720
- Kayky Paschoal Ribeiro - RM99929

## Status do Projeto

Em desenvolvimento :hourglass_flowing_sand:
