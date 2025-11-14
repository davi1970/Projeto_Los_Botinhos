import os
import random as rd


# ============================================================== #
# ================== VARIÁVEIS E CONFIGURAÇÕES ================= #
# ============================================================== #

# Texto de introdução do jogo
HISTORIA = """Aqueles que vivem as margens do Rio Negro acreditam na existência de uma criatura mística sob suas águas,
um boto-cor-de-rosa, nomeado “Amazonino”, que se transforma ao cair da noite num belo rapaz perfumado e sedutor com vestes brancas.

Nas celebrações, o boto-cor-de-rosa encantava as mulheres com seu dançar e olhar sedutor,
levando-as para perto do rio, desaparecendo ao amanhecer.

Até então, nenhum outro boto ousou desafiar seu território, porém surge o boto Vaquita nomeado “Chiquito”, 
de origem mexicana, carismático e atrevido, disposto a disputar território e as moças do lugar.

Certa noite, Chiquito desafia Amazonino para uma corrida. Quem acertar mais perguntas chegará primeiro ao encontro das águas negras com as barrentas, vencendo a disputa.
"""

# Paleta de cores ANSI 256
AZ_C = 37
AZUL = 31
PRET = 0
BRAN = 15
VERD = 70
VD_E = 64
ROSA = 132
CINZ = 102
# Elemento visual
PIXEL = "██"

# Mapa-base do jogo (cores)
MAPA = [
    [VERD, VERD, VERD, VERD, VERD, VD_E, VD_E, VD_E, VD_E, VD_E, VD_E, VERD, VERD, VERD, VERD, VERD, PRET, VERD],
    [VERD, VERD, VERD, VERD, VERD, VERD, VD_E, VD_E, VERD, VD_E, VERD, VERD, VERD, VERD, VERD, VERD, BRAN, VERD],
    [AZ_C, BRAN, AZ_C, AZ_C, AZ_C, VERD, VERD, VERD, VERD, VERD, VERD, VERD, AZ_C, AZ_C, BRAN, AZ_C, PRET, AZ_C],
    [AZUL, AZUL, AZUL, AZUL, BRAN, AZ_C, AZ_C, AZ_C, AZ_C, BRAN, AZ_C, BRAN, AZ_C, AZUL, AZUL, AZUL, BRAN, AZUL],
    [AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, PRET, AZUL],
    [AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, BRAN, AZUL],
    [AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, PRET, AZUL],
    [AZ_C, BRAN, AZ_C, BRAN, AZ_C, AZ_C, BRAN, AZUL, AZUL, AZUL, AZUL, AZ_C, AZ_C, AZ_C, BRAN, AZ_C, BRAN, AZ_C],
    [VERD, VERD, VERD, VERD, VERD, VERD, AZ_C, AZ_C, AZ_C, BRAN, AZ_C, BRAN, VERD, VERD, VERD, VERD, PRET, VERD],
    [VD_E, VD_E, VERD, VD_E, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VERD, VD_E, VD_E, VD_E, BRAN, VERD],
    [VD_E, VD_E, VD_E, VD_E, VD_E, VD_E, VERD, VERD, VERD, VERD, VERD, VD_E, VD_E, VD_E, VD_E, VD_E, PRET, VD_E]
]


# Dados da corrida
CHEGADA_X = len(MAPA[0]) - 2  # Posição X da linha de chegada
PERGUNTAS = [
    ["Qual o nome da fruta que contém as seguintes características: cor roxa, fruto da palmeira e predominante na região amazônica?","Acerola","Buriti","Tucumã","Açaí#"],
    ["Qual dos peixes abaixo NÃO faz parte dos peixes da fauna amazônica?","Pirarara","Tambaqui","Jaraqui","Peixe-Palhaço#"],
    ["Em quê tucumã é muito consumido na Amazônia principalmente?","Sucos","Sanduíches e Tapiocas#","Bolos","Sorvete"],
    ["Qual é a lenda do folclore que descreve uma bela sereia que seduz os homens com seu canto?","Lenda da Vitória-régia","Lenda do Curupira","Lenda da Iara#","Lenda do Boto-cor-de-rosa"],
    ["O Rio Madeira possui diversas corredeiras e cachoeiras. Em qual país ele nasce antes de entrar no Brasil?", "Colômbia", "Peru", "Bolívia#", "Venezuela"],
    ["Qual personagem da mitologia amazônica é conhecido como um gigante peludo, com um olho no centro da testa e mau hálito, que assusta caçadores?", "Mapinguari#", "Curupira", "Boitatá", "Jurupari"],
    ["Qual lenda amazônica fala de um boto que se transforma em homem durante as festas e seduz as moças da região?", "Iara", "Curupira", "Boto-cor-de-rosa#", "Mapinguari"],
    ["Complete o ditado: Quem come Jaraqui,…", "Não sai mais daqui#", "Não pisa mais aqui", "Não vem mais aqui", "Não fica mais aqui"],
    ["Qual é o maior felino da Amazônia?", "Jaguatirica", "Onça-pintada#", "Gato-do-mato", "Puma"],
    ["Em quê o buriti é rico?", "Vitamina C", "Vitamina A#", "Ferro", "Cálcio"],
    ["Qual desses peixes possui placas ósseas no corpo e é conhecido por fazer roncos para se comunicar?", "Pacu", "Arraia-d’água-doce", "Bodó#", "Jatuarana"],
    ["A pirarara é um peixe facilmente reconhecido pela:", "Cauda Vermelha intensa#", "Nadadeira dorsal azulada", "Boca em formato de bico", "Escamas brilhantes prateadas"], #12
    ["Qual peixe amazônico é considerado um dos maiores de água doce do mundo, podendo ultrapassar 3 metros?", "Pirarucu#", "Piranha-preta", "Tambaqui", "Jaraqui"],
    ["O Rio Tapajós é conhecido pela cor de suas águas. De que tipo ele é classificado?", "Água branca", "Água barrenta", "Água preta", "Água clara(verde-azulada)#"],
    ["A pupunha deve ser consumida normalmente após:", "Ser frita", "Ser assada", "Ser cozida#", "ser deixada de molho"],
    ["Qual destas frutas possui casca grossa e polpa amarela muito aromática?", "Bacuri", "Pitanga", "Acerola", "Taperebá#"],
    ["Qual destes animais é conhecido por mudar de cor?", "Onça-pintada", "Boto-cor-de-rosa", "Camaleão#", "Tartaruga-da-amazônia"],
    ["Qual fruta amazônica é conhecida por seu sabor ácido e forte aroma, usada em sorvetes?", "Castanha-do-pará", "Cupuaçu#", "Açaí", "Murici"],
    ["Qual rio amazônico é famoso por abrigar o maior arquipélago fluvial do mundo, o Arquipélago de Mariuá?", "Rio Tapajós", "Rio Negro#", "Rio Purus", "Rio Madeira"],
    ["O tambaqui é muito apreciado na culinária amazônica. Ele se alimenta principalmente de:", "Outros peixes", "Frutos e sementes caídos de árvores#", "Insetos aquáticos", "Plâncton"],
    ["Qual peixe amazônico consegue emitir descargas elétricas de alta voltagem para caça e defesa?", "Poraquê#", "Matrinxã", "Traíra", "Aruanã"],
    ["Qual desses répteis amazônicos pode medir mais de 5 metros de comprimento?", "Iguana-verde", "Jacaré-açu#", "Jabuti", "Lagarto-teiú"],
]

# Estado do jogo
infos = [True, "", 0, 0]  # [continuar, resposta_atual, rodada, estado final do jogo (se e quem ganhou)]
frame_atual = [linha.copy() for linha in MAPA]
amazon_coords = [4, 1]  # (y (linha), x (coluna))
tucuxi_coords = [6, 1]  # (y (linha), x (coluna))
amazonino_cor = ROSA
tucuxi_cor = CINZ

# ============================================================== #
# ===================== FUNÇÕES AUXILIARES ===================== #
# ============================================================== #

def _printPixel(cor_texto, cor_fundo=0, caractere=PIXEL):
    """Imprime um pixel colorido no terminal usando ANSI."""
    print(f"\033[38;5;{cor_texto};48;5;{cor_fundo}m{caractere}\033[0m", end="")

def _desenharFrame(frame):
    """Renderiza o frame atual (mapa + personagens) no terminal."""
    for linha in frame:
        for cor_pixel in linha:
            _printPixel(cor_pixel, cor_pixel)
        print()

def _resetarFrame():
    """Restaura o mapa base, sem os personagens."""
    return [linha.copy() for linha in MAPA]

def _desenharBotos(frame):
    """Atualiza o frame com as posições atuais dos botos."""
    frame[tucuxi_coords[0]][tucuxi_coords[1]] = tucuxi_cor
    frame[amazon_coords[0]][amazon_coords[1]] = amazonino_cor
    return frame

def _nadoTucuxi():
    """Move o Tucuxi de forma aleatória (0 a 2 casas)."""
    tucuxi_coords[1] = min(tucuxi_coords[1] + rd.choice([0,1,2]), len(MAPA[0])-1)

def _limparTela():
    """Limpa o terminal (Windows, Linux, macOS)."""
    os.system("cls" if os.name == "nt" else "clear")

def _continuar():
    """Pausa até o jogador pressionar Enter."""
    input('\nPressione "Enter" para continuar.\n')

# ============================================================== #
# ==================== LÓGICA DAS PERGUNTAS ==================== #
# ============================================================== #

def _escreverPergunta(perguntas):
    """
    Escolhe aleatoriamente uma pergunta, embaralha alternativas e imprime.
    Marca a resposta correta e chama o analisador.
    """

    pergunta_escolhida = rd.choice(perguntas)
    resposta = ""
    alternativas = rd.sample(pergunta_escolhida[1:],4)    
    
    print()
    print(pergunta_escolhida[0]+"?\n")
    for i in range(len(alternativas)):
        if alternativas[i][-1] == "#":
            resposta = str(i+1)
        print(f"{i+1}. {alternativas[i][:-1] if alternativas[i][-1] == str('#') else alternativas[i]}")
    
    _analisarResposta(input(),resposta)

def _analisarResposta(resposta, resposta_certa=""):
    """
    Analisa a resposta do jogador:
    - Se correta, Amazonino avança 1-2 casas
    - Se errada, Amazonino recua 1-2 casas
    - Se 'sair', encerra o jogo
    """
    if resposta.lower() == "sair":
        print("Encerrando programa")
        infos[0] = False
        return

    if resposta == resposta_certa:
        desloc = rd.choice([1,2])
        amazon_coords[1] = min(amazon_coords[1] + desloc, len(MAPA[0])-1) # "len(MAPA[0])-1" dá a coord x máxia da tela 
        print(f"Resposta correta! Amazonino avança {desloc} casas.")
    else:
        desloc = rd.choice([1,2])
        amazon_coords[1] = max(0, amazon_coords[1] - desloc) # impede que o boto se mova para "fora"
        print(f"Resposta errada. Amazonino recua {desloc} casas.")
    _continuar()

def _finalizarJogo():
    infos[0] = False

def _resultadoCorrida():
    _limparTela()
    if amazon_coords[1] > tucuxi_coords[1]:
        infos[3] = 1
    elif amazon_coords[1] < tucuxi_coords[1]:
        infos[3] = 1
    _finalizarJogo()
# ============================================================== #
# ===================== ETAPAS DO JOGO ========================= #
# ============================================================== #

def etapaInicial():
    """Prepara início da rodada (limpa tela)."""
    _limparTela()
    

def etapa():
    """Executa movimentação do Tucuxi."""
    _nadoTucuxi()

def etapaFinal():
    """Atualiza o frame, desenha botos e faz a pergunta."""
    print(f"Rodada: {infos[2]}\n")
    frame = _resetarFrame()
    frame = _desenharBotos(frame)

    if (amazon_coords[1] == len(MAPA[0])-2) or (tucuxi_coords[1] == len(MAPA[0])-2):
        _resultadoCorrida()

    _desenharFrame(frame)
    _escreverPergunta(PERGUNTAS)

# ============================================================== #
# ====================== LOOP PRINCIPAL ======================= #
# ============================================================== #

def main():
    """Loop principal do jogo."""
    _limparTela()
    print(HISTORIA)
    _continuar()

    while infos[0]:
        infos[2] += 1
        etapaInicial()
        etapa()
        etapaFinal()

    if infos[2] == 0:
        print("Empate")
    elif infos[2] == 1:
        print("Amazonino Ganhou!")
    else:
        print("Chiquito Ganhou")
    _continuar()
# Inicia o jogo
if __name__ == "__main__":
    main()
