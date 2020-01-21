import string
import random
import requests

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy()
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        # recherche dans le dico
        reponse_api = requests.get('https://wagon-dictionary.herokuapp.com/'+word)
        if reponse_api.status_code != 200:
            raise ("ERROR API")
        reponse_json=reponse_api.json()
        if "found" not in reponse_json:
            raise ("ERROR API")
        if not bool(reponse_json["found"]):
            return False

        return True
