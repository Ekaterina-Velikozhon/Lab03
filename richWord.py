class RichWord:
    def __init__(self, parola):
        self._parola = parola # this is a string
        self._corretta = False #this is a bool

    @property #getter
    def corretta(self):
        # print("getter of parola called" )
        return self._corretta
    #sia "parola" che "corretta" sono private! -> qundi devo utilizzare i metodi Getter e Setter
    @corretta.setter #setter, setta il valore di "corretta"
    def corretta(self, boolValue):
        # print("setter of parola called" )
        self._corretta = boolValue

    def __str__(self):
        return self._parola + self._corretta