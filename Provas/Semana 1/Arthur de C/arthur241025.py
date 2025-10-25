
import os 
import random as rd

sprite = dict[tuple[int],list[str]]
TELA: sprite = {}
FRAME: sprite = {}
TELA_X: int = 20
TELA_Y: int = 10
PIXEL_CHEIO: str = "██"
PIXEL_VAZIO: str = "░░"
CORES_ANSI = {
    "PRETO": 30,
    "VERMELHO": 31,
    "VERDE": 32,
    "AMARELO": 33,
    "AZUL": 34,
    "MAGENTA": 35,
    "CIANO": 36,
    "BRANCO": 37
    }


def limparTela():
    os.system("cls" if os.name == "nt" else "clear") # retorna "cls" se o os.name for igual a "nt" (Sistema Operacional do Windows) e caso não seja, retorna "clear" (Usado para Linux e Mac)
    global FRAME; FRAME = TELA.copy()
def criarTela(x: int ,y: int) -> None:
    for _y in range(y):
        for _x in range(x):
            TELA[(_x, _y)] = [PIXEL_CHEIO,"AZUL"]
def desenharFrame(x: int, y: int,SPRITE: sprite) -> None:
    for _y in range(y):
        for _x in range(x):
            caractere, cor = SPRITE[(_x,_y)]
            printColorido(caractere,cor)
        print()
def criarQuadradoCheio(x1:int, y1:int, x2:int, y2:int, cor:str="BRANCO", caractere:str=PIXEL_CHEIO) -> sprite:
    largura: int = x2 - x1
    altura: int = y2 - y1
    imagem_final: sprite = {}
    for _y in range(altura):
        for _x in range(largura):
            imagem_final[(_x, _y)] = [caractere,cor]
    return imagem_final
def criarQuadrado(x1:int, y1:int, x2:int, y2:int, cor_cheia:str="BRANCO", caractere_cheio:str=PIXEL_CHEIO,caractere_vazio:str=PIXEL_CHEIO,cor_vazia:str="PRETO") -> sprite:
    imagem_final = criarQuadradoCheio(x1,y1,x2,y2,cor_cheia,caractere_cheio).copy()
    imagem_final = criarQuadradoCheio(x1+1,y1+1,x2-1,y2-1,cor_vazia,caractere_vazio)
    return imagem_final
def printColorido(texto: str, cor: str) -> None:
    print(f"\033[{CORES_ANSI[cor]}m{texto}\033[0m", end="")



# --EXECUÇÃO DO CÓDIGO-- #

# -Pré-Loop- #
criarTela(TELA_X,TELA_Y)
FRAME = TELA.copy()

while True:
    limparTela()
    desenharFrame(10,10,criarQuadradoCheio(0,0,10,10))
    

    # desenharFrame(TELA_X,TELA_Y)
