from game.terminal_service import TerminalService
from game.guesser import Guesser
from game.jumper import Jumper
from game.word import Word

class Director:
    """Person who directs the game.
    
    The responsibility of a Director is to control the sequence of play.
    
    Attributes:
        jumper (Jumper): The game's jumper.
        is_playing (boolean): Whether or not to keep playing.
        guesser (Guesser): The game's seeker.
        word (Word): word from a list of word the guesser will be guessing.
        terminal_service: For getting and displaying information on the terminal.
    """
    
    def __init__(self):
        """Constructs a new Director.
        
        Ars:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._guesser = Guesser()
        self._word = Word()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Ars:
            self (Director): an instance of Director.
        """
        self._terminal_service.write_text(self._word._display_word(self._guesser.get_guess()))
        self._terminal_service.print_jumper(self._jumper.get_jumper())
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            
    def _get_inputs(self):
        """ Get random word from Word class. 
        
        Args:
            self (Director): An instance of Director.
        """
        newGuess = self._terminal_service.read_text("Guess a letter (a-z): ")
        self._guesser.set_guess(newGuess.lower())
        while self._guesser.if_duplicate_guess() == 1 or self._guesser.if_duplicate_guess() == 2:
            if self._guesser.if_duplicate_guess() == 1:
                newGuess = self._terminal_service.read_text("\nYou\'ve already guessed this letter. Please guess a different letter [a-z]: ")
                self._guesser.set_guess(newGuess)
            elif self._guesser.if_duplicate_guess() == 2:
                newGuess = self._terminal_service.read_text("\nThat isn't a letter. Please guess a different letter [a-z]: ")
                self._guesser.set_guess(newGuess)                                                
        
    def _do_updates(self):
        """ Compares guess to chosen_word.

        If correct, changes display word with correct letter.
        if wrong, changes jumper.

        Args:
            self (Director): An instance of Director.
        """
        newGuess = self._guesser.get_guess()
        if self._word._compare_letter(newGuess):
            self._word._display_word(self._word)
        else: 
            self._jumper.update_jumper()
        
    def _do_outputs(self):
        """Prints jumper and display word.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text(self._word._display_word(self._guesser.get_guess()))
        if self._jumper.has_fallen():
            self._jumper.update_jumper()
        self._terminal_service.print_jumper(self._jumper.get_jumper())
        if self._jumper.has_fallen() or self._word._is_found():
            self._is_playing = False
        
             
        
        
    """Methods
    
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
        show word update
        show jumper update
    """