import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()
    txtIn = input()
    # Add input control here!
    match txtIn:
        case "1":
            print("Inserisci la tua frase in Italiano\n")
            txtIn = input()
            sc.handleSentence(txtIn,"italiano")
            continue

        case "2":
            print("Inserisci la tua frase in Inglese\n")
            txtIn = input()
            sc.handleSentence(txtIn,"inglese")
            continue

        case "3":
            print("Inserisci la tua frase in Spagnolo\n")
            txtIn = input()
            sc.handleSentence(txtIn,"spagnolo")
            continue

        case "4":
            break

        case _:  # Se l'utente inserisce un numero non valido
            print("Opzione non valida. Riprova.")