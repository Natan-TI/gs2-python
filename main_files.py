from funcoes_files import *

nome = input("Digite seu nome: ")
print(f"Seja bem vindo ao MedMaps, {nome}!!!")

c_ou_f = forca_opcao("Você é cliente ou funcionário? (c/f) ", ['c', 'f'])

if c_ou_f == 'c':
    hospitais = load_data_from_json('dados.json')

    for i in range(len(convenios)):
        print(f"{i} - {convenios[i]}")
    convenio = int(forca_opcao("Qual é o seu convênio? ", [str(i) for i in range(3)]))

    print("Hospitais disponíveis para o seu convênio:")
    for i in range(len(hospitais['nome'])):
        if hospitais['convenio'][i] == convenio:
            print("------")
            print(f"Nome: {hospitais['nome'][i]}")
            print(f"Tempo de espera: {hospitais['tempo de espera'][i]} minutos")
            print(f"Lotação: Nível {hospitais['lotacao'][i]} de lotação")
            print(f"Distância: {hospitais['distancia'][i]} km")
    print("------")
    indice = recomendacao(convenio, 'dados.json')
    print(f"De acordo com análises relacionando o tempo de espera e a distância, o MedMaps recomenda que você vá até o {hospitais['nome'][indice]}!")
else:
    hospitais = load_data_from_json('dados.json')
    # email = dev
    # senha = 123
    if fazer_login("usuario.json"):
        while True:
            print("------------------------------")
            print("O que você deseja fazer? ")
            opcao = int(forca_opcao("0 - Ver hospitais\n"
                                    "1 - Adicionar hospital\n"
                                    "2 - Editar hospital\n"
                                    "3 - Deletar hospital\n"
                                    "4 - Sair\n", [str(i) for i in range(5)]))
            print("------------------------------")
            if opcao == 0:
                ver_hospitais('dados.json')
            elif opcao == 1:
                add_hosp('dados.json')
            elif opcao == 2:
                edit_info('dados.json')
            elif opcao == 3:
                delete_hosp('dados.json')
            else:
                print(f"Até mais, {nome}!")
                break
    else:
        print("Programa encerrado.")
