import time
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multi_dict = md.MultiDictionary()

        self.multi_dict.addDictionary("italiano", "resources/Italian.txt")
        self.multi_dict.addDictionary("inglese", "resources/English.txt")
        self.multi_dict.addDictionary("spagnolo", "resources/Spanish.txt")

    def handleSentence(self, txtIn, language): #correzione
        tic_contains = time.time()
        words = replaceChars(txtIn)

        #Usa il metodo contains
        print("-"*30 + "\nUsing contains")
        for word in words:
            rich_word_contains= self.multi_dict.searchWord(word, language)
            if rich_word_contains and not rich_word_contains.corretta: #rich_word.corretta == False, verifico anche se esiste un dizionario per questa lingua
                print(word)
        toc_contains = time.time()
        tempo_contains = toc_contains - tic_contains
        print(f"Time elapsed {tempo_contains:.4f}")

        #Usa la ricerca lineare
        tic_lineare = time.time()

        print("-" * 30 +"\nUsing Linear Search")
        for word in words:
            rich_word_ricerca_lineare = self.multi_dict.searchWordLinear(word, language)
            if rich_word_ricerca_lineare and not rich_word_ricerca_lineare.corretta:
                print(word)
        toc_lineare = time.time()
        tempo_lineare = toc_lineare - tic_lineare
        print(f"Time elapsed {tempo_lineare:.4f}")

        #Usa la ricerca dicotomica
        tic_dichotomic = time.time()

        print("-" * 30 + "\nUsing Dichotomic")
        for word in words:
            rich_word_ricerca_dichotomic = self.multi_dict.searchWordDichotomic(word, language)
            if rich_word_ricerca_dichotomic and not rich_word_ricerca_dichotomic.corretta:
                print(word)
        toc_dichotomic = time.time()
        tempo_dichotomic = toc_dichotomic - tic_dichotomic
        print(f"Time elapsed {tempo_dichotomic:.4f}")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    text = text.lower()
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text.split()