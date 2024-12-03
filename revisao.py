#ler entradas do usuário
cont = 0
escolha_usuario = int (input())
while cont < escolha_usuario:
    nome = input("digite o nome do aluno:") #armazenar o nome do aluno 

    nota1 = float (input())
    nota2 = float (input())
    nota3 = float (input())
    nota4 = float (input())

    faltas = int (input())

    #calculo da mèdia
    media = (nota1+nota2+nota3+nota4)/4
    print(media)
    if media >= 8:
        situacao = "você esta aprovado"
    elif media >= 5:
        recuperacao = float (input())
        if recuperacao >=(10-media):
            situacao = "aprovado na recuperacao"
        else:
                situacao = "reprovado na recuperacao"
    else:
        situacao = "reprovado na media"
        #relatorio
        print("nome:", nome)
        print("notas:", nota1, nota2, nota3, nota4)
        print("faltas:", faltas)
        print("media:", media)
        print("situacao:", situacao)
        cont = cont + 1