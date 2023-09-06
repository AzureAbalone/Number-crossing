import MENU
import SETTING
import DOCS
from random import randint
from time import sleep
import Modified_settings as modset
from importlib import reload


class PLAY():
    def visualxP(maxP):
        global size, P1_score, P2_score, table, win #- For unbound error
        print()
        # - Display the table according to the number of players
        match maxP:
            case 2:
                print(f'* Score:\nP1:{P1_score}\nP2:{P2_score}')
            case 3:
                global P3_score
                match win[0]:
                    case None: print(f"P1:{P1_score}")
                    case True: print("P1: Win")
                    case False: print("P1: Lose")
                match win[1]:
                    case None: print(f"P2:{P2_score}")
                    case True: print("P2: Win")
                    case False: print("P2: Lose")
                match win[2]:
                    case None: print(f"P3:{P3_score}")
                    case True: print("P3: Win")
                    case False: print("P3: Lose")
            case 4:
                global P4_score
                match win[0]:
                    case None: print(f"P1:{P1_score}")
                    case True: print("P1: Win")
                    case False: print("P1: Lose")
                match win[1]:
                    case None: print(f"P2:{P2_score}")
                    case True: print("P2: Win")
                    case False: print("P2: Lose")
                match win[2]:
                    case None: print(f"P3:{P3_score}")
                    case True: print("P3: Win")
                    case False: print("P3: Lose")
                match win[3]:
                    case None: print(f"P4:{P4_score}")
                    case True: print("P4: Win")
                    case False: print("P4: Lose")
        for i in table:
            for j in i:
                #- Format the table if negative numbers exist
                print(j, end='  ') if str(j)[0] == '-' else print(j, end='   ')
            print()
        print('----'*size)

    def Px_process(numP, mode):
        global table, P4_score, check_neg_6, win_condition, win, check_pos_6, P1_score, P2_score, P3_score, count, size, check_insane_pos_6, check_insane_neg_6
        for i in range(1, numP+1): #- Player turn
            match numP:
                case 3:
                    if win.count(False) == 2: #- If 2 players lose
                        print(f"Player {win.index(None)+1} win !!!")
                        return
                    if win.count(False) == 1 and win.count(True) == 1: #- If 1 player wins and 1 player loses
                        print(f"Player {win.index(None)+1} lose !!!")
                        return
                    if win.count(True) == 2: #- If 2 players win
                        print(f"Player {win.index(None)+1} lose !!!")
                        return
                case 4:
                    if win.count(False) == 3: #- If 3 players lose
                        print(f"Player {win.index(None)+1} win !!!")
                        break
                    if win.count(False) == 2 and win.count(True) == 1: #- If 2 players lose and 1 player wins
                        print(f"Player {win.index(None)+1} lose !!!")
                        break
                    if win.count(False) == 1 and win.count(True) == 2: #- If 1 player loses and 2 players win
                        print(f"Player {win.index(None)+1} win !!!")
                        break
                    if win.count(True) == 3: #- If 3 players win
                        print(f"Player {win.index(None)+1} lose !!!")
                        break
            if win[i-1] != None: #- Check if current player win or lose
                continue
            #- Rolling phase
            P_dice = randint(1, 6)
            print("R", end='')
            sleep(0.1)
            print("o", end='')
            sleep(0.1)
            print("l", end='')
            sleep(0.1)
            print("l", end='')
            sleep(0.1)
            print("i", end='')
            sleep(0.1)
            print("n", end='')
            sleep(0.1)
            print("g", end='')
            for _ in range(3):
                sleep(0.5)
                print(".", end='')
            print()
            print(f'- Player {i} dice: {P_dice}')
            check = True
            #! Check if player's input is valid 
            while check:
                P_pos = input(
                    "- Select where to put (Row then column): ").split()
                try:
                    while len(P_pos) != 2 or int(P_pos[0]) not in range(1, size+1) or int(P_pos[1]) not in range(1, size+1):
                        print("INVALID POSITION!")
                        P_pos = input(
                            "- Select where to put (Row then column): ").split()
                except Exception:
                    while len(P_pos) != 2 or not (P_pos[0].isnumeric() and P_pos[1].isnumeric()):
                        print("INVALID POSITION!")
                        P_pos = input(
                            "- Select where to put (Row then column): ").split()
                if int(P_pos[0]) in range(1, size+1) or int(P_pos[1]) in range(1, size+1):
                    check = False
                    P_pos = list(map(int, P_pos))
            #- Processing (center)
            table[P_pos[0]-1][P_pos[1]-1] -= P_dice
            # - Processing (inside)
            if 1 < P_pos[0] < size and 1 < P_pos[1] < size:
                table[P_pos[0]-1][P_pos[1]-2] += P_dice  # - Left
                table[P_pos[0]-1][P_pos[1]] += P_dice  # - Right
                table[P_pos[0]-2][P_pos[1]-1] += P_dice  # - Up
                table[P_pos[0]][P_pos[1]-1] += P_dice  # - Down
            # - Processing (corner)
            elif P_pos == [1, 1]:  # - Up left
                table[P_pos[0]-1][P_pos[1]] += P_dice  # - Right
                table[P_pos[0]][P_pos[1]-1] += P_dice  # - Down
            elif P_pos == [1, size]:  # - Up right
                table[P_pos[0]-1][P_pos[1]-2] += P_dice  # - Left
                table[P_pos[0]][P_pos[1]-1] += P_dice  # - Down
            elif P_pos == [size, 1]:  # - Down left
                table[P_pos[0]-1][P_pos[1]] += P_dice  # - Right
                table[P_pos[0]-2][P_pos[1]-1] += P_dice  # - Up
            elif P_pos == [size, size]:  # - Down right
                table[P_pos[0]-1][P_pos[1]-2] += P_dice  # - Left
                table[P_pos[0]-2][P_pos[1]-1] += P_dice  # - Up
            # - Process (edge)
            # - First row
            elif P_pos[0] == 1 and P_pos[1] in range(2, size):
                table[P_pos[0]-1][P_pos[1]-2] += P_dice  # - Left
                table[P_pos[0]-1][P_pos[1]] += P_dice  # - Right
                table[P_pos[0]][P_pos[1]-1] += P_dice  # - Down
            # - Last row
            elif P_pos[0] == size and P_pos[1] in range(2, size):
                table[P_pos[0]-1][P_pos[1]-2] += P_dice  # - Left
                table[P_pos[0]-1][P_pos[1]] += P_dice  # - Right
                table[P_pos[0]-2][P_pos[1]-1] += P_dice  # - Up
            # - Last column
            elif P_pos[1] == 1 and P_pos[0] in range(2, size):
                table[P_pos[0]-1][P_pos[1]] += P_dice  # - Right
                table[P_pos[0]-2][P_pos[1]-1] += P_dice  # - Up
                table[P_pos[0]][P_pos[1]-1] += P_dice  # - Down
            # - First column
            elif P_pos[1] == size and P_pos[0] in range(2, size):
                table[P_pos[0]-1][P_pos[1]-2] += P_dice  # - Left
                table[P_pos[0]-2][P_pos[1]-1] += P_dice  # - Up
                table[P_pos[0]][P_pos[1]-1] += P_dice  # - Down
            match mode:
                case "Easy":
                    match numP:
                        case 2:
                            if count == 1:
                                return
                            for idx, value in enumerate(table):
                                if max(value) > 6 or min(value) < -6:
                                    PLAY.visualxP(numP)
                                    print()
                                    match i:
                                        case 1:
                                            print('Player 1 lose !!!')
                                            print('Player 2 win !!!')
                                        case 2:
                                            print('Player 1 win !!!')
                                            print('Player 2 lose !!!')
                                    count += 1
                                    return
                                if max(value) == 6:
                                    match i:
                                        case 1:
                                            P1_score += value.count(6)
                                        case 2:
                                            P2_score += value.count(6)
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == 6:
                                            table[idx][temp_idx] = 0
                                if min(value) == -6:
                                    match i:
                                        case 1:
                                            P1_score -= value.count(-6)
                                        case 2:
                                            P2_score -= value.count(-6)
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == -6:
                                            table[idx][temp_idx] = 0
                            PLAY.visualxP(numP)
                            match i:
                                case 1:
                                    if P1_score >= win_condition:
                                        print()
                                        print('Player 1 win !!!')
                                        print('Player 2 lose !!!')
                                        count += 1
                                        return
                                    elif P1_score < 0:
                                        print()
                                        print('Player 1 lose !!!')
                                        print('Player 2 win !!!')
                                        count += 1
                                        return
                                case 2:
                                    if P2_score >= win_condition:
                                        print()
                                        print('Player 1 lose !!!')
                                        print('Player 2 win !!!')
                                        count += 1
                                        return
                                    elif P2_score < 0:
                                        print()
                                        print('Player 1 win !!!')
                                        print('Player 2 lose !!!')
                                        count += 1
                                        return
                        case 3:
                            for idx, value in enumerate(table):
                                if max(value) > 6 or min(value) < -6:
                                    print()
                                    print(f'Player {i} lose !!!')
                                    win[i-1] = False
                                    for idx, value in enumerate(table):
                                        for temp_idx, temp_value in enumerate(value):
                                            if temp_value > 6 or temp_value < -6:
                                                table[idx][temp_idx] = 0
                                    PLAY.visualxP(numP)
                                    return
                                if max(value) == 6:
                                    match i:
                                        case 1:
                                            P1_score += value.count(6)
                                        case 2:
                                            P2_score += value.count(6)
                                        case 3:
                                            P3_score += value.count(6)
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == 6:
                                            table[idx][temp_idx] = 0
                                if min(value) == -6:
                                    match i:
                                        case 1:
                                            P1_score -= value.count(-6)
                                        case 2:
                                            P2_score -= value.count(-6)
                                        case 3:
                                            P3_score -= value.count(-6)
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == -6:
                                            table[idx][temp_idx] = 0
                            PLAY.visualxP(numP)
                            match i:
                                case 1:
                                    if P1_score >= win_condition:
                                        print()
                                        print('Player 1 win !!!')
                                        win[0] = True
                                        return
                                    elif P1_score < 0:
                                        print()
                                        print('Player 1 lose !!!')
                                        win[0] = False
                                        return
                                case 2:
                                    if P2_score >= win_condition:
                                        print()
                                        print('Player 2 win !!!')
                                        win[1] = True
                                        return
                                    elif P2_score < 0:
                                        print()
                                        print('Player 2 lose !!!')
                                        win[1] = False
                                        return
                                case 3:
                                    if P3_score >= win_condition:
                                        print()
                                        print('Player 3 win !!!')
                                        win[2] = True
                                        return
                                    elif P3_score < 0:
                                        print()
                                        print('Player 3 lose !!!')
                                        win[2] = False
                                        return
                        case 4:
                            for idx, value in enumerate(table):
                                if max(value) > 6 or min(value) < -6:
                                    print()
                                    print(f'Player {i} lose !!!')
                                    win[i-1] = False
                                    for idx, value in enumerate(table):
                                        for temp_idx, temp_value in enumerate(value):
                                            if temp_value > 6 or temp_value < -6:
                                                table[idx][temp_idx] = 0
                                    PLAY.visualxP(numP)
                                    return
                                if max(value) == 6:
                                    match i:
                                        case 1:
                                            P1_score += value.count(6)
                                        case 2:
                                            P2_score += value.count(6)
                                        case 3:
                                            P3_score += value.count(6)
                                        case 4:
                                            P4_score += value.count(6)
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == 6:
                                            table[idx][temp_idx] = 0
                                if min(value) == -6:
                                    match i:
                                        case 1:
                                            P1_score -= value.count(-6)
                                        case 2:
                                            P2_score -= value.count(-6)
                                        case 3:
                                            P3_score -= value.count(-6)
                                        case 4:
                                            P4_score -= value.count(-6)
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == -6:
                                            table[idx][temp_idx] = 0
                            PLAY.visualxP(numP)
                            match i:
                                case 1:
                                    if P1_score >= win_condition:
                                        print()
                                        print('Player 1 win !!!')
                                        win[0] = True
                                        return
                                    elif P1_score < 0:
                                        print()
                                        print('Player 1 lose !!!')
                                        win[0] = False
                                        return
                                case 2:
                                    if P2_score >= win_condition:
                                        print()
                                        print('Player 2 win !!!')
                                        win[1] = True
                                        return
                                    elif P2_score < 0:
                                        print()
                                        print('Player 2 lose !!!')
                                        win[1] = False
                                        return
                                case 3:
                                    if P3_score >= win_condition:
                                        print()
                                        print('Player 3 win !!!')
                                        win[2] = True
                                        return
                                    elif P3_score < 0:
                                        print()
                                        print('Player 3 lose !!!')
                                        win[2] = False
                                        return
                                case 4:
                                    if P4_score >= win_condition:
                                        print()
                                        print('Player 4 win !!!')
                                        win[3] = True
                                        return
                                    elif P4_score < 0:
                                        print()
                                        print('Player 4 lose !!!')
                                        win[3] = False
                                        return
                case "Normal":
                    match numP:
                        case 2:
                            for idx, value in enumerate(table):
                                if max(value) > 6 or min(value) < -6:
                                    PLAY.visualxP(numP)
                                    print()
                                    match i:
                                        case 1:
                                            print('Player 1 lose !!!')
                                            print('Player 2 win !!!')
                                        case 2:
                                            print('Player 1 win !!!')
                                            print('Player 2 lose !!!')
                                    count += 1
                                    return
                                if max(value) == 6:
                                    match i:
                                        case 1:
                                            P1_score += value.count(6)
                                        case 2:
                                            P2_score += value.count(6)
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == 6:
                                            table[idx][temp_idx] = 0
                                if min(value) == -6:
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == -6 and not (check_neg_6[idx][temp_idx]):
                                            check_neg_6[idx][temp_idx] = True
                                            match i:
                                                case 1:
                                                    P1_score -= 1
                                                case 2:
                                                    P2_score -= 1
                                        elif temp_value != -6:
                                            check_neg_6[idx][temp_idx] = False
                            PLAY.visualxP(numP)
                            match i:
                                case 1:
                                    if P1_score >= win_condition:
                                        print()
                                        print('Player 1 win !!!')
                                        print('Player 2 lose !!!')
                                        count += 1
                                        return
                                    elif P1_score < 0:
                                        print()
                                        print('Player 1 lose !!!')
                                        print('Player 2 win !!!')
                                        count += 1
                                        return
                                case 2:
                                    if P2_score >= win_condition:
                                        print()
                                        print('Player 1 lose !!!')
                                        print('Player 2 win !!!')
                                        count += 1
                                        return
                                    elif P2_score < 0:
                                        print()
                                        print('Player 1 win !!!')
                                        print('Player 2 lose !!!')
                                        count += 1
                                        return
                        case 3:
                            for idx, value in enumerate(table):
                                if max(value) > 6 or min(value) < -6:
                                    print()
                                    print(f'Player {i} lose !!!')
                                    win[i-1] = False
                                    for idx, value in enumerate(table):
                                        for temp_idx, temp_value in enumerate(value):
                                            if temp_value > 6 or temp_value < -6:
                                                table[idx][temp_idx] = 0
                                    PLAY.visualxP(numP)
                                    return
                                if max(value) == 6:
                                    match i:
                                        case 1:
                                            P1_score += value.count(6)
                                        case 2:
                                            P2_score += value.count(6)
                                        case 3:
                                            P3_score += value.count(6)
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == 6:
                                            table[idx][temp_idx] = 0
                                if min(value) == -6:
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == -6 and not (check_neg_6[idx][temp_idx]):
                                            check_neg_6[idx][temp_idx] = True
                                            match i:
                                                case 1:
                                                    P1_score -= 1
                                                case 2:
                                                    P2_score -= 1
                                                case 3:
                                                    P3_score -= 1
                                        elif temp_value != -6:
                                            check_neg_6[idx][temp_idx] = False
                            PLAY.visualxP(numP)
                            match i:
                                case 1:
                                    if P1_score >= win_condition:
                                        print()
                                        print('Player 1 win !!!')
                                        win[0] = True
                                        return
                                    elif P1_score < 0:
                                        print()
                                        print('Player 1 lose !!!')
                                        win[0] = False
                                        return
                                case 2:
                                    if P2_score >= win_condition:
                                        print()
                                        print('Player 2 win !!!')
                                        win[1] = True
                                        return
                                    elif P2_score < 0:
                                        print()
                                        print('Player 2 lose !!!')
                                        win[1] = False
                                        return
                                case 3:
                                    if P3_score >= win_condition:
                                        print()
                                        print('Player 3 win !!!')
                                        win[2] = True
                                        return
                                    elif P3_score < 0:
                                        print()
                                        print('Player 3 lose !!!')
                                        win[2] = False
                                        return
                        case 4:
                            for idx, value in enumerate(table):
                                if max(value) > 6 or min(value) < -6:
                                    print()
                                    print(f'Player {i} lose !!!')
                                    win[i-1] = False
                                    for idx, value in enumerate(table):
                                        for temp_idx, temp_value in enumerate(value):
                                            if temp_value > 6 or temp_value < -6:
                                                table[idx][temp_idx] = 0
                                    PLAY.visualxP(numP)
                                    return
                                if max(value) == 6:
                                    match i:
                                        case 1:
                                            P1_score += value.count(6)
                                        case 2:
                                            P2_score += value.count(6)
                                        case 3:
                                            P3_score += value.count(6)
                                        case 4:
                                            P4_score += value.count(6)
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == 6:
                                            table[idx][temp_idx] = 0
                                if min(value) == -6:
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == -6 and not (check_neg_6[idx][temp_idx]):
                                            check_neg_6[idx][temp_idx] = True
                                            match i:
                                                case 1:
                                                    P1_score -= 1
                                                case 2:
                                                    P2_score -= 1
                                                case 3:
                                                    P3_score -= 1
                                                case 4:
                                                    P4_score -= 1
                                        elif temp_value != -6:
                                            check_neg_6[idx][temp_idx] = False
                            PLAY.visualxP(numP)
                            match i:
                                case 1:
                                    if P1_score >= win_condition:
                                        print()
                                        print('Player 1 win !!!')
                                        win[0] = True
                                        return
                                    elif P1_score < 0:
                                        print()
                                        print('Player 1 lose !!!')
                                        win[0] = False
                                        return
                                case 2:
                                    if P2_score >= win_condition:
                                        print()
                                        print('Player 2 win !!!')
                                        win[1] = True
                                        return
                                    elif P2_score < 0:
                                        print()
                                        print('Player 2 lose !!!')
                                        win[1] = False
                                        return
                                case 3:
                                    if P3_score >= win_condition:
                                        print()
                                        print('Player 3 win !!!')
                                        win[2] = True
                                        return
                                    elif P3_score < 0:
                                        print()
                                        print('Player 3 lose !!!')
                                        win[2] = False
                                        return
                                case 4:
                                    if P4_score >= win_condition:
                                        print()
                                        print('Player 4 win !!!')
                                        win[3] = True
                                        return
                                    elif P4_score < 0:
                                        print()
                                        print('Player 1 lose !!!')
                                        win[3] = False
                                        return
                case "Hard":
                    match numP:
                        case 2:
                            for idx, value in enumerate(table):
                                if max(value) > 6 or min(value) < -6:
                                    PLAY.visualxP(numP)
                                    print()
                                    match i:
                                        case 1:
                                            print('Player 1 lose !!!')
                                            print('Player 2 win !!!')
                                        case 2:
                                            print('Player 1 win !!!')
                                            print('Player 2 lose !!!')
                                    count += 1
                                    return
                                if max(value) == 6:
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == 6 and not (check_pos_6[idx][temp_idx]):
                                            check_pos_6[idx][temp_idx] = True
                                            match i:
                                                case 1:
                                                    P1_score += 1
                                                case 2:
                                                    P2_score += 1
                                        elif temp_value != 6:
                                            check_pos_6[idx][temp_idx] = False
                                if min(value) == -6:
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == -6 and not (check_neg_6[idx][temp_idx]):
                                            check_neg_6[idx][temp_idx] = True
                                            match i:
                                                case 1:
                                                    P1_score -= 1
                                                case 2:
                                                    P2_score -= 1
                                        elif temp_value != -6:
                                            check_neg_6[idx][temp_idx] = False
                            match i:
                                case 1:
                                    PLAY.visualxP(numP)
                                    if P1_score >= win_condition:
                                        print()
                                        print('Player 1 win !!!')
                                        print('Player 2 lose !!!')
                                        count += 1
                                        return
                                    elif P1_score < 0:
                                        print()
                                        print('Player 1 lose !!!')
                                        print('Player 2 win !!!')
                                        count += 1
                                        return
                                case 2:
                                    PLAY.visualxP(numP)
                                    if P2_score >= win_condition:
                                        print()
                                        print('Player 1 lose !!!')
                                        print('Player 2 win !!!')
                                        count += 1
                                        return
                                    elif P2_score < 0:
                                        print()
                                        print('Player 1 win !!!')
                                        print('Player 2 lose !!!')
                                        count += 1
                                        return
                        case 3:
                            for idx, value in enumerate(table):
                                if max(value) > 6 or min(value) < -6:
                                    print()
                                    print(f'Player {i} lose !!!')
                                    win[i-1] = False
                                    for idx, value in enumerate(table):
                                        for temp_idx, temp_value in enumerate(value):
                                            if temp_value > 6 or temp_value < -6:
                                                table[idx][temp_idx] = 0
                                    PLAY.visualxP(numP)
                                    return
                                if max(value) == 6:
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == 6 and not (check_pos_6[idx][temp_idx]):
                                            check_pos_6[idx][temp_idx] = True
                                            match i:
                                                case 1:
                                                    P1_score += 1
                                                case 2:
                                                    P2_score += 1
                                                case 3:
                                                    P3_score += 1
                                        elif temp_value != 6:
                                            check_pos_6[idx][temp_idx] = False
                                if min(value) == -6:
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == -6 and not (check_neg_6[idx][temp_idx]):
                                            check_neg_6[idx][temp_idx] = True
                                            match i:
                                                case 1:
                                                    P1_score -= 1
                                                case 2:
                                                    P2_score -= 1
                                                case 3:
                                                    P3_score -= 1
                                        elif temp_value != -6:
                                            check_neg_6[idx][temp_idx] = False
                            PLAY.visualxP(numP)
                            match i:
                                case 1:
                                    if P1_score >= win_condition:
                                        print()
                                        print('Player 1 win !!!')
                                        win[0] = True
                                        return
                                    elif P1_score < 0:
                                        print()
                                        print('Player 1 lose !!!')
                                        win[0] = False
                                        return
                                case 2:
                                    if P2_score >= win_condition:
                                        print()
                                        print('Player 2 win !!!')
                                        win[1] = True
                                        return
                                    elif P2_score < 0:
                                        print()
                                        print('Player 2 lose !!!')
                                        win[1] = False
                                        return
                                case 3:
                                    if P3_score >= win_condition:
                                        print()
                                        print('Player 3 win !!!')
                                        win[2] = True
                                        return
                                    elif P3_score < 0:
                                        print()
                                        print('Player 3 lose !!!')
                                        win[2] = False
                                        return
                        case 4:
                            for idx, value in enumerate(table):
                                if max(value) > 6 or min(value) < -6:
                                    print()
                                    print(f'Player {i} lose !!!')
                                    win[i-1] = False
                                    for idx, value in enumerate(table):
                                        for temp_idx, temp_value in enumerate(value):
                                            if temp_value > 6 or temp_value < -6:
                                                table[idx][temp_idx] = 0
                                    PLAY.visualxP(numP)
                                    return
                                if max(value) == 6:
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == 6 and not (check_pos_6[idx][temp_idx]):
                                            check_pos_6[idx][temp_idx] = True
                                            match i:
                                                case 1:
                                                    P1_score += 1
                                                case 2:
                                                    P2_score += 1
                                                case 3:
                                                    P3_score += 1
                                                case 4:
                                                    P4_score += 1
                                        elif temp_value != 6:
                                            check_pos_6[idx][temp_idx] = False
                                if min(value) == -6:
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == -6 and not (check_neg_6[idx][temp_idx]):
                                            check_neg_6[idx][temp_idx] = True
                                            match i:
                                                case 1:
                                                    P1_score -= 1
                                                case 2:
                                                    P2_score -= 1
                                                case 3:
                                                    P3_score -= 1
                                                case 4:
                                                    P4_score -= 1
                                        elif temp_value != -6:
                                            check_neg_6[idx][temp_idx] = False
                            PLAY.visualxP(numP)
                            match i:
                                case 1:
                                    if P1_score >= win_condition:
                                        print()
                                        print('Player 1 win !!!')
                                        win[0] = True
                                        return
                                    elif P1_score < 0:
                                        print()
                                        print('Player 1 lose !!!')
                                        win[0] = False
                                        return
                                case 2:
                                    if P2_score >= win_condition:
                                        print()
                                        print('Player 2 win !!!')
                                        win[1] = True
                                        return
                                    elif P2_score < 0:
                                        print()
                                        print('Player 2 lose !!!')
                                        win[1] = False
                                        return
                                case 3:
                                    if P3_score >= win_condition:
                                        print()
                                        print('Player 3 win !!!')
                                        win[2] = True
                                        return
                                    elif P3_score < 0:
                                        print()
                                        print('Player 3 lose !!!')
                                        win[2] = False
                                        return
                                case 4:
                                    if P4_score >= win_condition:
                                        print()
                                        print('Player 4 win !!!')
                                        win[3] = True
                                        return
                                    elif P4_score < 0:
                                        print()
                                        print('Player 4 lose !!!')
                                        win[3] = False
                                        return
                case "Insane":
                    match numP:
                        case 2:
                            for idx, value in enumerate(table):
                                if max(value) > 6 or min(value) < -6:
                                    PLAY.visualxP(numP)
                                    print()
                                    match i:
                                        case 1:
                                            print('Player 1 lose !!!')
                                            print('Player 2 win !!!')
                                        case 2:
                                            print('Player 1 win !!!')
                                            print('Player 2 lose !!!')
                                    count += 1
                                    return
                                if max(value) == 6:
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == 6 and check_insane_pos_6[idx][temp_idx] == 0:
                                            check_insane_pos_6[idx][temp_idx] = "X"
                                            match i:
                                                case 1:
                                                    P1_score += 1
                                                case 2:
                                                    P2_score += 1
                                        if temp_value != 6 and check_insane_pos_6[idx][temp_idx] == "X":
                                            PLAY.visualxP(numP)
                                            print()
                                            match i:
                                                case 1:
                                                    print('Player 1 lose !!!')
                                                    print('Player 2 win !!!')
                                                case 2:
                                                    print('Player 1 win !!!')
                                                    print('Player 2 lose !!!')
                                            count += 1
                                            return
                                if min(value) == -6:
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == -6 and check_insane_neg_6[idx][temp_idx] == 0:
                                            check_insane_neg_6[idx][temp_idx] = "X"
                                            match i:
                                                case 1:
                                                    P1_score -= 1
                                                case 2:
                                                    P2_score -= 1
                                        if temp_value != -6 and check_insane_neg_6[idx][temp_idx] == "X":
                                            PLAY.visualxP(numP)
                                            print()
                                            match i:
                                                case 1:
                                                    print('Player 1 lose !!!')
                                                    print('Player 2 win !!!')
                                                case 2:
                                                    print('Player 1 win !!!')
                                                    print('Player 2 lose !!!')
                                            count += 1
                                            return
                            PLAY.visualxP(numP)
                            match i:
                                case 1:
                                    if P1_score >= win_condition:
                                        print()
                                        print('Player 1 win !!!')
                                        print('Player 2 lose !!!')
                                        count += 1
                                        return
                                    elif P1_score < 0:
                                        print()
                                        print('Player 1 lose !!!')
                                        print('Player 2 win !!!')
                                        count += 1
                                        return
                                case 2:
                                    if P2_score >= win_condition:
                                        print()
                                        print('Player 1 lose !!!')
                                        print('Player 2 win !!!')
                                        count += 1
                                        return
                                    elif P2_score < 0:
                                        print()
                                        print('Player 1 win !!!')
                                        print('Player 2 lose !!!')
                                        count += 1
                                        return
                        case 3:
                            for idx, value in enumerate(table):
                                if max(value) > 6 or min(value) < -6:
                                    print()
                                    print(f'Player {i} lose !!!')
                                    win[i-1] = False
                                    for idx, value in enumerate(table):
                                        for temp_idx, temp_value in enumerate(value):
                                            if temp_value > 6 or temp_value < -6:
                                                table[idx][temp_idx] = 0
                                    PLAY.visualxP(numP)
                                    return
                                if max(value) == 6:
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == 6 and check_insane_pos_6[idx][temp_idx] == 0:
                                            check_insane_pos_6[idx][temp_idx] = "X"
                                            match i:
                                                case 1:
                                                    P1_score += 1
                                                case 2:
                                                    P2_score += 1
                                                case 3:
                                                    P3_score += 1
                                        if temp_value != 6 and check_insane_pos_6[idx][temp_idx] == "X":
                                            print()
                                            print(f'Player {i} lose !!!')
                                            win[i-1] = False
                                            check_insane_pos_6[idx][temp_idx] = 0
                                            PLAY.visualxP(numP)
                                            return
                                if min(value) == -6:
                                    for temp_idx, temp_value in enumerate(value):
                                        if temp_value == -6 and check_insane_neg_6[idx][temp_idx] == 0:
                                            check_insane_neg_6[idx][temp_idx] = "X"
                                            match i:
                                                case 1:
                                                    P1_score -= 1
                                                case 2:
                                                    P2_score -= 1
                                                case 3:
                                                    P3_score -= 1
                                        if temp_value != -6 and check_insane_neg_6[idx][temp_idx] == "X":
                                            print()
                                            print(f'Player {i} lose !!!')
                                            win[i-1] = False
                                            check_insane_neg_6[idx][temp_idx] = 0
                                            PLAY.visualxP(numP)
                                            return
                            PLAY.visualxP(numP)
                            match i:
                                case 1:
                                    if P1_score >= win_condition:
                                        print()
                                        print('Player 1 win !!!')
                                        win[0] = True
                                        return
                                    elif P1_score < 0:
                                        print()
                                        print('Player 1 lose !!!')
                                        win[0] = False
                                        return
                                case 2:
                                    if P2_score >= win_condition:
                                        print()
                                        print('Player 2 win !!!')
                                        win[1] = True
                                        return
                                    elif P2_score < 0:
                                        print()
                                        print('Player 2 lose !!!')
                                        win[1] = False
                                        return
                                case 3:
                                    if P3_score >= win_condition:
                                        print()
                                        print('Player 3 win !!!')
                                        win[2] = True
                                        return
                                    elif P3_score < 0:
                                        print()
                                        print('Player 3 lose !!!')
                                        win[2] = False
                                        return


while True:
    # - Menu
    MENU.welcome()
    choose = input("Select: ").upper()  # - Input section
    while choose not in {"PLAY", "SETTING", "QUIT", "DOCS"}:
        print()
        print("INVALID SELECTION!")
        MENU.welcome()
        choose = input("Select: ").upper()
    match choose:
        case "QUIT":  # - Exit the game
            quit()
        case "DOCS":  # - Run the documentation
            DOCS.run()
        case "SETTING":  # - Modify the setting
            SETTING.run()
        case "PLAY":  # - Play the game
            # - Game func
            mode = modset.globals[0]
            size = modset.globals[1]
            table = [[0]*size for _ in range(size)]
            check_pos_6 = [[False]*size for _ in range(size)]
            check_neg_6 = [[False]*size for _ in range(size)]
            difficulty = modset.globals[2]
            win_condition = modset.globals[3]
            check_insane_pos_6 = [[0]*size for _ in range(size)]
            check_insane_neg_6 = [[0]*size for _ in range(size)]
            P1_score, P2_score, P3_score, P4_score, count = 0, 0, 0, 0, 0
            win = [None]*4
            reload(modset)
            match mode:
                case "2P":
                    PLAY.visualxP(2)
                    while count == 0:
                        match difficulty:
                            case "Easy":  # - Easy mode
                                # - Processing
                                PLAY.Px_process(2, "Easy")
                            case "Normal":  # - Normal mode
                                # - Process
                                PLAY.Px_process(2, "Normal")
                            case "Hard":  # - Hard mode
                                # - Processing
                                PLAY.Px_process(2, "Hard")
                            case "Insane":  # - Insane mode
                                # - Process
                                PLAY.Px_process(2, "Insane")
                case "3P":
                    PLAY.visualxP(3)
                    del win[-1]
                    match difficulty:
                        case "Easy":  # - Easy mode
                            while win.count(None) > 1:
                                PLAY.Px_process(3, "Easy")
                            PLAY.Px_process(3, "Easy")
                        case "Normal":  # - Normal mode
                            while win.count(None) > 1:
                                PLAY.Px_process(3, "Normal")
                            PLAY.Px_process(3, "Normal")
                        case "Hard":  # - Hard mode
                            while win.count(None) > 1:
                                PLAY.Px_process(3, "Hard")
                            PLAY.Px_process(3, "Hard")
                        case "Insane":  # - Insane mode
                            quit()
                            while win.count(None) > 1:
                                PLAY.Px_process(3, "Insane")
                            PLAY.Px_process(3, "Insane")
                case "4P":
                    PLAY.PLAY.visualxP(numP)
                    match difficulty:
                        case "Easy":  # - Easy mode
                            while win.count(None) > 1:
                                PLAY.Px_process(4, "Easy")
                            PLAY.Px_process(4, "Easy")
                        case "Normal":  # - Normal mode
                            while win.count(None) > 1:
                                PLAY.Px_process(4, "Normal")
                            PLAY.Px_process(4, "Normal")
                        case "Hard":  # - Hard mode
                            while win.count(None) > 1:
                                PLAY.Px_process(4, "Hard")
                            PLAY.Px_process(4, "Hard")
                        case "Insane": # - Insane mode
                            print("THE GAME HAS ENCOUNTERED A FATAL ERROR!")
                            quit()
                            while True:
                                if win.count(False) == 3:
                                    print(f"Player {win.index(None)+1} win !!!")
                                    break
                                if win.count(False) == 2 and win.count(True) == 1:
                                    print(f"Player {win.index(None)+1} lose !!!")
                                    break
                                if win.count(False) == 1 and win.count(True) == 2:
                                    print(f"Player {win.index(None)+1} win !!!")
                                    break
                                if win.count(True) == 3:
                                    print(f"Player {win.index(None)+1} lose !!!")
                                    break
                                if win[0] == None:
                                    # - P1 turn
                                    # - Process
                                    PLAY.Px_process(1)
                                    # - Condition check
                                    check("Insane", 4, 1)
                                if win.count(False) == 3:
                                    print(f"Player {win.index(None)+1} win !!!")
                                    break
                                if win.count(False) == 2 and win.count(True) == 1:
                                    print(f"Player {win.index(None)+1} lose !!!")
                                    break
                                if win.count(False) == 1 and win.count(True) == 2:
                                    print(f"Player {win.index(None)+1} win !!!")
                                    break
                                if win.count(True) == 3:
                                    print(f"Player {win.index(None)+1} lose !!!")
                                    break
                                if win[1] == None:
                                    # - P2 turn
                                    # - Process
                                    PLAY.Px_process(2)
                                    # - Condition check
                                    check("Insane", 4, 2)
                                if win.count(False) == 3:
                                    print(f"Player {win.index(None)+1} win !!!")
                                    break
                                if win.count(False) == 2 and win.count(True) == 1:
                                    print(f"Player {win.index(None)+1} lose !!!")
                                    break
                                if win.count(False) == 1 and win.count(True) == 2:
                                    print(f"Player {win.index(None)+1} win !!!")
                                    break
                                if win.count(True) == 3:
                                    print(f"Player {win.index(None)+1} lose !!!")
                                    break
                                if win[2] == None:
                                    # - P3 turn
                                    # - Process
                                    PLAY.Px_process(3)
                                    # - Condition check
                                    check("Insane", 4, 3)
                                if win.count(False) == 3:
                                    print(f"Player {win.index(None)+1} win !!!")
                                    break
                                if win.count(False) == 2 and win.count(True) == 1:
                                    print(f"Player {win.index(None)+1} lose !!!")
                                    break
                                if win.count(False) == 1 and win.count(True) == 2:
                                    print(f"Player {win.index(None)+1} win !!!")
                                    break
                                if win.count(True) == 3:
                                    print(f"Player {win.index(None)+1} lose !!!")
                                    break
                                if win[3] == None:
                                    # - P4 turn
                                    # - Process
                                    PLAY.Px_process(4)
                                    # - Condition check
                                    check("Insane", 4, 4)

