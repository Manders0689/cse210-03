import random

from pyparsing import stringStart

class Word:
    """A Word that is a list with each item being a letter in the word.
    user attempts to guess.
    
    The responsibility of a Word is to choose a word as the hidden word, 
    and compare the user's guesses to letters within the chosen word.

    Attributes:
        _word_list (list[str]): List of words randomly chosen from.
        _word (string): word chosen from Word list.
        _display_word (list[str]): placeholder for each letter until correct guess.
    """

    def __init__(self):
        """Constructs a new instance of Word.
        
        Args:
            self (Card): An instance of Word.
        """
        self._word_list = ['apple', 'audio', 'zesty', 'fluffy']
        self._word = random.choice(self._word_list)
        self._word_output = []
        
        for i in range(len(self._word)):
            self._word_output.append('_')

    def _compare_letter(self, letter):
        """Compares the user guess letter to letters within the chosen_word list.
        
        Args:
            self (Card): An instance of Card.
        """
        if letter in self._word:
            return True
        else:
            return False
    
    def _display_word(self, new_letter):
        """Displays the word and any correctly guessed letters that are within the chosen_word.
        
        Args:
            self (Card): An instance of Card.
        """
        for i in range(len(self._word)):
            if new_letter == self._word[i]:
                self._word_output[i] = new_letter
        return self._word_output

    def is_found(self):
        if "".join(self._word_output) == self._word:
            return True
        else:
            return False
        
'''Methods:
    _compare_letter
        compare guess to chosen word
    _display_word
        update word output
'''   