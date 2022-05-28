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
    def display_jumper(tries):
        stages = [  # final state: no parachute
                """
        
                0
               /|\
               / \
            """,

            """
               \ /
                0
               /|\
               / \
            """,

            """
              \   /
               \ /
                0
               /|\
               / \
            """,

            """
              /___\
              \   /
               \ /
                0
               /|\
               / \
            """,
       
            """
               ___
              /___\
              \   /
               \ /
                0
               /|\
               / \
            """
    ]
    return stages[tries]


       """ if letter is true, do nothing """


       """if letter is false, remove top line
       redraw jumper """

      

