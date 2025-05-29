						 Sistema de Gerenciamento de Cursos
O sistema desenvolvido é um programa de cadastro simples que permite registrar informações de cursos, professores e alunos. Além disso, o sistema conta com uma funcionalidade extra que exibe as últimas ações realizadas, funcionando como um pequeno histórico. O funcionamento do programa é baseado em um menu interativo, onde o usuário escolhe as opções através da digitação de números. O menu é exibido continuamente até que o usuário opte por sair do sistema.
Cadastro de Cursos
Na função cadastrar_curso (), o sistema solicita ao usuário:

	•	Nome do curso

	•	Carga horária
Essas duas informações são armazenadas em uma tupla, que agrupa os dados do curso. Em seguida, essa tupla é adicionada à lista cursos, que guarda todos os cursos cadastrados. A ação de cadastro também é registrada na lista acoes, para manter o histórico.
A lista cursos é usada porque permite armazenar vários cursos dinamicamente. Toda vez que um novo curso é cadastrado, ele é adicionado ao final da lista com. append().
Cadastro de Professores
Na função cadastrar_professor (), o usuário informa:

	•	 Nome do professor
	•	 Curso que ele leciona
Esses dois dados são agrupados em uma tupla (nome, curso) e adicionados à lista professores. Assim como nos cursos, a ação é registrada na lista acoes.

	•  A tupla foi usada para armazenar os dados fixos de cada professor.
 
	•  A lista professores serve para manter todos os registros em ordem de cadastro.
 
							Cadastro de Alunos
Na função cadastrar_aluno (), o sistema solicita:

	•	O nome do aluno
	
	•	A idade

Esses dados são salvos em uma tupla (nome, idade) e armazenados na lista alunos. A ação de cadastro também é registrada na lista acoes.

	•  A tupla foi usada para representar cada aluno individualmente, com dados fixos.
	
	•  A lista alunos permite armazenar todos os cadastros de forma sequencial e dinâmica.

A lista acoes funciona como uma pilha de ações recentes. A cada vez que um curso, professor ou aluno é cadastrado, uma mensagem é adicionada ao final dessa lista.

Na função mostrar_acoes (), o sistema exibe as últimas 5 ações realizadas, utilizando reversed () para mostrar da mais recente até a mais antiga.

	•  A lista é usada porque permite adicionar elementos de forma simples com append().
 
	•  A exibição invertida é feita para simular uma pilha, onde o último item adicionado é o primeiro a ser mostrado.
O sistema funciona com um laço de repetição while,True, que exibe as escolhas do usuário que são tratadas com estruturas if, elif e else, que verificam qual opção foi digitada e chamam a função correspondente.

							Gerenciamento de Cursos
O gerenciamento das turmas funciona de forma a que, para cada curso que estiver na lista de cursos, ele cria um dicionário no qual o nome do curso é a chave, e essa chave é um outro dicionário, composto por duas listas, uma de professores na turma e outra de alunos na turma. Cada aluno é inserido da sua turma correspondente por meio da comparação do nome da chave e do curso já cadastrado em suas informações, para os professores, o mesmo ocorre. 

A saída de visualização das turmas acessa a chave do dicionário turmas, ou seja o nome do curso, e verifica se a lista de alunos tem dados e os exibe, se a lista estiver vazia, ele exibe a mensagem “Turma sem alunos”. A mesma verificação é feita para os professores, logo, se a lista de professores estiver vazia o programa exibe “Turma sem professor”.

	•  A lista é usada porque além de ser mutável, como mencionado, permite adicionar elementos de forma simples com append().
 
	•  O dicionário foi utilizado visando agrupar as informações das turmas de uma forma mais organizada, uma vez que precisamos nomear tais elementos para sua identificação e a forma mais fácil de sua manipulação, com a inserção e alteração de listas por exemplo, contribuíram para a escolha desse elemento na estrutura do código 

							Mudar de curso
A função mudar_de_curso tem o objetivo de transferir um aluno de um curso para outro. Nela, o sistema solicita que o usuário preencha os seguintes dados:

	•	Nome do aluno
 
	•	Novo curso
 
A partir desses dados, o sistema utiliza a função enumerate() para percorrer a lista alunos, analisando os itens (nome, idade e curso_atual). Se o nome for igual ao nome digitado pelo usuário, o sistema atualiza as informações do aluno, removendo-o do curso antigo e adicionando-o ao novo curso. Se o nome não existir na lista alunos, o sistema retorna a mensagem "Aluno não encontrado".

O sistema também verifica se o novo curso já existe em turmas; caso não exista, ele cria esse novo curso e o adiciona ao dicionário de turmas.
Ao final, a ação é registrada na lista acoes com um append(), e a função é encerrada com um return.

							Cancelar matrícula
A função cancelar_matricula tem o objetivo de remover um aluno completamente do sistema, como se ele estivesse se desligando do curso. Nela, o sistema solicita que o usuário preencha o seguinte dado:

	•	Nome do aluno
 
Com base nesse dado, o sistema verifica se o aluno existe na lista alunos. Se encontrado, o aluno é removido tanto da lista geral quanto da turma correspondente. Se o nome não for encontrado, é exibida a mensagem "Aluno não encontrado".

Como nas demais funções, a ação é registrada na lista acoes por meio de um append.

							Por que utilizamos essas estruturas de dados?
Lista de tuplas (alunos): As tuplas são imutáveis, o que ajuda a evitar alterações informações dos alunos.
Dicionário (turmas): Ideal para organizar os cursos, pois permite acesso rápido aos dados de cada turma por meio de chaves.
Listas dentro do dicionário: Usadas para armazenar os alunos e professores de cada turma, mantendo a organização e a ordem de inserção.
Lista de ações (acoes): Serve como registro histórico de tudo o que aconteceu no sistema (como mudanças de curso ou cancelamentos), funcionando como um log.

Passo a passo de como funciona o sistema
Ao executar o programa o usuário terá acesso a um Menu com todas as opções de ações que ele pode fazer dentro do sistema de gerenciamento de cursos, ele deve escolher uma dessas opções de cada vez e inserir os dados solicitados por cada uma delas:
As opções são as seguintes:
1.	Cadastrar curso: O usuário deve inserir o nome do curso e carga horária, a partir dessas informações um novo curso é criado e armazenado na lista cursos.
2.	Cadastrar Professor: O usuário deve inserir o nome do professor e o curso que ele lesiona, a partir dessas informações este professor é cadastrado na lista professores.
3.	Cadastrar Alunos: O usuário deve inserir o nome do aluno, idade e curso, a partir dessas informações este aluno é cadastrado na lista de alunos.
4.	Listar Todos: Mostra as listas completas de cursos, professores e alunos cadastrados.
5.	Mudar de Curso: O usuário deve inserir o nome do aluno e o novo curso para qual ele deseja mudar, a partir desta ação o aluno é retirado do curso antigo e adicionado para o novo curso.
6.	Cancelar Matrícula: O usuário deve inserir o nome do aluno que vai cancelar a matricula, a partir desta informação o aluno com este mesmo nome é removido da lista geral e da sua turma respectiva.
7.	Ver Turmas: Nesta opção será exibida todas as turmas criadas dentro do sistema, separadas pelos cursos, sendo exibido os alunos matriculados nelas e os professores que ministram na mesma.
8.	Ver ultimas ações: Nesta opção será exibida as ultimas ações que o usuário executou, como um histórico.
9.	Sair: Encerra o programa.

							 Como executar o programa


 	Instalando Python:

	1. Certifique-se  que tenha o Python instalado em seu PC.
 	2. Se não tiver acesse https://www.python.org/downloads/
  	3.Baixe e instale a versão mais recente do Python 3.
 	4. Durante a instalação, marque a opção "Add Python to PATH".
  	5. Para testar se está funcionando, abra o terminal (Prompt de Comando) e digite: py --version

   	Instalando Git:
  	
  	6. Acesse: https://git-scm.com/downloads
  	7. Baixe e instale o Git para o seu sistema (Windows, Linux ou macOS).
  	8. Após a instalação, abra o terminal e teste com:
   	9. git --version
  
    Clonando o repositório e executando o projeto
       
     10. Abra o terminal e execute: git clone https://github.com/oliveira191205/Gerenciamento_de_Cursos.git
     11. Acesse a pasta do arquivo com: cd Gerenciamento_de_Cursos
     12. Instale as dependências do projeto com pip install -r requirements.txt
     13. Execute o projeto com py cadastro_cursos.py ou python cadastro_cursos.py

