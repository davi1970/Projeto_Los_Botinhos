import os
import random as rd
import curses


# ==============================================================
# =============== VARIÁVEIS E CONFIGURAÇÕES GERAIS =============
# ==============================================================

TEXTO_INTRODUCAO = """''Aqueles que vivem as margens do Rio Negro acreditam na existência de uma criatura mística sob suas águas,
um boto-cor-de-rosa, nomeado como “Amazonino”, que se transforma ao cair da noite num belo rapaz perfumado e sedutor com vestes brancas.

Nas celebrações, o boto-cor-de-rosa encatava com facilidade as mulheres com seu dançar e seu olhar sedutor,
e as levava para perto do rio, depois desaparecia e as abandonava ao amanhecer.

Até então nenhum outro boto ousou desafia-lo pelo seu lugar, porém, surge o boto Vaquita nomeado “Chiquito” de origem mexicana muito
atrevido e tão carismático quanto Amazonino, mas com ousadia o suficiente para disputar território e as belas moças que nele habitavam.

Certa noite, Chiquito com muita determinação, desafia Amazonino para uma corrida, para resolver os conflitos entre eles. Quem obtiver
o maior número de acertos nas perguntas alcançará primeiro o local onde as águas negras se encontram com as barrentas e vencerá a disputa.''

"""

# Paleta de cores (valores para ANSI 256 cores)
AZ_C = 37
AZUL = 31
PRET = 0
BRAN = 15
VERD = 70
VD_E = 64
ROSA = 132
CINZ = 102

# Elementos visuais
PIXEL = "██"

# Mapa-base do jogo (cores de cada célula)
MAPA = [
    [VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, PRET, VERD],
    [VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, BRAN, VERD],
    [AZUL, AZUL, AZUL, AZUL, AZUL, VERD, VERD, VERD, VERD, VERD, VERD, VERD, AZUL, AZUL, AZUL, AZUL, PRET, AZUL],
    [AZ_C, AZ_C, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZ_C, BRAN, AZ_C],
    [AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, PRET, AZ_C],
    [AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, BRAN, AZ_C],
    [AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, AZ_C, PRET, AZ_C],
    [AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZ_C, AZ_C, AZ_C, AZ_C, AZUL, AZUL, AZUL, AZUL, AZUL, BRAN, AZUL],
    [VERD, VERD, VERD, VERD, VERD, VERD, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, VERD, VERD, VERD, VERD, PRET, VERD],
    [VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, BRAN, VERD],
    [VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, PRET, VERD]
]

# Dados da corrida
CHEGADA_X = MAPA[0][-2]
PERGUNTAS = [["Pergunta","errado","errado","errado","certo "]]
RESPOSTAS_SIMS = []
RESPOSTAS_NAOS = [
    "NÃO", "não", "nao", "NAO", "Nao", "Não",
    "ñ", "Ñ", "n", "N", "no", "No", "nO",
    "NaO", "NãO", "NÃo", "nÃO", "nAO", "NAo"
]
continuar = True
resposta = ""
infos = [
    True, # continuar
    "", # resposta
    0, # rodada
]
# Estado inicial do jogo
frame_atual = [linha.copy() for linha in MAPA]
amazonino_pos = [4, 1]  # (y, x)
tucuxi_coords = [6, 1]     # (y, x)
amazonino_cor = ROSA
tucuxi_cor = CINZ


# ==============================================================
# ===================== FUNÇÕES AUXILIARES =====================
# ==============================================================

def _printPixel(cor_texto, cor_fundo=0, caractere=PIXEL):
    """Imprime um pixel colorido no terminal usando ANSI."""
    print(f"\033[38;5;{cor_texto};48;5;{cor_fundo}m{caractere}\033[0m", end="")


def _desenharFrame(frame_atual):
    """Renderiza o frame atual (mapa) no terminal."""
    for linha in frame_atual:
        for cor_pixel in linha:
            _printPixel(cor_pixel, cor_pixel)
        print()


def _resetarFrame():
    """Restaura o mapa base sem os personagens."""
    return [linha.copy() for linha in MAPA]


def _desenharBotos(frame):
    """Atualiza o frame com a posição atual dos botos."""
    frame[tucuxi_coords[0]][tucuxi_coords[1]] = tucuxi_cor
    frame[amazonino_pos[0]][amazonino_pos[1]] = amazonino_cor
    return frame


def _nadoTucuxi():
    """Rola os dados e move o boto vencedor."""
    tucuxi_coords[1] += rd.choice([0,1,2])

def _escreverPergunta(perguntas):
    pergunta_escolhida = rd.choice(perguntas)
    resposta = ""
    
    print()
    print(pergunta_escolhida[0])
    
    for i in range(len(pergunta_escolhida)):
        if i == 0: continue
        if pergunta_escolhida[i][-1] == " ":
            resposta = str(i)
        print(f"{i}. {pergunta_escolhida[i]}")
    
    _analisarResposta(input(),resposta)


def _analisarResposta(resposta, resposta_certa = ""):
    """Analisa a resposta e executa funções de acordo com ela"""

    if resposta == resposta_certa:
        amazonino_pos[1] += rd.choice([1,2])
        print(f"Resposta Correta!")
    elif resposta == "sair":
        infos[0] = False
    elif resposta in str([1,2,3,4]) and amazonino_pos[1] != 1:
        amazonino_pos[1] -= rd.choice([1,2])


def _lerInput(stdscr):
    """Lê uma tecla pressionada usando curses."""
    tecla = stdscr.getch()
    return tecla


def _continuar():
    """Pausa até o jogador pressionar Enter."""
    input('Pressione "Enter" para continuar.')


def _limparTela():
    """Limpa o terminal (funciona no Windows, Linux e macOS)."""
    os.system("cls" if os.name == "nt" else "clear")


# ==============================================================
# ===================== ETAPAS DO JOGO =========================
# ==============================================================

def etapaInicial():
    """Prepara o início de uma rodada."""
    _limparTela()


def etapa():
    """Executa a lógica principal e movimentação."""
    _nadoTucuxi()


def etapaFinal():
    """Atualiza e desenha o estado final da rodada."""
    print(f"Rodada: {infos[2]}")
    frame_atual = _resetarFrame()
    frame_atual = _desenharBotos(frame_atual)
    _desenharFrame(frame_atual)
    _escreverPergunta(PERGUNTAS)


# ==============================================================
# ====================== EXECUÇÃO DO JOGO ======================
# ==============================================================

# Exibe a introdução
_limparTela()
print(TEXTO_INTRODUCAO)
_continuar()

# Loop principal do jogo
def main():
    while continuar:
        infos[2]+=1
        etapaInicial()
        etapa()
        etapaFinal()


# Inicia o jogo
main()
