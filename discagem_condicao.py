menu = 5
novo = ''
while menu != 6:
    numero1 = float(input(f"Digite {novo} o 1º Número: "))
    numero2 = float(input(f"Digite {novo} o 2º Número: "))
    menu = int(input("informe a opção\n"
                     "1 para soma\n"
                     "2 para subtração\n"
                     "3 para multiplicação\n"
                     "4 para divisão\n"
                     "5 digitar um novo numero\n"
                     "6 para sair\n"
                     "Digite: "))
    match menu:
        case 1:
            soma = numero1 + numero2
            print(f"A soma dos valores {numero1}+ {numero2} = {soma}")
        case 2:
            subtracao = numero1 - numero2
            print(f"A subtração dos valores {numero1} - {numero2} = {subtracao}")
        case 3:
            multiplicacao = numero1 * numero2
            print(f"A multiplicação dos valores {numero1} X {numero2} = {multiplicacao}")
        case 4:
            if numero2 == 0:
                numero2 = int(input("Não é possível divisão por 0\n"
                                    "Informe um novo valor para o 2º Número: "))
            divisao = numero1 / numero2
            print(f"A divisão dos valores {numero1} / {numero2} = {divisao}")
        case 5:
            print(end='')
            novo = 'um novo valor para'
else:
    print("Obrigado pela sua atenção!!")
