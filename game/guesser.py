

class Guesser:
    """The person guessing the hidden word
    
    The resposibility of a Guesser is to keep track of the letters guessed in hidden word.
    
    Attributes:
        guesses (list): stores guesses made.
        guess (string): induvidual letter guessed.
        """
    
    """Methods
        get_guess
        if_duplicate_guess
            compare current guess with guesses_list         
        add_guess to guesses_list
    """

    def __init__(self):
        """Constructs a new Guesser

        Args:
            self (Guesser): An instance of Guesser.
        """
        self.guess_list = []
        self._guess = ''

    def get_guess(self):
        """Get guess from the user"""
        return self._guess
   

    def if_duplicate_guess(self):
        """Compare guess to guess list and determine if duplicate
        If a duplicate, prompt for new guess"""
        if self._guess in self.guess_list:
            return 1
        elif self._guess.isalpha() and (len(self._guess) < 2):
            self.guess_list.append(self._guess)  
            return 0
        else:
            return 2
        
    def set_guess(self, letter):
        self._guess = letter