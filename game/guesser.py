

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
        self.guess = ''

    def get_guess(self):
        """Gets a guess from the user"""

    def if_duplicate_guess(self):
        """Compare guess to guess list and determine if duplicate
        If a duplicate, prompt for new guess"""

    def add_guess(self):
        "Add guess to guesses list"