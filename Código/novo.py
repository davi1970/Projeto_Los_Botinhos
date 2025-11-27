import os
import random as rd


# ============================================================== #
# ----------------- VARIÁVEIS E CONFIGURAÇÕES ------------------ #
# ============================================================== #

# Texto de introdução do jogo
HISTORIA = [
"Aqueles que vivem as margens do Rio Negro acreditam na existência de uma criatura mística sob suas águas, um boto-cor-de-rosa, nomeado “Amazonino”, que se transforma ao cair da noite num belo rapaz perfumado e sedutor com vestes brancas.", 
"Nas celebrações, o boto-cor-de-rosa encantava as mulheres com seu dançar e olhar sedutor, levando-as para perto do rio, desaparecendo ao amanhecer.",
"Até então, nenhum outro boto ousou desafiar seu território, porém surge o boto Vaquita nomeado “Chiquito”, de origem mexicana, carismático e atrevido, disposto a disputar território e as moças do lugar.",
"Certa noite, Chiquito desafia Amazonino para uma corrida. Apenas aquele que entender mais sobre a floresta em que estão chegará primeiro ao encontro das águas negras com as barrentas, vencendo a disputa."
]


# Paleta de cores e pixel
AZ_C = 37
AZUL = 31
PRET = 0
BRAN = 15
VERD = 70
VD_E = 64
ROSA = 132
LARA = 208
CINZ = 102

PIXEL = "██"

# Mapa-base do jogo (cores & tamanho)
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




# Perguntas, alternativas e respostas corretas
# Perguntas (1º informação é a pergunta e o último é a resposta)
perguntas = [
    ["Qual o nome da fruta que contém as seguintes características: cor roxa, fruto da palmeira e predominante na região amazônica?",
     "Acerola", "Buriti", "Tucumã", "Açaí"],

    ["Qual dos peixes abaixo NÃO faz parte dos peixes da fauna amazônica?",
     "Pirarara", "Tambaqui", "Jaraqui", "Peixe-Palhaço"],

    ["Em quê tucumã é muito consumido na Amazônia principalmente?",
     "Sucos", "Bolos", "Sorvete", "Sanduíches e Tapiocas"],

    ["Qual é a lenda do folclore que descreve uma bela sereia que seduz os homens com seu canto?",
     "Lenda da Vitória-régia", "Lenda do Curupira", "Lenda do Boto-cor-de-rosa", "Lenda da Iara"],

    ["O Rio Madeira possui diversas corredeiras e cachoeiras. Em qual país ele nasce antes de entrar no Brasil?",
     "Colômbia", "Peru", "Venezuela", "Bolívia"],

    ["Qual personagem da mitologia amazônica é conhecido como um gigante peludo, com um olho no centro da testa e mau hálito, que assusta caçadores?",
     "Curupira", "Boitatá", "Jurupari", "Mapinguari"],

    ["Qual lenda amazônica fala de um boto que se transforma em homem durante as festas e seduz as moças da região?",
     "Iara", "Curupira", "Mapinguari", "Boto-cor-de-rosa"],

    ["Complete o ditado: Quem come Jaraqui,…",
     "Não pisa mais aqui", "Não vem mais aqui", "Não fica mais aqui", "Não sai mais daqui"],

    ["Qual é o maior felino da Amazônia?",
     "Jaguatirica", "Gato-do-mato", "Puma", "Onça-pintada"],

    ["Em quê o buriti é rico?",
     "Vitamina C", "Ferro", "Cálcio", "Vitamina A"],

    ["Qual desses peixes possui placas ósseas no corpo e é conhecido por fazer roncos para se comunicar?",
     "Pacu", "Arraia-d’água-doce", "Jatuarana", "Bodó"],

    ["A pirarara é um peixe facilmente reconhecido pela:",
     "Nadadeira dorsal azulada", "Boca em formato de bico", "Escamas brilhantes prateadas", "Cauda Vermelha intensa"],

    ["Qual peixe amazônico é considerado um dos maiores de água doce do mundo, podendo ultrapassar 3 metros?",
     "Piranha-preta", "Tambaqui", "Jaraqui", "Pirarucu"],

    ["O Rio Tapajós é conhecido pela cor de suas águas. De que tipo ele é classificado?",
     "Água branca", "Água barrenta", "Água preta", "Água clara(verde-azulada)"],

    ["A pupunha deve ser consumida normalmente após:",
     "Ser frita", "Ser assada", "ser deixada de molho", "Ser cozida"],

    ["Qual destas frutas possui casca grossa e polpa amarela muito aromática?",
     "Bacuri", "Pitanga", "Acerola", "Taperebá"],

    ["Qual destes animais é conhecido por mudar de cor?",
     "Onça-pintada", "Boto-cor-de-rosa", "Tartaruga-da-amazônia", "Camaleão"],

    ["Qual fruta amazônica é conhecida por seu sabor ácido e forte aroma, usada em sorvetes?",
     "Castanha-do-pará", "Açaí", "Murici", "Cupuaçu"],

    ["Qual rio amazônico é famoso por abrigar o maior arquipélago fluvial do mundo, o Arquipélago de Mariuá?",
     "Rio Tapajós", "Rio Purus", "Rio Madeira", "Rio Negro"],

    ["O tambaqui é muito apreciado na culinária amazônica. Ele se alimenta principalmente de:",
     "Outros peixes", "Insetos aquáticos", "Plâncton", "Frutos e sementes caídos de árvores"],

    ["Qual peixe amazônico consegue emitir descargas elétricas de alta voltagem para caça e defesa?",
     "Matrinxã", "Traíra", "Aruanã", "Poraquê"],

    ["Qual desses répteis amazônicos pode medir mais de 5 metros de comprimento?",
     "Iguana-verde", "Jabuti", "Lagarto-teiú", "Jacaré-açu"],
]


infos = [True, "", 0, 0, ["","",""],[linha.copy() for linha in MAPA]]  
# 1º. continuar
# 2º. resposta_atual
# 3º. rodada
# 4º. estado final do jogo (se e quem ganhou)
# 5º. dados da pergunta escolhida no momento  [pergunta, alternativas, reposta]
# 6º. frame atual


CHEGADA_X = len(MAPA[0]) - 2  # Posição X da linha de chegada
amazon_coords = [4, 1]  # (y (linha), x (coluna))
tucuxi_coords = [6, 1]  # (y (linha), x (coluna))

amazonino_cor = ROSA
tucuxi_cor = CINZ
 
# ============================================================== #
# --------------------- FUNÇÕES AUXILIARES --------------------- #
# ============================================================== #


# --------------------FUNÇÕES DE ENTRADA -------------------- #
def _continuar():
    """Pausa até o jogador pressionar Enter."""
    input('\nPressione "Enter" para continuar.\n')

def _perguntar():
    """
    Solicita e valida a resposta do jogador.
    
    A resposta deve ser um número entre 1-4 ou 'sair' para finalizar o jogo.
    Caso a resposta seja inválida, solicita novamente até obter uma resposta válida.
    """
    infos[1] = input().lower()
    if infos[1] not in ["1","2","3","4","sair"]:
        print('Insira uma resposta válida. (1,2,3,4 ou "sair",para finalizar o jogo")')
        _perguntar()

# -------------------- FUNÇÕES DE LÓGICA -------------------- #
def _tucuxiNado():
    """Move o Tucuxi de forma aleatória (0 a 2 casas)."""

    tucuxi_coords[1] = min(tucuxi_coords[1] + rd.choice([0,1,2]), len(MAPA[0])-1)

def _escolherNovaPergunta():
    """
    Escolhe aleatoriamente uma pergunta, embaralha alternativas e retorna essas informações.
    
    Processo:
    1. Seleciona uma pergunta aleatória do banco
    2. Extrai a pergunta e resposta correta
    3. Remove a pergunta da lista de opções
    4. Embaralha as alternativas
    5. Armazena pergunta, alternativas e índice da resposta correta
    """

    opcoes = rd.choice(perguntas).copy()

    pergunta = opcoes[0]
    resposta_correta = opcoes[-1]

    opcoes.pop(0) # remove a pergunta das alternativas
    rd.shuffle(opcoes)
    
    infos[4] = [pergunta,opcoes, str(opcoes.index(resposta_correta)+1)] # no final, opcoes viram as alternativas

def _analisarResposta():
    """
    Analisa a resposta do jogador:
    - Se correta, Amazonino avança 1-2 casas
    - Se errada, Amazonino recua 1-2 casas
    - Se 'sair', encerra o jogo
    
    Returns:
        str: Mensagem com o resultado da análise
    """
    resposta = infos[1].lower()
        # Só processa resposta se houver uma pergunta ativa
    if infos[4] and infos[4][0]:  # Verifica se há pergunta
        if resposta == "sair":
            _finalizarJogo()
            infos[1] = "Encerrando programa."
        elif resposta == infos[4][2]:
            desloc = rd.choice([1,2])
            amazon_coords[1] = min(amazon_coords[1] + desloc, len(MAPA[0])-1) # "len(MAPA[0])-1" dá a coord x máxima da tela 
            infos[1] = f"Resposta correta! Amazonino avança {desloc} casas."
        else:
            desloc = rd.choice([1,2])
            amazon_coords[1] = max(0, amazon_coords[1] - desloc) # impede que o boto se mova para "fora"
            infos[1] = f"Resposta errada. Amazonino recua {desloc} casas."
    
def _mensagem():
    if infos[1] not in ["1", "2", "3", "4", "5", "sair"]:
        print(f"\n{infos[1]}")
        _continuar()


def _finalizarJogo():
    """Finaliza o jogo alterando o estado de continuidade para False."""
    infos[0] = False

def _resultadoCorrida():
    """
    Verifica se algum dos botos chegou à linha de chegada e determina o vencedor.
    
    Estados possíveis:
    3 - Empate (ambos chegaram)
    1 - Amazonino venceu
    2 - Chiquito venceu
    """
    amazon_chegou = amazon_coords[1] >= CHEGADA_X
    tucuxi_chegou = tucuxi_coords[1] >= CHEGADA_X
    
    if amazon_chegou and tucuxi_chegou:
        infos[3] = 3  # Empate
        _finalizarJogo()
    elif amazon_chegou:
        infos[3] = 1  # Amazonino ganhou
        _finalizarJogo()
    elif tucuxi_chegou:
        infos[3] = 2  # Chiquito ganhou
        _finalizarJogo()

# -------------------- FUNÇÕES DE RENDER -------------------- #
def _desenharPixel(cor_texto, cor_fundo=0, caractere=PIXEL):
    """Imprime um pixel colorido no terminal usando ANSCII."""
    print(f"\033[38;5;{cor_texto};48;5;{cor_fundo}m{caractere}\033[0m", end="")

def _desenharMapa():
    """Renderiza o frame atual no terminal."""
    _limparTela()
    
    print(f"Rodada: {infos[2]}\n")
    _desenharBotos()

    for y in infos[5]:
        for x in y:
            _desenharPixel(x, x)
        print()
        

def _escreverPergunta():
    """
    Exibe a pergunta atual e suas alternativas numeradas.
    
    Formato:
    [Pergunta]
    
    1. [Alternativa 1]
    2. [Alternativa 2]
    3. [Alternativa 3]
    4. [Alternativa 4]
    """
    print("\n"+infos[4][0]+'\n')
    for i in range(len(infos[4][1])):
        print(f"{i+1}. {infos[4][1][i]}")
    print('\n(Escreva o número da alternativa escolhida, ou digite "sair", para finalizar o programa).\n')

def _resetarMapa():
    """Restaura o mapa base, sem os personagens."""
    infos[5] = [linha.copy() for linha in MAPA]

def _desenharBotos():
    """Atualiza o frame com as posições atuais dos botos."""
    infos[5][tucuxi_coords[0]][tucuxi_coords[1]] = tucuxi_cor
    infos[5][amazon_coords[0]][amazon_coords[1]] = amazonino_cor

def _limparTela():
    """Limpa o terminal (Windows, Linux, macOS)."""
    os.system("cls" if os.name == "nt" else "clear")

def _mostrarEstoria():
    """
    Exibe a história introdutória do jogo parágrafo por parágrafo.
    
    Cada parágrafo é mostrado em uma tela limpa com cor laranja,
    aguardando confirmação do jogador para continuar.
    """
    for paragrafo in HISTORIA:
        _limparTela()
        _printColorido(paragrafo, LARA)
        _continuar()

def _printColorido(texto, cor=0):
    """
    Imprime texto colorido no terminal usando códigos ANSI.
    
    Argumentoss:
        texto (str): Texto a ser impresso
        cor (int): Código da cor (0-255) da paleta ANSI 256 cores
    """
    print(f"\033[38;5;{cor}m{texto}\033[0m")

# ============================================================== #
# ----------------------- ETAPAS DO JOGO ----------------------- #
# ============================================================== #

def entrada():
    """Captura a entrada do jogador para a pergunta atual."""
    _perguntar()    

def etapaNovaRodada():
    """
    Prepara uma nova rodada do jogo.
    
    Inclui:
    - Selecionar nova pergunta
    - Incrementar contador de rodadas
    """
    _escolherNovaPergunta()
    infos[2] += 1
    
def etapaProcessamento():
    """
    Processa a resposta da rodada atual.
    
    Executa em sequência:
    - Análise da resposta do jogador
        . 
    - Movimento do adversário (Tucuxi)
    - Verificação de condições de vitória
    """
    _analisarResposta()
    _tucuxiNado()
    _resultadoCorrida()

def renderizacao():
    """
    Renderiza o estado completo do jogo.
    
    Inclui:
    - Reset do mapa base
    - Posicionamento dos botos
    - Desenho do mapa com cores
    - Exibição da pergunta atual
    """
    _resetarMapa()
    _desenharBotos()
    _desenharMapa()
    _escreverPergunta()

def mostrarResultadoFinal():
    """
    Exibe o resultado final do jogo baseado no estado armazenado.
    
    Estados:
    1 - Amazonino venceu
    2 - Chiquito venceu  
    3 - Empate
    Outro - Jogo interrompido
    """
    if infos[3] == 1:
        input("Amazonino venceu a corrida! 🏆")
    elif infos[3] == 2:
        input("Chiquito venceu a corrida! 🏆")
    elif infos[3] == 3:
        input("Empate! 🤝")
    else:
        input("Jogo Interrompido.")

# ============================================================== #
# -------------------------- EXECUÇÃO -------------------------- #
# ============================================================== #

def main():
    """
    Função principal que executa o fluxo completo do jogo.
    
    Fluxo:
    1. Exibe história introdutória
    2. Loop principal do jogo
    3. Processamento de rodadas
    4. Exibição do resultado final
    """
    _mostrarEstoria()
    while infos[0]:
        # MOSTRA o estado atual (com pergunta)
        if infos[2] != 0:
            renderizacao()

            # Pega a RESPOSTA do jogador
            entrada()

            # PROCESSA a resposta
            etapaProcessamento()
            _mensagem()
        etapaNovaRodada()
        renderizacao()

    # Pós-loop
    _limparTela()
    mostrarResultadoFinal()

# Inicia o jogo
main()