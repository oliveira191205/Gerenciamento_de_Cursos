#Dados 
cursos = []
professores = []
alunos = []
acoes = []

turmas = {
    "ANÁLISE E DESENVOLVIMENTO DE SISTEMAS": {
        "professores_na_turma": [],
        "alunos_na_turma": []
    }
}

#Cadastro 
def cadastrar_curso():
    nome = input("Nome do curso: ").upper()
    carga = input("Carga horária (em horas): ")
    cursos.append((nome, carga))
    acoes.append(f"Curso cadastrado: {nome}")
    print("Curso cadastrado com sucesso!")

def cadastrar_professor():
    nome = input("Nome do professor: ")
    curso = input("Curso que o professor dá aula: ").upper()
    professores.append((nome, curso))
    acoes.append(f"Professor cadastrado: {nome}")
    print("Professor cadastrado com sucesso!")

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    idade = input("Idade: ")
    curso = input("Curso: ").upper()
    alunos.append((nome, idade, curso))
    acoes.append(f"Aluno cadastrado: {nome}")
    print("Aluno cadastrado com sucesso!") 

#Visualização
def mostrar_acoes():
    print("\nÚltimas ações realizadas:")
    if not acoes:
        print("Nenhuma ação registrada.")
    else:
        for acao in reversed(acoes[-5:]):
            print("- " + acao)


#Gerenciamento de turmas
def criar_turmas():
    for nome, carga in cursos:
        if nome not in turmas:
            turmas[nome] = {
                "professores_na_turma": [],
                "alunos_na_turma": []
            }

    for nome, idade, curso in alunos:
        if curso in turmas:
            if (nome, idade) not in turmas[curso]["alunos_na_turma"]:
                turmas[curso]["alunos_na_turma"].append((nome, idade))

    for nome, curso in professores:
        if curso in turmas:
            if nome not in turmas[curso]["professores_na_turma"]:
                turmas[curso]["professores_na_turma"].append(nome)

def mostrar_turmas():
    criar_turmas()
    for nome, dados in turmas.items():
        print(f"\nTurma: {nome}")
        if dados["alunos_na_turma"]:
            print("Alunos:")
            for aluno in dados["alunos_na_turma"]:
                print(f"- {aluno[0]}")
        else:
            print("Turma sem alunos")
        if dados["professores_na_turma"]:
            print("Professores:")
            for professor in dados["professores_na_turma"]:
                print(f"- {professor}")
        else:
            print("Turma sem professor")


#Operações
def mudar_de_curso():
    nome_aluno = input("Nome do aluno: ")
    novo_curso = input("Novo curso: ").upper()

    for i, (nome, idade, curso_atual) in enumerate(alunos):
        if nome == nome_aluno:
            alunos[i] = (nome, idade, novo_curso)

            if curso_atual in turmas:
                turmas[curso_atual]["alunos_na_turma"] = [
                    (n, idd) for n, idd in turmas[curso_atual]["alunos_na_turma"] if n != nome
                ]

            if novo_curso not in turmas:
                turmas[novo_curso] = {
                    "professores_na_turma": [],
                    "alunos_na_turma": []
                }

            turmas[novo_curso]["alunos_na_turma"].append((nome, idade))

            acoes.append(f"Aluno {nome} mudou de curso: {curso_atual} -> {novo_curso}")
            print(f"{nome} foi transferido para o curso {novo_curso}.")
            return

    print("Aluno não encontrado.")

def cancelar_matricula():
    nome_aluno = input("Nome do aluno a ser desmatriculado: ")

    for i, (nome, idade, curso) in enumerate(alunos):
        if nome == nome_aluno:
            alunos.pop(i)

            if curso in turmas:
                turmas[curso]["alunos_na_turma"] = [
                    (n, idd) for n, idd in turmas[curso]["alunos_na_turma"] if n != nome
                ]

            acoes.append(f"Aluno desmatriculado: {nome}")
            print(f"Aluno {nome} foi desmatriculado com sucesso.")
            return

    print("Aluno não encontrado.")

#Menu 
def menu():
    while True:
        print("\n--- MENU DE CADASTRO ---")
        print("1. Cadastrar Curso")
        print("2. Cadastrar Professor")
        print("3. Cadastrar Aluno")
        print("4. Listar todos")
        print("5. Mudar de Curso")
        print("6. Cancelar Matrícula")
        print("7. Ver Turmas")
        print("8. Ver últimas ações")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_curso()
        elif opcao == "2":
            cadastrar_professor()
        elif opcao == "3":
            cadastrar_aluno()
        elif opcao == "4":
            print("\nCursos:", cursos)
            print("Professores:", professores)
            print("Alunos:", alunos)
        elif opcao == "5":
            mudar_de_curso()
        elif opcao == "6":
            cancelar_matricula()
        elif opcao == "7":
            mostrar_turmas()
        elif opcao == "8":
            mostrar_acoes()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()