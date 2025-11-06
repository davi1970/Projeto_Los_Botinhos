import os 
import random as rd




# -- VARIÁVEIS DO JOGO -- #
amazonino_posicao = 0
tucuxi_posicao = 0

# - CONSTANTES - #

AZ_C = 51   
AZUL = 19
PRET = 0       
BRAN = 15
VERD = 46
VD_E = 22
ROSA = 200
CINZ = 245

PIXEL = "██"
TELA = [
    [VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, BRAN, VERD],
    [AZUL, AZUL, AZUL, VERD, VERD, VERD, VERD, VERD, AZUL, AZUL, PRET, AZUL],
    [AZ_C, AZ_C, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZ_C, BRAN, AZ_C],
    [AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, PRET, AZ_C],
    [AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, BRAN, AZ_C],
    [AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, PRET, AZ_C],
    [AZUL, AZUL, AZUL, AZUL, AZUL, AZ_C, AZ_C, AZUL, AZUL, AZUL, BRAN, AZUL],
    [VERD, VERD, VERD, VERD, AZUL, AZUL, AZUL, AZUL, VERD, VERD, PRET, VERD],
    [VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, BRAN, VERD]
]

# -- FUNÇÕES -- #


def desenharFrame(frame_atual):
    for linha in frame_atual:
        for cor_pixel in linha:
            printFormatado(cor_pixel, cor_pixel)
        print()

def rolarDados():
    amazonino_dado = rd.randint(1,6)
    tucuxi_dado = rd.randint(1,6)
    if amazonino_dado > tucuxi_dado:
        pass
    elif amazonino_dado < tucuxi_dado:
        pass
    else:
        pass
    


def limparTela():
    os.system("cls" if os.name == "nt" else "clear") # retorna "cls" se o os.name for igual a "nt" (Sistema Operacional do Windows) e caso não seja, retorna "clear" (Usado para Linux e Mac)
    # global FRAME; FRAME = TELA.copy()


def printFormatado(cor_texto, cor_fundo = 0, caractere=PIXEL):
    print(f"\033[38;5;{cor_texto};48;5;{cor_fundo}m{caractere}\033[0m", end="")



# --EXECUÇÃO DO CÓDIGO-- #

# - Pré-Loop - #
limparTela()

# - Loop - #
while True:
    desenharFrame(TELA)
    input()
    limparTela()
    #  desenharFrame(TELA_X,TELA_Y)