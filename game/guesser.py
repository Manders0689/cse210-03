

class Guesser:
    """The person guessing the hidden word
    
    The resposibility of a Guesser is to keep track of the letters guessed in hidden word.
    
    Attributes:
        guesses (list[str]): stores guesses made.
        guess (string): induvidual letter guessed.
    """
    
    """Methods
        get_guess
        if_duplicate_guess
            compare current guess with guesses_list         
            add_guess to guesses_list
        set_guess
    """

    def __init__(self):
        """Constructs a new Guesser

        Args:
            self (Guesser): An instance of Guesser.
        """
        self.guess_list = []
        self._guess = ''

    def get_guess(self):
        """Gets the current guess.
        
        Returns:
            string: The current guess
        """
        return self._guess
   
    def if_duplicate_guess(self):
        """Checks if letter has already been guessed.

        Args:
            self (Guesser): An instance of Guesser.
            guess (string): The current guess.
        """
        if self._guess in self.guess_list:
            return 1
        elif self._guess.isalpha() and (len(self._guess) < 2):
            self.guess_list.append(self._guess)  
            return 0
        else:
            return 2
        
    def set_guess(self, letter):
        """Sets the current guess.

        Args:
            self (Guesser): An instance of Guesser.
            guess (string): The current guess.
        """
        self._guess = letter