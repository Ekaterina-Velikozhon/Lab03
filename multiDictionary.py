import dictionary as d
import richWord as rw

class MultiDictionary:

    def __init__(self):
        self.dictionaries = {}

    def printDic(self, language):
        print(self.dictionaries[language])

    def searchWord(self, word, language):
        if language in self.dictionaries:
            is_correct = self.dictionaries[language].contains(word.lower())
            rich_W = rw.RichWord(word)
            rich_W.corretta = is_correct #setta il valore della variabile "corretta"
            return rich_W
        else:
            print("Dizionario non disponibile:(")
            return None

    def addDictionary(self, language, filename):
        self.dictionaries[language] = d.Dictionary(language, filename)

    def searchWordLinear(self, word, language):
        if language in self.dictionaries:
            dictionary = self.dictionaries[language]  # Ottiengo il dizionario della lingua selezionata; converto il set in una lista
            is_correct = False  # Variabile per controllare se la parola è presente

            # Implementazione della ricerca lineare
            for w in dictionary.get_words():
                if word.lower() == w.lower():
                    is_correct = True
                    break #Esce dal ciclo appena trova la parola

            rich_W = rw.RichWord(word)
            rich_W.corretta = is_correct
            return rich_W
        else:
            print("Dizionario non disponibile:(")
            return None

    def searchWordDichotomic(self, word, language):
        dictionary = self.dictionaries[language]
        if language in self.dictionaries:
            dictionary = sorted(dictionary.get_words())  # Converte il set in lista ordinata
            is_correct = False

            parte_sinistra, parte_destra = 0, len(dictionary)-1 # sinistra = 0, destra = len -1
            while parte_sinistra <= parte_destra:
                centro = (parte_sinistra + parte_destra) // 2
                if dictionary[centro] == word.lower():
                    is_correct = True #Elemento trovato
                elif dictionary[centro] < word.lower():
                    parte_sinistra = centro + 1 #Cerca nella meta destra
                else:
                    parte_destra = centro - 1 #Cerca nella meta sinistra

            rich_W = rw.RichWord(word)
            rich_W.corretta = is_correct
            return rich_W
        else:
            print("Dizionario non disponibile :(")
            return None