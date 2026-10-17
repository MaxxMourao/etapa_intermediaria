
def solicitar_titulo():

    while True:
        titulo = input("Digite o título da tarefa: ").strip()

        if titulo:
            return titulo

        print("Erro: o título não pode ficar vazio. Tente novamente.")


def solicitar_prioridade():

    while True:
        prioridade = input(
            "Digite a prioridade (Alta, Média ou Baixa): "
        ).strip().casefold()

        prioridades_validas = {
            "alta": "Alta",
            "média": "Média",
            "media": "Média",
            "baixa": "Baixa"
        }

        if prioridade in prioridades_validas:
            return prioridades_validas[prioridade]

        print(
            "Erro: prioridade inválida. "
            "Escolha Alta, Média ou Baixa."
        )


def cadastrar_tarefa(tarefas):

    print("\n--- CADASTRO DE TAREFA ---")

    titulo = solicitar_titulo()

    descricao = input("Digite a descrição: ").strip()

    prioridade = solicitar_prioridade()

    data_limite = input(
        "Digite a data limite (DD/MM/AAAA): "
    ).strip()


    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }


    tarefas.append(tarefa)

    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas(tarefas):

    print("\n--- LISTA DE TAREFAS ---")

    if not tarefas:
        print("Não existem tarefas cadastradas no momento.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {indice}")
        print(f"Título:      {tarefa['titulo']}")
        print(f"Descrição:   {tarefa['descricao']}")
        print(f"Prioridade:  {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status:      {tarefa['status']}")

        print("-" * 35)


def exibir_menu():

    print("\n========== TASKTRACKER ==========")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")

    return input("Escolha uma opção: ").strip()


def main():
    """Controla o funcionamento da aplicação."""
    tarefas = []

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            cadastrar_tarefa(tarefas)

        elif opcao == "2":
            visualizar_tarefas(tarefas)

        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break

        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")



if __name__ == "__main__":
    main()

