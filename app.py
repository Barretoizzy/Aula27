        # cadastro DE USUÁRIO E SENHA
       # MENU PRINCIPAL
saldo = 0.0  #variável que guarda o saldo do usuário
while True:
    print("Bem vindo! \n digite 1.cadastrar 2.login 3. encerrar")
            # LER A ESCOLHA DO USUÁRIO
    escolha_menu = int(input()) #Lê A ESCOLHA COM UM NÚMERO

            #SE USUÁRIO ESCOLHER CADASTRO
    if escolha_menu == 1:
                usuario = input("crie um nome de usuário")
                senha = input("crie uma senha")
    elif escolha_menu == 2: #seusuário escolher login
        #comparar as informações cadastradas com uma leitura
        login_usuario = input("digite seu usuário:")
        login_senha = input("digite sua senha:")
        if login_usuario == usuario and login_senha == senha:
            print("LOGIN REALIZADO COM SUCESSO")
            #SE LOGIN CORRETO, ENTRA NO 
            #MENU PRINCIPAL DO APP
            print("Bem vindo", usuario)
            while True: #enquanto que exibirá o menu principal
                print("1. Deposito 2. sacar 3. pix 4. extrato 5. encerrar")
                escolha_principal = int(input())
                #se usuário escolher deposito
                if escolha_principal == 1:
                    #lÊ o valor a ser deposito
                    valor_deposito = float(input("digite o valor do deposito"))   
                    saldo = saldo + valor_deposito  #ATUALIZA O VALOR 
                elif escolha_principal == 2: #SAQUE 
                    valor_saque = float(input("digite o valor do saque"))
                    senha_saque = input("digite sua senha:")
                    if senha_saque == senha:
                         saldo = saldo - valor_saque #subtrai o valor do saldo 
                    elif escolha_principal == 3:  
                         valor_pix = float(input("digite o valor do pix"))    
                         senha_pix = input("digite sua senha")    
                         if senha_pix == senha:
                              saldo = saldo - valor_pix 
                         else:
                              print("senha incorreta")
                elif escolha_principal == 4:  #se usuário escolher visualizar 
                     senha_extrato = input("digite sua senha")
                     if senha_extrato == senha:
                          print("extrato: ", saldo)  
                     else:
                          print("senha incorreta") 
                elif escolha_principal == 5:  #ENCERRAR
                     senha_encerrar = input("digite sua senha")
                     if senha_encerrar == senha:
                          break
                     else:
                          print("senha incorreta")      
                    
        else:

           print("USUÁRIO OU SENHA INCORRETOS")
        