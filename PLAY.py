
class insane:
    class threeP:
        def P1_condition():
            global table, P1_score, check_insane_neg_6, win_condition, win, check_insane_pos_6
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

    class fourP:
        def P1_condition():
            global table, P1_score, check_insane_neg_6, win_condition, win, check_insane_pos_6
            for idx, value in enumerate(table):
                if max(value) > 6 or min(value) < -6:
                    print()
                    print('Player 1 lose !!!')
                    win[0] = False
                    for idx, value in enumerate(table):
                        for temp_idx, temp_value in enumerate(value):
                            if temp_value > 6 or temp_value < -6:
                                table[idx][temp_idx] = 0
                    visualxP(4)
                    return
                if max(value) == 6:
                    for temp_idx, temp_value in enumerate(value):
                        if temp_value == 6 and not (check_insane_pos_6[idx][temp_idx]):
                            check_insane_pos_6[idx][temp_idx] = True
                            P1_score += 1
                        if temp_value != 6 and check_insane_pos_6[idx][temp_idx]:
                            # - Playground Visualization
                            visualxP(4)
                            print()
                            print('Player 1 lose !!!')
                            win[0] = False
                            check_insane_pos_6[idx][temp_idx] = False
                            return
                if min(value) == -6:
                    for temp_idx, temp_value in enumerate(value):
                        if temp_value == -6 and not (check_insane_neg_6[idx][temp_idx]):
                            check_insane_neg_6[idx][temp_idx] = True
                            P1_score -= 1
                        if temp_value != -6 and check_insane_neg_6[idx][temp_idx]:
                            # - Playground Visualization
                            visualxP(4)
                            print()
                            print('Player 1 lose !!!')
                            win[0] = False
                            check_insane_neg_6[idx][temp_idx] = False
                            return
            visualxP(4)
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

        def P2_condition():
            global table, P2_score, check_insane_neg_6, win_condition, win, check_insane_pos_6
            for idx, value in enumerate(table):
                if max(value) > 6 or min(value) < -6:
                    print()
                    print('Player 2 lose !!!')
                    win[1] = False
                    for idx, value in enumerate(table):
                        for temp_idx, temp_value in enumerate(value):
                            if temp_value > 6 or temp_value < -6:
                                table[idx][temp_idx] = 0
                    visualxP(4)
                    return
                if max(value) == 6:
                    for temp_idx, temp_value in enumerate(value):
                        if temp_value == 6 and not (check_insane_pos_6[idx][temp_idx]):
                            check_insane_pos_6[idx][temp_idx] = True
                            P2_score += 1
                        if temp_value != 6 and check_insane_pos_6[idx][temp_idx]:
                            # - Playground Visualization
                            visualxP(4)
                            print()
                            print('Player 2 lose !!!')
                            win[1] = False
                            check_insane_pos_6[idx][temp_idx] = False
                            return
                if min(value) == -6:
                    for temp_idx, temp_value in enumerate(value):
                        if temp_value == -6 and not (check_insane_neg_6[idx][temp_idx]):
                            check_insane_neg_6[idx][temp_idx] = True
                            P2_score -= 1
                        if temp_value != -6 and check_insane_neg_6[idx][temp_idx]:
                            # - Playground Visualization
                            visualxP(4)
                            print()
                            print('Player 2 lose !!!')
                            win[1] = False
                            check_insane_neg_6[idx][temp_idx] = False
                            return
            visualxP(4)
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

        def P3_condition():
            global table, P3_score, check_insane_neg_6, win_condition, win, check_insane_pos_6
            for idx, value in enumerate(table):
                if max(value) > 6 or min(value) < -6:
                    print()
                    print('Player 3 lose !!!')
                    win[2] = False
                    for idx, value in enumerate(table):
                        for temp_idx, temp_value in enumerate(value):
                            if temp_value > 6 or temp_value < -6:
                                table[idx][temp_idx] = 0
                    visualxP(4)
                    return
                if max(value) == 6:
                    for temp_idx, temp_value in enumerate(value):
                        if temp_value == 6 and not (check_insane_pos_6[idx][temp_idx]):
                            check_insane_pos_6[idx][temp_idx] = True
                            P3_score += 1
                        if temp_value != 6 and check_insane_pos_6[idx][temp_idx]:
                            # - Playground Visualization
                            visualxP(4)
                            print()
                            print('Player 3 lose !!!')
                            win[2] = False
                            check_insane_pos_6[idx][temp_idx] = False
                            return
                if min(value) == -6:
                    for temp_idx, temp_value in enumerate(value):
                        if temp_value == -6 and not (check_insane_neg_6[idx][temp_idx]):
                            check_insane_neg_6[idx][temp_idx] = True
                            P3_score -= 1
                        if temp_value != -6 and check_insane_neg_6[idx][temp_idx]:
                            # - Playground Visualization
                            visualxP(4)
                            print()
                            print('Player 3 lose !!!')
                            win[2] = False
                            check_insane_neg_6[idx][temp_idx] = False
                            return
            visualxP(4)
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

        def P4_condition():
            global table, P4_score, check_insane_neg_6, win_condition, win, check_insane_pos_6
            for idx, value in enumerate(table):
                if max(value) > 6 or min(value) < -6:
                    print()
                    print('Player 4 lose !!!')
                    win[3] = False
                    for idx, value in enumerate(table):
                        for temp_idx, temp_value in enumerate(value):
                            if temp_value > 6 or temp_value < -6:
                                table[idx][temp_idx] = 0
                    visualxP(4)
                    return
                if max(value) == 6:
                    for temp_idx, temp_value in enumerate(value):
                        if temp_value == 6 and not (check_insane_pos_6[idx][temp_idx]):
                            check_insane_pos_6[idx][temp_idx] = True
                            P4_score += 1
                        if temp_value != 6 and check_insane_pos_6[idx][temp_idx]:
                            # - Playground Visualization
                            visualxP(4)
                            print()
                            print('Player 4 lose !!!')
                            win[3] = False
                            check_insane_pos_6[idx][temp_idx] = False
                            return
                if min(value) == -6:
                    for temp_idx, temp_value in enumerate(value):
                        if temp_value == -6 and not (check_insane_neg_6[idx][temp_idx]):
                            check_insane_neg_6[idx][temp_idx] = True
                            P4_score -= 1
                        if temp_value != -6 and check_insane_neg_6[idx][temp_idx]:
                            # - Playground Visualization
                            visualxP(4)
                            print()
                            print('Player 4 lose !!!')
                            win[3] = False
                            check_insane_neg_6[idx][temp_idx] = False
                            return
            visualxP(4)
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
