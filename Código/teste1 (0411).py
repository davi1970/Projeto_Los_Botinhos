import curses
#último recurso caso nem eu, nem o arthur consiga achar uma outra biblioteca que não conflita com o atual método de
#"renderização" do terminal.
#terminologia utilizada: stdscr -> standard screen

#Pra te guiar arthur <3
def main(stdscr): #func. principal
    stdscr.clear() #limpa a tela
    curses.curs_set(0)  #remove o cursorzinho (eu chamo de quadrado) que pisca ao abrir o terminal e esperar por input

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Bem-Vindo À X! Pressione (1) para Y, (2) para Z ou Esc para sair.")
        stdscr.refresh() #atualiza a tela com a string acima

        tecla = stdscr.getch() #func. que captura os caracteres digitados e retorna elas em integer code, formato reconhecido pela biblioteca para gerenciar teclas pressionadas  
        if tecla == ord('1'): #ord() é uma func. que converte os integer codes para strings. 
            stdscr.clear()
            stdscr.addstr(0, 0, "The missile knows where it is at all times.")
            stdscr.refresh()
            curses.napms(2000)  # Pausa por 2 segundos antes de voltar à string inicial
        elif tecla == ord('2'):  
            stdscr.clear()
            stdscr.addstr(0, 0, "It knows this by subtracting where it is from where it isn't.")
            stdscr.refresh()
            curses.napms(2000)
        elif tecla == 27: 
            break

curses.wrapper(main) 