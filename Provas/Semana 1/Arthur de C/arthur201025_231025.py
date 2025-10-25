import os
import random as rd

tela: list[str] = []
def print_colorido(cor: str, texto) -> None:
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
    print(f"\033[{CORES_ANSI[cor]}m{texto}\033[0m")


def rolar_dados() -> int:
    return rd.randint(1,6)

def criar_canvas(y_canvas: int,x_canvas: int, valor: str = "▇▇") -> list:
    return [[valor for _ in range(x_canvas)] for _ in range(y_canvas)]



def desenhar_canvas(canvas: list[list[str]]) -> None:
    for i in canvas:
        print_colorido("PRETO","".join(i))
    

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear") # retorna "cls" se o os.name for igual a "nt" (Sistema Operacional do Windows) e caso não seja, retorna "clear" (Usado para Linux e Mac)

tela = criar_canvas(20,50)  
while True:
    limpar_tela()
    tela[1][1] = "O"
    
    desenhar_canvas(tela)
    tela[1][2] = "▇▇"
    
