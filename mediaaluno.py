# função para calcular a media
def calcular_media(notas):
    # A função recebe uma lista de notas e retorna a média, somando as notas e dividindo pelo número
   return sum(notas) / len(notas)
 # função para determinar a situação do aluno com base na média e no número de faltas 
def situacao_aluno(media, faltas):
    # se o aluno tiver mais de 20 faltas, ele será reprovado por falta 
    if faltas >20:
        return "reprovado por falta"
    # se a média for 7 ou mais, o aluno é aprovado
    elif media >=7:
        return "aprovado"
    # se a mèdia for entre 5 e 6.99, o aluno está em recuperação 
    elif media <= 5:
        return "recuperação"
    # se a média for menor que 5, o aluno é reprovado
    else:
        return "reprovado"
    # função para obter os dados dos alunos e gerar o relatório final
def gerar_relatorio(num_alunos):
        alunos = []  #inicializando a lista que armazenará os dados do alunos

        # loop que coleta os dados de cada aluno 
        for i in range(num_alunos):
            #exibe o número do aluno
            print(f"nAluno {i+1}:")

        # coleta o nome do aluno
        nome = input("digite o nome do aluno: ")

        # coleta o número de faltas do aluno
        faltas = int (input("digite o número de faltas: "))

        # lista para armazenar as notas do aluno
        notas = []

        # loop para coletar as notas do 4 bimestres 
        for j in range (4):  # considerando 4 bimestres
            # coleta a nota de cada bimestre e converte para float
            nota = float(input(f"digite a nota do {j+1}º bimestre"))
            # adiciona a nota á lista de notas
            notas.append(nota)

        # calcula a média das notas usando a função definida anteriormente
        media = calcular_media(notas)

        # determina a situação do aluno com base na média e faltas
        situacao = situacao_aluno(media, faltas)

        #cria um dicionário com as informações do aluno 
        aluno = {
              "nome": nome,
              "faltas": faltas,
              "notas": notas,
              "media": media,
              "situacao": situacao,
        }
        
        # adiciona o dicionário de dados do aluno á lista de alunos 
        alunos.append(aluno)
    #exibe o relatório final de todos os alunos 
print("/nrelatório final:")
# cabeçalho com a estrutura de tabela
print(f"{'nome':<20} {'faltas':<7} {'media':>6} {'situação'}")
print("_" *50)
# loop para exibir as informações de cada aluno 
for aluno in alunos:

