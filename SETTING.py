from Modified_settings import modified as mod


mode = mod[0]
size = mod[1]
difficulty = mod[2]
win_condition = mod[3]


def player():  # - Modify number of players
    # - Input numeber of players
    temp = input("- Select player(s): \n+ 2P\n+ 3P\n+ 4P\n-->").upper()
    # ! If the input is wrong, input until it is right
    while temp not in {"3P", "4P", "2P"}:
        print("INVALID MODE!")
        temp = input("- Select player(s): \n+ 2P\n+ 3P\n+ 4P\n-->").upper()
    return temp


def table_size():  # - Modify size of playground
    global table
    # - Input size of playground
    temp = input("- Size of playground (3 to 15): ")
    check = True
    # ! If the input is wrong, input until it is right
    while check:
        try:  # * Check if the input is appropriate
            while int(temp) not in range(3, 16):
                print("INVALID SIZE!")
                temp = input("- Size of playground (3 to 15): ")
        except Exception:  # * Check if the input is numerical or not
            while not (temp.isnumeric()):
                print("INVALID SIZE!")
                temp = input("- Size of playground (3 to 15): ")
        if int(temp) in range(3, 16):
            check = False
    return int(temp)


def win():  # - Modify the score a player needs to win
    temp = input("- Select win condition (3 to 20): ")  # - Input the condition
    check = True
    # ! If the input is wrong, input until it is right
    while check:
        try:  # * Check if the input is appropriate
            while int(temp) not in range(3, 21):
                print("INVALID WIN CONDITION!")
                temp = input("- Select win condition (3 to 20): ")
        except Exception:  # * Check if the input is numerical or not
            while not (temp.isnumeric()):
                print("INVALID WIN CONDITION!")
                temp = input("- Select win condition (3 to 20): ")
        if int(temp) in range(3, 21):
            check = False
    return int(temp)


def diff():  # - Modify the difficulty
    temp = input(
        "- Select difficulty: \n+ Easy\n+ Normal\n+ Hard\n+ Insane\n-->").capitalize()  # - Input the difficulty
    # ! If the input is wrong, input until it is right
    while temp not in {"Easy", "Normal", "Hard", "Insane"}:
        print("INVALID DIFFICULTY!")
        temp = input("- Select difficulty: ").capitalize()
    return temp


def run():  # - Run the modifier
    global mode, win_condition, difficulty, size  # - Prevent unbound error
    while True:
        # - Adjust gameplay
        import MENU
        MENU.SETTING()  # - Display the setting menu
        # - Input the section you want to modify
        temp = input("Adjust your gameplay: ").capitalize()
        # ! If the input is wrong, input until it is right
        while temp not in {"Player", "Difficulty", "Size", "Return", "Win"}:
            print("INVALID SETTING!")
            MENU.SETTING()
            temp = input("Adjust your gameplay: ").capitalize()
        with open('Modified_settings.py', 'r+') as mod:
            match temp:
                case "Return":  # - Quit modifying
                    break
                case "Player":  # - Select the number of players
                    mode = player()
                case "Size":  # - Adjust playground
                    size = table_size()
                case "Difficulty":  # - Choose difficulty
                    difficulty = diff()
                case "Win":  # - Choose how many score need to win
                    win_condition = win()
            mod.write(
                f'modified = ["{mode}", {size}, "{difficulty}", {win_condition}]               ')  # ! Warning: For modifying purposes only!
