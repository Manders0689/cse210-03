from game.terminal_service import TerminalService
from game.guesser import Guesser
from game.jumper import Jumper
from game.word import Word

class Director:
    '''Person who directs the game.
    
    The responsibility of a Director is to control the sequence of play.
    
    Attributes:
        jumper (Jumper): The game's jumper.
        is_playing (boolean): Whether or not to keep playing.
        guesser (Guesser): The game's seeker.
        word (Word): word from a list of word the guesser will be guessing.
        terminal_service: For getting and displaying information on the terminal.
    '''
    
    def __init__(self):
        '''Constructs a new Director.
        
        Ars:
            self (Director): an instance of Director.
        '''
        self._jumper = Jumper()
        self._is_playing = True
        self._guesser = Guesser()
        self._word = Word()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        '''Starts the game by running the main game loop.
        
        Ars:
            self (Director): an instance of Director.
        '''
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            
    def _get_inputs(self):
        ''''''
        
        
        
        
        
    
    '''Methods
    
    start-game
        start the game by running the main game loop
    _get_inputs
        word
        guess
    _do_update
        compares guess to word
        update word if correct guess
        update jumper if wrong guess
    _do_outputs
        show word and jumper update
    '''