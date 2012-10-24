#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
# ------------------------------ 
import threading
import os

from bot import Bot

# ------------------------------
# Classes
# ------------------------------ 

GAMES_PATH = "Games/"
BOTS_PATH = "bots/"

class Game(threading.Thread):
    """ Docstring for Game
    
   Meta-class which future games will herites. It defines main caractéristiques of games 

    """
    def __init__(self,name, bots):
        """ Initiate Game 
    
        @param name: Name of the game
        @param folder: folder where the game is
        
        """
        self.check_name(name)
        self.folder = GAMES_PATH + self.game_name
        self.import_bots(bots)

        threading.Thread.__init__(self)

    def check_name(self, name):
        """ Docstring of check_name
        
        Check if the name correspond to a folder containing the game
        And set name, path and bots_path
    
        @param name: name of the game
        
        """
        if not os.path.exists(GAMES_PATH + name):
            raise ValueError("Could not find the game at '{game}'".format(game = GAMES_PATH + name))
        else:
            self.game_name = name
            self.path = GAMES_PATH + self.game_name + "/"
            self.bots_path = self.path + BOTS_PATH

    def import_bots(self, bots):
        """ Docstring for import_bots
        
        Import bots which should be in self.bots_path
        
        """
        self.bots = [] 
        for b in bots:
            self.bots += [Bot(b, self.bots_path)]
        
    def main(self):
        """ Docstring for main
        
        Let the game going on
        
        """
        pass

    def det_winner(self):
        """ Docstring for det_winner
        
        Determine the winner
        
        """
        # Soucis! Tous les jeux ne se terminent pas de la même façon! Certain sont left to die et d'autres se jouent au score!
        pass

    # -------------------
    # Communication with bots

    def start_bots(self):
        """ Docstring for start_bots
        
        Start bots
        
        """
        for bot in self.bots:
            bot.start_bot()

    def ready_bots(self):
        """ Docstring for ready_bots
        
        Send the ready message to bots
        
        """
        for bot in self.bots:
            bot.ready()

    def end_bots(self):
        """ Docstring for end_bots
        
        Send the end of the game message to bots
        
        """
        for bot in self.bots:
            bot.send_msg("Q\n")

# ------------------------------
# Bloc principal
# ------------------------------

if __name__ == '__main__':
    pass


# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 

