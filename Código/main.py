import os 
import random as rd



# -- VARIÁVEIS DO JOGO -- #

AZ_C = 51   
AZUL = 19
PRET = 0       
BRAN = 15
VERD = 46
VD_E = 22
ROSA = 200
CINZ = 245

PIXEL = "██"
MAPA = [
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
frame_atual = [linha.copy() for linha in MAPA]
amazonino_coords = [3,1] # y, x 
amazonino_cor = ROSA
tucuxi_coords = [5,1] # y, x
tucuxi_cor = CINZ

# -- FUNÇÕES -- #
def desenharFrame(frame_atual):
    for linha in frame_atual:
        for cor_pixel in linha:
            printPixel(cor_pixel, cor_pixel)
        print()


def resetarFrame():
    return [linha.copy() for linha in MAPA]


def atualizarFrame(frame):
    frame[amazonino_coords[0]][amazonino_coords[1]] = amazonino_cor
    frame[tucuxi_coords[0]][tucuxi_coords[1]] = tucuxi_cor
    return frame


def rolarDados():
    amazonino_dado = rd.randint(1,6)
    tucuxi_dado = rd.randint(1,6)
    if amazonino_dado > tucuxi_dado:
        amazonino_coords[1] += 1
    elif amazonino_dado < tucuxi_dado:
        tucuxi_coords[1] += 1
    else:
        pass
    


def limparTela():
    os.system("cls" if os.name == "nt" else "clear") # retorna "cls" se o os.name for igual a "nt" (Sistema Operacional do Windows) e caso não seja, retorna "clear" (Usado para Linux e Mac)
    # global FRAME; FRAME = TELA.copy()


def printPixel(cor_texto, cor_fundo = 0, caractere=PIXEL):
    print(f"\033[38;5;{cor_texto};48;5;{cor_fundo}m{caractere}\033[0m", end="")




# --EXECUÇÃO DO CÓDIGO-- #


# - Pré-Loop - #
limparTela()



# - Loop - #
while True:
    frame_atual = resetarFrame()
    frame_atual = atualizarFrame(frame_atual)
    desenharFrame(frame_atual)
    input()
    rolarDados()
    limparTela()