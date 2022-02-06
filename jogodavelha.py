def mostrarTabuleiro():
    cont = 1
    for valor in tabuleiro:

        if valor == 'X':
            #mostrar valor X em vermelho
            print(f'[ \033[1;91m{valor}\033[0;0m ]', end='')
        elif valor == 'O':
            #mostrar valor O em ciano
            print(f'[ \033[1;96m{valor}\033[0;0m ]', end='')
        else:
            #mostrar numero sem formatação
            print(f'[ {valor} ]', end = '')

        if cont % 3 == 0:
            print()
        cont += 1

def atualizarTabuleiro(jogada, simbolo):
    tabuleiro.insert(jogada - 1, simbolo)
    tabuleiro.remove(jogada)


def verificarVelha():

    lista = [str(v) for v in tabuleiro]

    nums = 0
    for item in lista:
        if item.isnumeric():
            nums += 1

    if nums == 0:
        return True

    return False


def verificarVencedor(jogador):
    resultado = [str(v) for v in tabuleiro]

    if jogador == 1:
        simbolo = 'XXX'
    if jogador == 2:
        simbolo = 'OOO'

    #verificação de possibilidades de vitória na horizontal
    if resultado[0] + resultado[1] + resultado[2] == simbolo:
        return True
    if resultado[3] + resultado[4] + resultado[5] == simbolo:
        return True
    if resultado[6] + resultado[7] + resultado[8] == simbolo:
        return True

    # verificação de possibilidades de vitória na vertical
    if resultado[0] + resultado[3] + resultado[6] == simbolo:
        return True
    if resultado[1] + resultado[4] + resultado[7] == simbolo:
        return True
    if resultado[2] + resultado[5] + resultado[8] == simbolo:
        return True

    # verificação de possibilidades de vitória na diagonal
    if resultado[0] + resultado[4] + resultado[8] == simbolo:
        return True
    if resultado[2] + resultado[4] + resultado[6] == simbolo:
        return True

    return False


tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
valores_digitados = set()


while True:
    mostrarTabuleiro()

    while True:
        jogador_1 = int(input("Jogador 1: (X): "))
        if jogador_1 in valores_digitados:
            print('\033[1;31mNumero já jogado, por favor, escolha outro.\033[0;0m')
            continue
        else:
            break
    valores_digitados.add(jogador_1)
    atualizarTabuleiro(jogador_1, 'X')


    #verificações
    verificação_jogador_1 = verificarVencedor(1)
    verificação_jogador_2 = verificarVencedor(2)
    if verificação_jogador_1 or verificação_jogador_2 == True:
        break

    verificação_velha = verificarVelha()
    if verificação_velha == True:
        break

    mostrarTabuleiro()

    while True:
        jogador_2 = int(input("Jogador 2: (O): "))
        if jogador_2 in valores_digitados:
            print('\033[1;31mNumero já jogado, por favor, escolha outro.\033[0;0m')
            continue
        else:
            break

    atualizarTabuleiro(jogador_2, 'O')
    valores_digitados.add(jogador_2)

    #verificações
    verificação_jogador_1 = verificarVencedor(1)
    verificação_jogador_2 = verificarVencedor(2)
    if verificação_jogador_1 or verificação_jogador_2 == True:
        break

    verificação_velha = verificarVelha()
    if verificação_velha == True:
        print('EMPATE: DEU VELHA!')
        break


mostrarTabuleiro()
if verificação_velha == True:
    print('EMPATE: DEU VELHA!')
else:
    if tabuleiro.count('X') > tabuleiro.count('O'):
        print('VITÓRIA: JOGADOR 1 VENCEU!')
    else:
        print('VITÓRIA: JOGADOR 2 VENCEU!')