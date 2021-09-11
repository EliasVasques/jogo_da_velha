import funções
from time import sleep

quadro = [' ' for c in range(9)]

if funções.quem_comeca() == 'jogador':
    vez_player = True
    print('Você começa, boa sorte!')
else:
    vez_player = False
    print('Eu começo!')

fim_jogo = False

while True:

    funções.printa_quadro(quadro)
    print('=' * 50)

    empate = funções.quadro_cheio(quadro)
    if empate:
        funções.printa_quadro(quadro)
        print('Empatamos, foi um bom jogo!!!')
        break

    if vez_player:
        print('Sua vez')
        quadro = funções.jogar_jogador(quadro)

        venceu = funções.verif_vitoria(quadro, 'x')
        if venceu:
            funções.printa_quadro(quadro)
            print('Parabéns!')
            break

    else:
        print('Minha vez! deixa eu ver...')
        sleep(2)
        quadro = funções.jogar_computador(quadro)

        venceu = funções.verif_vitoria(quadro, '0')
        if venceu:
            funções.printa_quadro(quadro)
            print('Não fica triste, sou muito bom!')
            break

    vez_player = not vez_player

print('\nObrigado por jogar o meu jogo!')
