import MENU


def run():
    while True:
        # - How to play
        MENU.DOCS()
        # - Documentation input
        temp = input("What do you want to know: ").capitalize()
        # ! If the input is wrong, input until it is right
        while temp not in {"Play", "Return", "Insane", "Hard", "Normal", "Easy", "Score"}:
            MENU.DOCS()
            print("INVALID DOCS!")
            print()
            temp = input("What do you want to know: ").capitalize()
        if temp == "Return":  # - Exit documentation
            break
        while True:
            match temp:
                case "Score":  # - Scoring documentation
                    MENU.SCORING()
                case "Play":  # - Play documentation
                    MENU.PLAY()
                case "Easy":  # - Easy documentation
                    MENU.EASY()
                case "Normal":  # - Normal documentation
                    MENU.NORMAL()
                case "Hard":  # - Hard documentation
                    MENU.HARD()
                case "Insane":  # - Insane documentation
                    MENU.INSANE()
            # - Exit the current documentation
            back = input("Go back: ").upper()
            # ! If the input is wrong, input until it is right
            while back not in {"RETURN"}:
                MENU.SCORING()
                print("INVALD!")
                back = input("Go back: ").upper()
            if back == "RETURN":
                break
