numero1 = float(input(f"Digite o 1º Número: "))  #Inserir o primeiro numero
numero2 = float(input(f"Digite o 2º Número: "))  #Inserir o segundo numero
menu = int(input("Selecione a operação\n"
                 "1 para soma\n"
                 "2 para subtração\n"
                 "3 para multiplicação\n"
                 "4 para divisão\n"
                 "5 digitar novos números\n"
                 "6 para sair\n"
                 "Digite: "))  #Escolher a opção
while menu == 5:
    informe = int(input("Informe qual número você deseja alterar\n"
                        "1 para o 1º número\n"
                        "2 para o 2º número\n"
                        "3 para ambos\n"
                        "digite: "))
    if informe == 1:
        numero1 = float(input(f"Digite um novo valor para o 1º Número: "))  #Inserir o primeiro numero
    elif informe == 2:
        numero2 = float(input(f"Digite um novo valor para o 2º Número: "))  #Inserir o primeiro numero
    else:
        numero1 = float(input(f"Digite um novo valor para o 1º Número: "))  # Inserir o primeiro numero
        numero2 = float(input(f"Digite um novo valor para o 2º Número: "))  #Inserir o segundo numero
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
print("Programa encerrado!!!\n"
      "Obrigado pela sua atenção!!")
