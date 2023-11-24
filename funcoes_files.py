import json

convenios = ['NotreDame Intermédica', 'Hapvida Assitência Médica', 'Bradesco Saúde']

def fazer_login(file_name):
    tentativas = 0

    with open(file_name, "r") as file:
        dados_usuario = json.load(file)

    email_correto = dados_usuario.get("email")
    senha_correta = dados_usuario.get("senha")

    while tentativas < 3:
        email = input("Digite o email: ")
        senha = input("Digite a senha: ")

        if email == email_correto and senha == senha_correta:
            print("Login bem-sucedido!")
            return True

        else:
            tentativas += 1
            if tentativas < 3:
                print(f"Credenciais incorretas! Você tem mais {3 - tentativas} tentativas.")

    print("Você excedeu o número de tentativas permitidas.")
    return False


def load_data_from_json(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def save_data_to_json(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    return


def forca_opcao(msg, lista):
    x = input(msg)
    if x not in lista:
        print("Tente novamente!")
        return forca_opcao(msg, lista)
    return x


def load_data_from_json(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {'nome': [], 'convenio': [], 'tempo de espera': [], 'lotacao': [], 'distancia': []}
    return data


def acha_menor(lista):
    menor = lista[0]
    indice = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice = i
    return indice


def recomendacao(convenio, file_name):
    data = load_data_from_json(file_name)

    lista_tempo = []
    lista_distancia = []
    lista_final = []
    lista_indices = []

    for i in range(len(data['nome'])):
        if data['convenio'][i] == convenio:
            lista_tempo.append(data['tempo de espera'][i])
            lista_distancia.append((data['distancia'][i]) * 5)
            lista_indices.append(i)

    for i in range(len(lista_tempo)):
        lista_final.append(lista_tempo[i] + lista_distancia[i])

    indice_final = acha_menor(lista_final)
    return lista_indices[indice_final]


def ver_hospitais(file_name):
    data = load_data_from_json(file_name)

    for i in range(len(data['nome'])):
        print(f"{i} : {data['nome'][i]}")
    return


def add_hosp(file_name):
    data = load_data_from_json(file_name)

    print("Digite as informações do novo hospital que você deseja cadastrar: ")
    new_hospital = {}
    for key in data.keys():
        if isinstance(data[key][0], int):
            while True:
                try:
                    if key == 'convenio':
                        for i in range(len(convenios)):
                            print(f"{i} - {convenios[i]}")
                        info = int(forca_opcao(f"Digite o/a {key} (0, 1, 2): ", ['0', '1', '2']))
                    elif key == 'tempo de espera':
                        valor = int(input(f"Digite o/a {key}: "))
                        info = valor
                    elif key == 'lotacao':
                        info = valor // 10
                    else:
                        info = int(input(f"Digite o/a {key}: "))
                    break
                except ValueError:
                    print("Erro: Por favor, insira um número.")
        else:
            info = input(f"Digite o/a {key}: ")
        new_hospital[key] = info

    for key, value in new_hospital.items():
        data[key].append(value)

    save_data_to_json(data, file_name)
    print("Dados adicionados com sucesso!")
    for key in new_hospital.keys():
        print(f"{key} : {new_hospital[key]}")
    return


def edit_info(file_name):
    data = load_data_from_json(file_name)

    for i in range(len(data['nome'])):
        print(f"{i} : {data['nome'][i]}")

    qual = int(
        forca_opcao("Qual hospital você deseja editar as informações? ", [str(i) for i in range(len(data['nome']))]))

    for key in data.keys():
        if isinstance(data[key][0], int):
            while True:
                try:
                    if key == 'convenio':
                        for i in range(len(convenios)):
                            print(f"{i} - {convenios[i]}")
                        info = int(forca_opcao(f"Digite o novo/a {key}:  (0, 1, 2): ", ['0', '1', '2']))
                    elif key == 'lotacao':
                        info = data['tempo de espera'][qual] // 10
                    else:
                        info = int(input(f"Digite o novo/a {key}: "))
                    break
                except ValueError:
                    print("Erro: Por favor, insira um número.")
        else:
            info = input(f"Digite o novo/a {key}: ")

        data[key][qual] = info

    save_data_to_json(data, file_name)
    print("Dados alterados com sucesso: ")

    for key in data.keys():
        print(f"{key} : {data[key][qual]}")
    return


def delete_hosp(file_name):
    data = load_data_from_json(file_name)

    for i in range(len(data['nome'])):
        print(f"{i} : {data['nome'][i]}")

    qual = int(forca_opcao("Qual hospital você deseja apagar? ", [str(i) for i in range(len(data['nome']))]))
    confirmacao = forca_opcao(f"Você tem certeza que deseja apagar o {data['nome'][qual]}? (s/n) ", ['s', 'n'])

    if confirmacao == 's':
        print("Dados apagados com sucesso: ")
        for key in data.keys():
            print(f"{key} : {data[key][qual]}")
            data[key].pop(qual)
    else:
        print("Operação cancelada!")

    save_data_to_json(data, file_name)
    return



