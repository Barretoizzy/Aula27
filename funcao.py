# declarando as função
def saudacoes(hora_do_dia): #EXIBIR A SAUDAÇÃO CORRESPONDENTE A HORA DO DIA
    #DAR BOM DIA
    if (hora_do_dia >= 0) and (hora_do_dia <= 12):
        print("BUENOS DIAS!!!")
    elif (hora_do_dia >= 13) and (hora_do_dia <= 18): 
        print("BUENAS TARDES!!!")
    elif (hora_do_dia >= 19) and (hora_do_dia <= 23.59):
        print("BUENAS NOCHES!!!")

#FORA DA FUNÇÃO
#PEÇO PARA O USUÁRIO DIZER A HORA ATUAL
resposta = int(input("digite que horas são: \n"))

saudacoes(resposta)

