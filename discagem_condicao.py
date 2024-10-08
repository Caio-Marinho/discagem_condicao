menu = 5
novo = ''
while menu != 6:
    numero1 = float(input(f"Digite {novo} o 1º Número: "))  #Inserir o primeiro numero
    numero2 = float(input(f"Digite {novo} o 2º Número: "))  #Inserir o segundo numero
    menu = int(input("Selecione a operação\n"
                     "1 para soma\n"
                     "2 para subtração\n"
                     "3 para multiplicação\n"
                     "4 para divisão\n"
                     "5 digitar novos números\n"
                     "6 para sair\n"
                     "Digite: "))  #Escolher a opção

    match menu:
        case 1:  #soma
            soma = numero1 + numero2
            print(f"A soma dos valores {numero1} + {numero2} = {soma}")
        case 2:  #subtração
            subtracao = numero1 - numero2
            print(f"A subtração dos valores {numero1} - {numero2} = {subtracao}")
        case 3:  #multiplicação
            multiplicacao = numero1 * numero2
            print(f"A multiplicação dos valores {numero1} X {numero2} = {multiplicacao}")
        case 4:  # divisão
            while numero2 == 0:  #verifica se não é uma divisão por 0
                numero2 = float(input("Não é possível divisão por 0\n"
                                      "Informe um novo valor para o 2º Número: "))
            divisao = numero1 / numero2
            print(f"A divisão dos valores {numero1} / {numero2} = {divisao}")
        case 5:  #repete para inserir um novo número
            print(end='')
            novo = 'um novo valor para'
        case 6:
            print(end='')
        case _:
            print("Opção Invalida!!")
    if menu != 5 and menu != 6:
        print("Começando novamente...")
else:  #é chamado caso 6 seja selecionado
    print("Programa encerrado!!!\n"
          "Obrigado pela sua atenção!!")
