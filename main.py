from curses import wrapper
from game import Game, GameState
from entities import CharacterClass, Player
from data import Sprite


##TODO
#[x] Integrera curses
#[x] tisdagsdemo
#[x] InputHandler
#[ ] roaming 
#[ ] battlescene
#[ ] character creation

def create_player(name: str, char_class: CharacterClass, sprite: Sprite, x: int = 0, y: int = 0) -> Player:
    return Player(
        name=name,
        sprite=sprite,
        stats=char_class.initial_stats,
        x=x,
        y=y,
        role=char_class.display_name,
    )

def main(stdscr):
    game = Game(stdscr)
    game.run()

if __name__ == "__main__":
    wrapper(main)
    main()



