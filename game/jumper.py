class Jumper:
    """The drawing of the jumper.
    
    The resposibility of the Jumper is to keep track and count amount of wrong guesses.
    
    Attributes:
        Jumper (list or array)
        """
    
    """Methods
        draw_jumper

        update_jumper
            remove first line in list/array if incorrect guess.
    """

    def __init__(self):
        """  draw jumper """
        self._jumper = [' ___', '/___\\', '\\   /', ' \\ /', '  0', ' /|\\', ' / \\', '', '^^^^^^^']


    def has_fallen(self):
      if len(self._jumper) == 5:
          return True
      else: 
          return False
    
    def update_jumper(self):
        if self._jumper[0] == '  0':
            self._jumper[0] = '  x'
        else:
            self._jumper.pop(0)

      
    def get_jumper(self):
        return self._jumper
