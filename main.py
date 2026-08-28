from curses import wrapper
import curses
from game import Game

##TODO
#[x] Integrera curses
#[x] tisdagsdemo
#[x] InputHandler
#[ ] roaming 
#[ ] battlescene
#[ ] character creation

def main(stdscr):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(True)
    
    game = Game(stdscr)
    game.run()

    while game.is_running:
        game.update()

if __name__ == "__main__":
    wrapper(main)



