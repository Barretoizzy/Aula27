alunos = [] # lista que vai guardar os dados do aluno
while True:

 escolha_menu = int(input("escolha menu:")) #vairável que guarda qual a escolha do usuário
 if escolha_menu == 1:
            cont = 0  #variável que controla a repetição
            escolha_usuario = int (input("quantos alunos deseja cadastrar:")) #variavel que guarda quantas repetição
            while cont < escolha_usuario:
                nome = input("digite o nome do aluno:") #armazenar o nome do aluno 
                print(nome)
                nota1 = float (input("nota1: "))
                nota2 = float (input("nota2: "))
                nota3 = float (input("nota3: "))
                nota4 = float (input("nota4: "))

                faltas = int (input("número de faltas do aluno: "))

                #calculo da mèdia
                media = (nota1+nota2+nota3+nota4)/4
                print(media)
                if media >= 8:
                    situacao = "você esta aprovado"
                elif media >= 5:
                    recuperacao = float (input("nota da recuperação: "))
                    if recuperacao >=(10-media):
                        situacao = "aprovado na recuperacao"
                    else:
                            situacao = "reprovado na recuperacao"
                else:
                    situacao = "reprovado na media"
                    # enviar os dados do aluno para a lista
                alunos.append([nome, faltas, media, situacao])
                cont += 1
                #relatorio
 elif escolha_menu == 2:  #relatório 
            print(alunos)
 elif escolha_menu == 3: #
        break 