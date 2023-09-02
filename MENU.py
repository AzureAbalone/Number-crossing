def welcome():  # - Main screen
    print()
    print("Number crossing")
    print("--------------")
    print("PLAY")
    print("SETTING")
    print("DOCS")
    print("QUIT")
    print("--------------")


def EASY():  # - Easy mode guide
    print()
    print("*** Easy:\nÔ nào đạt đến -6 hoặc 6 thì reset về 0.")
    print("- Ex:\nBefore:\n0 0 6 0\n0 6 -6 6\n0 0 6 0\n0 0 0 0\nAfter:\n0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0")
    print("->RETURN<-")


def NORMAL():  # - Normal mode guide
    print("*** Normal: Ô nào đạt đến -6 thì không reset.")
    print("- Ex:\nBefore:\n0 0 6 0\n0 6 -6 6\n0 0 6 0\n0 0 0 0\nAfter:\n0 0 0 0\n0 0 -6 0\n0 0 0 0\n0 0 0 0")
    print("->RETURN<-")


def HARD():  # - Hard mode guide
    print("*** Hard: Ô nào đạt đến -6 hoặc 6 thì không reset.")
    print("- Ex:\nBefore:\n0 0 6 0\n0 6 -6 6\n0 0 6 0\n0 0 0 0\nAfter:\n0 0 6 0\n0 6 -6 6\n0 0 6 0\n0 0 0 0")
    print("->RETURN<-")


def INSANE():  # - Insane mode guide
    print("*** Insane: Ô nào đạt đến -6 hoặc 6 sẽ thành ô bất biến và không thể tác động vào. Nếu bị thay đổi sẽ thua.")
    print("- Ex:\nBefore:\n0 0 6 0\n0 6 -6 6\n0 0 6 0\n0 0 0 0\n+ P1 turn: Dice = 5, Pos = 3 3\nAfter:\n0 0 6 0\n0 6 -1 6\n0 5 -5 5\n0 0 5 0\n--> P1 lose")
    print("->RETURN<-")


def DOCS():  # - Document menu
    print()
    print("* SCORE system")
    print("* How to PLAY")
    print("* EASY mode")
    print("* NORMAL mode")
    print("* HARD mode")
    print("* INSANE mode")
    print("->RETURN<-")


def PLAY(): # - Playing guide
    print()
    print("*** How to play: Chọn 1 ô sau khi tung xúc sắc, ô đó trừ đi điểm bằng xúc sắc, các ô xung quanh cộng điểm bằng xúc sắc.")
    print("- Ex:\nBefore:\n0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n+ Dice = 2\n+ Pos = 2 3\nAfter:\n0 0 2 0\n0 2 -2 2\n0 0 2 0\n0 0 0 0")
    print("->RETURN<-")


def SCORING(): # - Score system
    print()
    print("*** Scoring:\n* Ô nào đạt -6 trong lượt người chơi thì trừ 1 điểm của người đó, còn ô nào đạt 6 điểm thì người chơi đó nhận 1 điểm.")
    print("- Ex:\n0 0 6 0\n0 6 -6 6\n0 0 6 0\n0 0 0 0\n+ P1 score: 4(6 appears 4 times) - 1(-6 appears 1 time) = 3")
    print(
        "* Trong lượt của người chơi nào mà có ô vượt quá [-6, 6] hoặc điểm âm thì người đó thua.")
    print("- Ex:\n+ P2 score: -1\n+ P2 turn:\n0 0 7 0\n0 0 -9 0\n0 0 0 0\n0 8 0 0\n--> P2 lose!")
    print("* Ai đạt đủ điều kiện điểm hoặc hơn là thắng (mặc định là 6).")
    print("- Ex:\n+ P1 score: 6\n--> P1 win!")
    print("->RETURN<-")


def SETTING(): # - Setting menu
    import Modified_settings as modset
    from importlib import reload
    reload(modset)
    print()
    print(f"- Player: {modset.globals[0]}")
    print(f"- Size: {modset.globals[1]}")
    print(f"- Difficulty: {modset.globals[2]}")
    print(f"- Win condition: {modset.globals[3]}")
    print("->RETURN<-")
