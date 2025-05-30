# Sistema de Gerenciamento de Cursos 
O sistema de Gerenciamento de cursos é um programa de cadastro simples, desenvolvido com o foco em controlar os dados de **cursos**, **professores** e **alunos**. Além disso, o sistema conta com a funcionalidade extra que permite visualizar um **histórico das ultimas ações realizadas**, que simula o comportamento de uma pilha ( **LIFO**: ultimo a entrar, primeiro a sair), assim, oferecendo uma maior trasparência e rastreabililidade das operações realizadas.

## Objetivo
O objetivo deste sistema é proporcionar uma maneira simples e eficaz de cadastrar e gerenciar dados acadêmicos básicos, sendo especialmente útil para quem está aprendendo lógica de programação, manipulação de listas e tuplas, e estruturas de controle em Python.

## Menu
O sistema apresenta um menu de opções em um laço `while True`, que oferece ao usuário diferentes operações, que serão escolhidas por meio da digitação do numero referente a cada opção apresnetada no menu, este menu é exibido continuamente até que o usuário opte por encerrar as operações. As operações se tratam de:
1. Cadastrar Cursos
2. Cadastrar professores
3. Cadastrar cursos
4. Listar todos
5. Mudar de curso
6. Cancelar matrícula
7. Ver turmas
8. Mostrar ações
9. Sair do sistema

As escolhas do usuário são tratadas com estruturas `if`, `elif`, e `else`, que direcionam a execução para a função correspondente.
  
## Cadastro de Cursos

### Função: `cadastrar_curso()`

### Como funciona:
1. O sistema solicita dois dados:
- **Nome do curso**
- **Carga horária**
  
2. Esses dados são agrupados em uma **tupla** no formato `(nome_curso, carga_horaria)`.
   
3. A tupla é então adicionada à lista `cursos` utilizando o método `append()`.
   
4. Uma mensagem de registro da ação é adicionada à lista `acoes`.

### Estrutura escolhida:
- **Tupla:** Armazena os dados fixos do curso de forma compacta e imutável.
- **Lista (`cursos`):** Permite armazenar dinamicamente vários cursos, preservando a ordem de cadastro.
- **Lista (`acoes`):** Registra o histórico das operações realizadas no sistema.

## Cadastro de Professores

### Função: `cadastrar_professor()`

### Como funciona:
1. O sistema solicita:
    - **Nome do professor**
    - **Curso que ele leciona**
2. Os dados são agrupados em uma **tupla** `(nome_professor, curso)`.
3. Essa tupla é adicionada à lista `professores` com `append()`.
4. A ação é registrada na lista `acoes`.

### Estrutura escolhida:
- **Tupla:** Ideal para armazenar informações fixas sobre o professor.
- **Lista (`professores`):** Permite gerenciar os cadastros de forma sequencial.
- **Lista (`acoes`):** Garante rastreabilidade da operação.

## Cadastro de Alunos

### Função: `cadastrar_aluno()`

### Como funciona:

1. O sistema solicita:
    * **Nome do aluno**
    * **Idade**
2. Os dados são armazenados em uma **tupla** `(nome, idade)`.
3. Essa tupla é adicionada à lista `alunos` usando `append()`.
4. A ação é registrada na lista `acoes`.

### Estrutura escolhida:
- **Tupla:** Representa o aluno de forma clara e imutável.
- **Lista (`alunos`):** Permite adicionar diversos alunos dinamicamente.
- **Lista (`acoes`):** Ajuda a manter o histórico das interações.

## Histórico de Ações

### Função: `mostrar_acoes()`

A lista `acoes` funciona como uma **pilha de ações recentes**. A cada operação (cadastro, alteração, remoção), uma mensagem é adicionada com `append()` ao final da lista.

Para exibir o histórico, a função utiliza a função **`reversed()`** e mostra as **últimas 5 ações**, da mais recente para a mais antiga.

### Por que essa abordagem?

- **Lista (`acoes`):** Simples de implementar e eficaz para adicionar novas entradas.
- **`reversed()`:** Permite simular o comportamento de uma pilha (LIFO – Last In, First Out).

## Fluxo de Execução

Todo o sistema funciona dentro de um loop `while True`, garantindo que o menu continue sendo exibido até que o usuário decida sair.

### Exemplo de controle de fluxo:
```
while True:
    print("1 - Cadastrar curso")
    print("2 - Cadastrar professor")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_curso()
    elif opcao == "2":
        cadastrar_professor()
    elif opcao == "0":
        break
```

## Gerenciamento de Turmas

O gerenciamento das **turmas** foi implementado por meio de um **dicionário aninhado**, no qual:

- A **chave principal** é o nome do curso.
- O **valor** é outro dicionário que contém duas listas:
    - `alunos`: lista de alunos matriculados naquele curso
    - `professores`: lista de professores que lecionam naquele curso

### Como funciona:

- Sempre que um novo curso é cadastrado, uma nova chave é criada no dicionário `turmas`.
- Ao cadastrar um aluno ou professor, o sistema verifica o nome do curso e adiciona o item à lista correspondente dentro da chave do curso.
- Caso o curso ainda não exista no dicionário `turmas`, ele é criado automaticamente.

### Visualização:

- O sistema percorre cada curso no dicionário `turmas`.
- Se a lista de alunos estiver vazia, exibe: **"Turma sem alunos"**
- Se a lista de professores estiver vazia, exibe: **"Turma sem professor"**

### Estruturas escolhidas:

- **Dicionário (`turmas`):** Ideal para associar cursos a seus alunos e professores, foi utilizado visando agrupar as informações das turmas de uma forma mais organizada, uma vez que precisamos nomear tais elementos para sua identificação e a forma mais fácil de sua manipulação, com a inserção e alteração de listas por exemplo, contribuíram para a escolha desse elemento na estrutura do código
- **Lista:** Permitem a inserção e remoção dinâmica de elementos, facilitando a manutenção dos dados de cada turma.
- **Combinação de dicionário com listas:** Oferece uma organização eficiente e flexível.

## Mudar de Curso

A função **`mudar_de_curso`** tem como objetivo principal transferir um aluno de um curso (ou turma) para outro. Ela é especialmente útil em sistemas educacionais onde o aluno pode decidir trocar de área de estudo ou fazer correções administrativas.

### Etapas da função

1. **Solicitação de Dados**
    - O sistema solicita ao usuário:
        - **Nome do aluno**
        - **Novo curso** desejado
        
2. **Busca pelo Aluno**
    - A função utiliza o **`enumerate()`** para percorrer a lista chamada `alunos`, que contém **tuplas** com as informações: `(nome, idade, curso_atual)`.
    - A busca é feita comparando o nome digitado com o nome de cada aluno da lista.
  
3. **Atualização de Curso**
    - Se o aluno for encontrado:
        - O sistema remove o aluno do curso anterior (no dicionário `turmas`).
        - Atualiza a tupla do aluno com o novo curso.
        - Reinsere o aluno na lista `alunos` com os dados atualizados.
        - Adiciona o aluno à lista de alunos do **novo curso** no dicionário `turmas`. Se a turma ainda não existir, ela é criada.
        
4. **Validação**
    - Se o aluno **não for encontrado**, o sistema exibe:
        
        `"Aluno não encontrado"`
        
5. **Registro da Ação**
    - Toda ação é registrada na lista `acoes` utilizando o método **`append()`**, garantindo que o histórico do sistema seja preservado.
							
### Exemplo de uso:
```
alunos = [("Lucas", 20, "Engenharia")]
turmas = {"Engenharia": ["Lucas"]}

# Após chamar mudar_de_curso("Lucas", "Arquitetura")
# alunos → [("Lucas", 20, "Arquitetura")]
# turmas → {"Engenharia": [], "Arquitetura": ["Lucas"]}
```

## Cancelar Matrícula

A função **`cancelar_matricula`** é usada quando um aluno decide sair completamente do sistema — seja por desistência, transferência para outra instituição ou fim do vínculo acadêmico.

### Etapas da função

1. **Solicitação de Dados**
    - O sistema solicita apenas:
        - **Nome do aluno** que deseja cancelar a matrícula
        
2. **Busca e Remoção**
    - A função percorre a lista `alunos` para verificar se o aluno está cadastrado.
    - Se encontrado:
        - O aluno é removido da lista `alunos`.
        - Também é removido da lista de alunos da sua respectiva turma (dentro do dicionário `turmas`).
     
3. **Validação**
    - Se o aluno não estiver na lista, é exibida a mensagem:
        - `"Aluno não encontrado"`
        
4. **Registro da Ação**
    - A remoção é registrada na lista `acoes` com um **`append()`**, garantindo o registro do histórico da operação.

### Exemplo de uso:
```
alunos = [("Joana", 22, "Direito")]
turmas = {"Direito": ["Joana"]}

# Após chamar cancelar_matricula("Joana")
# alunos → []
# turmas → {"Direito": []}
```

## Por que utilizamos essas estruturas de dados?

### **Lista de tuplas (`alunos`):**
- Armazena os dados básicos de cada aluno: `(nome, idade, curso)`.
- **Tuplas são imutáveis**, o que ajuda a preservar a integridade dos dados. Se quisermos alterar algo, substituímos a tupla inteira, evitando modificações parciais acidentais.

### **Dicionário (`turmas`):**
- Armazena os cursos como **chaves**, e os alunos (e eventualmente professores) como **valores**, geralmente em listas.
- Isso permite acesso rápido a uma turma específica e facilita a inserção/remoção de membros.

### **Listas dentro do dicionário:**
- Cada chave (curso) aponta para uma lista de alunos, mantendo os dados organizados e com ordem de inserção.
- Também permite múltiplas operações como adicionar, remover ou verificar alunos de maneira eficiente.

### **Lista de ações (`acoes`):**
- Funciona como um **log de atividades**.
- Cada operação relevante (como matrícula, troca de curso, ou cancelamento) é registrada com um `append()`.
- Pode ser usada para auditoria, desfazer ações ou simplesmente acompanhar o histórico do sistema.

### Passo a Passo:
Ao executar o programa, o usuário terá acesso a um menu principal com todas as opções disponíveis no sistema de gerenciamento de cursos. O usuário deve escolher uma opção por vez e fornecer os dados solicitados.

As opções disponíveis são:

1. **Cadastrar Curso**: O usuário informa o nome do curso e a carga horária. Com esses dados, um novo curso é criado e adicionado à lista de cursos.
    
2. **Cadastrar Professor**: O usuário informa o nome do professor e o curso que ele irá lecionar. O professor é então cadastrado na lista de professores.
    
3. **Cadastrar Aluno**: O usuário insere o nome do aluno, idade e o curso desejado. Com essas informações, o aluno é registrado na lista de alunos.
    
4. **Listar Todos**: Exibe todas as listas de cursos, professores e alunos cadastrados no sistema.
    
5. **Mudar de Curso**: O usuário informa o nome do aluno e o novo curso. O sistema transfere o aluno do curso atual para o novo curso selecionado.
    
6. **Cancelar Matrícula**: O usuário informa o nome do aluno que deseja cancelar a matrícula. O aluno é então removido tanto da lista geral quanto da turma à qual pertence.
    
7. **Ver Turmas**: Exibe todas as turmas existentes, organizadas por curso. Mostra os alunos matriculados em cada turma e os professores responsáveis.
    
8. **Ver Últimas Ações**: Apresenta um histórico das últimas ações realizadas pelo usuário no sistema.
    
9. **Sair**: Encerra o programa.

## Como Executar o Programa

### 1. Instalando o Python

1. Verifique se o Python já está instalado em seu computador.
2. Caso não esteja, acesse: https://www.python.org/downloads/
3. Baixe e instale a versão mais recente do **Python 3**.
4. Durante a instalação, **marque a opção "Add Python to PATH"**.
5. Para confirmar se a instalação foi bem-sucedida, abra o terminal (Prompt de Comando) e digite:
    
    ```
    py --version
    ```
    
    ou
    
    ```
    python --version
    ```
    
### 2. Instalando o Git

1. Acesse: https://git-scm.com/downloads
2. Baixe e instale o Git de acordo com o seu sistema operacional (Windows, Linux ou macOS).
3. Após a instalação, verifique se está funcionando com o comando:
    
    ```
    git --version
    ```
    

### 3. Clonando o Repositório e Executando o Projeto

1. No terminal, execute o comando para clonar o repositório:
    
    ```
    git clone https://github.com/oliveira191205/Gerenciamento_de_Cursos.git
    ```
    
2. Acesse a pasta do projeto:
    
    ```
    cd Gerenciamento_de_Cursos
    ```
    
3. Instale as dependências (caso existam) com:
    
    ```
    pip install -r requirements.txt
    ```
    
4. Por fim, execute o programa com:
    
    ```
    py cadastro_cursos.py
    ```
    
    ou
    ```
    python cadastro_cursos.py
    ```


   ### Trabalho desenvolvido por
   ```
    LARISSA VITORIA CUSTODIO DE CARVALHO - RA: 1995354
    MARCELA BUZZO DE OLIVEIRA - RA: 2014340
    VINICIUS MIGUEL DE OLIVEIRA GARCIA - RA: 2002638

    Análise e Desenvolvimento de Sistemas - 3ºC
    ```
    


