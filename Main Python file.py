import math


# This program will run to predict the premier league using machine learning from previous data and player transfers

class Team:
    def __init__(self, name):
        self.name = name
        self.player = []

    def add_player(self, new_transfer):
        self.player.append(new_transfer)
