import os
import random as rd
import curses


# ==============================================================
# =============== VARIÁVEIS E CONFIGURAÇÕES GERAIS =============
# ==============================================================

TEXTO_INTRODUCAO = """''Aqueles que vivem as margens do Rio Negro acreditam na existência de uma criatura mística sob suas águas, um boto-cor-de-rosa, nomeado como “Amazonino”, que se transforma ao cair da noite num belo rapaz perfumado e sedutor com vestes brancas.

Nas celebrações, o boto-cor-de-rosa encatava com facilidade as mulheres com seu dançar e seu olhar sedutor, e as levava para perto do rio, depois desaparecia e as abandonava ao amanhecer.

Até então nenhum outro boto ousou desafia-lo pelo seu lugar, porém, surge o boto Vaquita nomeado “Chiquito” de origem mexicana muito atrevido e tão carismático quanto Amazonino, mas com ousadia o suficiente para disputar território e as belas moças que nele habitavam.

Certa noite, Chiquito com muita determinação, desafia Amazonino para uma corrida, para resolver os conflitos entre eles. Quem obtiver o maior número de acertos nas perguntas alcançará primeiro o local onde as águas negras se encontram com as barrentas e vencerá a disputa.''

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

# Dados da corrida
CHEGADA_X = MAPA[0][-2]
RESPOSTAS_SIMS = []
RESPOSTAS_NAOS = [
    "NÃO", "não", "nao", "NAO", "Nao", "Não",
    "ñ", "Ñ", "n", "N", "no", "No", "nO",
    "NaO", "NãO", "NÃo", "nÃO", "nAO", "NAo"
]
continuar = True
pergunta = ""
# Estado inicial do jogo
frame_atual = [linha.copy() for linha in MAPA]
amazonino_coords = [3, 1]  # (y, x)
tucuxi_coords = [5, 1]     # (y, x)
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


def _atualizarFrame(frame):
    """Atualiza o frame com a posição atual dos botos."""
    frame[amazonino_coords[0]][amazonino_coords[1]] = amazonino_cor
    frame[tucuxi_coords[0]][tucuxi_coords[1]] = tucuxi_cor
    return frame


def _rolarDados():
    """Rola os dados e move o boto vencedor."""
    amazonino_dado = rd.randint(1, 6)
    tucuxi_dado = rd.randint(1, 6)
    if amazonino_dado > tucuxi_dado:
        amazonino_coords[1] += 1
    elif amazonino_dado < tucuxi_dado:
        tucuxi_coords[1] += 1
    else:
        pass  # empate → nenhum avança

def _resposta(resposta, resposta_certa = ""):
    """Analisa a resposta e executa funções de acordo com ela"""
    if resposta == resposta_certa:
        amazonino_coords[1] += 1
        print(f"Resposta Correta!")
    elif resposta == "sair":
        contiuar = False
    else:
        print(f"Resposta Errada!")
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
    input()
    _limparTela()


def etapa():
    """Executa a rolagem de dados e movimentação."""
    _rolarDados()


def etapaFinal():
    """Atualiza e desenha o estado final da rodada."""
    frame_atual = _resetarFrame()
    frame_atual = _atualizarFrame(frame_atual)
    _desenharFrame(frame_atual)


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
        etapaInicial()
        etapa()
        etapaFinal()


# Inicia o jogo
main()
