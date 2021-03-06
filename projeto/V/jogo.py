# -*- coding: UTF-8 -*-

# Jogo da Velha
# Marianne Linhares, 26/02/2017

'''
    Versao V - Ufaaaaaaaa!

'''

def imprimir_menu():
    print '------------------------', 'JOGO DA VELHA', '-------------------------------'

    print ('coloque aqui informações sobre o jogo, '
           'e explicação sobre o menu...')

def opcoes_menu():
    print '----------------------------------------------------------------------'
    print 'digite:'
    print '----------------------------------------------------------------------'
    print '1 - Iniciar nova partida'
    print '2 - Visualizar histórico de partidas'
    print '3 - Sair'
    print '----------------------------------------------------------------------'

    opcao_menu = raw_input()
    return opcao_menu

def opcoes_nome_jogadores(nome_jogador1, nome_jogador2):
    print '----------------------------------------------------------------------'
    print 'nome do jogador 1:', nome_jogador1
    print 'nome do jogador 2:', nome_jogador2
    print '----------------------------------------------------------------------'
    print 'digite:'
    print '----------------------------------------------------------------------'
    print 'I - Iniciar partida'
    print 'X - Trocar nome do jogador 1 (X)'
    print 'O - Trocar nome do jogador 2 (O)'
    print '----------------------------------------------------------------------'

    opcao_nome_jogador = raw_input()
    return opcao_nome_jogador

def perguntar_nome_jogadores():

    nome_jogador1 = raw_input('Insira o nome do jogador 1 (X): ')
    nome_jogador2 = raw_input('Insira o nome do jogador 2 (O): ')

    opcao = opcoes_nome_jogadores(nome_jogador1, nome_jogador2)
    if opcao == 'I':
        print 'iniciar partida'
    elif opcao == 'X':
        print 'trocar nome do jogador 1 (X)'
    elif opcao == 'O':
        print 'trocar nome do jogador 2 (O)'
    else:
        print 'Opção inválida'

    return nome_jogador1, nome_jogador2

def iniciar_jogo():

    nome_jogador1, nome_jogador2 = perguntar_nome_jogadores()

def jogo_da_velha():

    imprimir_menu()

    opcao_menu = opcoes_menu()
    if opcao_menu == '1':
        print 'iniciar jogo'
        iniciar_jogo()
    elif opcao_menu == '2':
        print 'visualizar histórico'
    elif opcao_menu == '3':
        print 'sair do jogo'
    else:
        print 'entrada inválida'

if __name__ == '__main__':
    jogo_da_velha()
