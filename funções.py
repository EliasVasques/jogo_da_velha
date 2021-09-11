from random import choice


def quadro_cheio(quadro):
    if quadro.count(' ') == 0:
        return True


def quem_comeca():
    jogadores = ['computador', 'jogador']
    return choice(jogadores)


def printa_quadro(lista):
    print(lista[0], ' | ', lista[1], ' | ', lista[2])
    print('-' * 13)
    print(lista[3], ' | ', lista[4], ' | ', lista[5])
    print('-' * 13)
    print(lista[6], ' | ', lista[7], ' | ', lista[8])


def validar_numero(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print('Digite um número!')
        else:
            if 1 <= num <= 9:
                return num
            else:
                print('Inváido! digite um número entre 1 e 9.')


def jogar_jogador(quadro):

    while True:
        pos_por = validar_numero('onde quer por? [1-9] ') - 1
        if quadro[pos_por] == ' ':
            quadro[pos_por] = 'x'
            return quadro


def verif_vitoria(quadro, simbolo):
    # FINALIZAR JOGO
    l1 = [quadro[0], quadro[1], quadro[2]]
    l2 = [quadro[3], quadro[4], quadro[5]]
    l3 = [quadro[6], quadro[7], quadro[8]]

    c1 = [quadro[0], quadro[3], quadro[6]]
    c2 = [quadro[1], quadro[4], quadro[7]]
    c3 = [quadro[2], quadro[5], quadro[8]]

    dp = [quadro[0], quadro[4], quadro[8]]
    ds = [quadro[2], quadro[4], quadro[6]]

    if l1.count(simbolo) == 3 or l2.count(simbolo) == 3 or l3.count(simbolo) == 3:
        return True
    if c1.count(simbolo) == 3 or c2.count(simbolo) == 3 or c3.count(simbolo) == 3:
        return True
    if dp.count(simbolo) == 3 or ds.count(simbolo) == 3:
        return True

    return False


def jogar_computador(quadro):

    for pos in range(9):
        copia_quadro = quadro.copy()
        if quadro[pos] == ' ':
            copia_quadro[pos] = '0'
            teste_vitoria = verif_vitoria(copia_quadro, '0')
            if teste_vitoria:
                return copia_quadro

    for pos in range(9):
        copia_quadro = quadro.copy()
        if quadro[pos] == ' ':
            copia_quadro[pos] = 'x'
            teste_vitoria = verif_vitoria(copia_quadro, 'x')
            if teste_vitoria:
                copia_quadro[pos] = '0'
                return copia_quadro

    vazio = []
    for pos in range(9):
        if quadro[pos] == ' ':
            vazio.append(pos)
    aleatorio = choice(vazio)
    quadro[aleatorio] = '0'
    return quadro
