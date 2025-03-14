class Dictionary:
    def __init__(self, lingua, filename):
        self.lingua = lingua

        self.words = set()
        self.loadDictionary(filename)

    def loadDictionary(self, path):
        try:
            with open(path, 'r', encoding="utf-8") as file:
                for line in file:
                    self.words.add(line.strip().lower())
        except FileNotFoundError:
            print(f"Errore: Il file '{path}' non è stato trovato:(")

    def printAll(self):
        parole = ""
        for word in self.words:
            if len(parole) == len(self.words):
                parole += word
            else:
                parole += word + " "
        print(parole)

    def contains(self, word):
        return word in self.words

    def get_words(self): #è necessario per estrarre le parole dal mio oggetto Dictionary in un formato iterabile
        return self.words